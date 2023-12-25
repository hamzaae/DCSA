import os
from flask import Flask, jsonify, render_template, url_for, request, redirect
from mongoDB import *
from utils.data import *
from utils.model import *
from utils.use_api import query
from utils.ws import run_etl
# from farasa.stemmer import FarasaStemmer
import joblib


############################################################################
model_path = "model/dcsa-x.joblib"
model = joblib.load(model_path)

# stemmer = FarasaStemmer()
emoji_mapping = create_emoji_mapping(pd.read_csv("Dataset/emojis.csv"))
all_stopwords = get_stop_words("Dataset/all_stop_words.json")

uri = os.getenv("MONGO_URI")
client = connect_mongo(uri)

HG_URL = "https://api-inference.huggingface.co/models/CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment"
hg_faceToken = os.getenv("HG_TOKEN")
headers = {"Authorization": hg_faceToken}
############################################################################


def predict_api(comments, stemmer=False):
    """Make predictions on a set of data."""
    id=0
    arabic_text = {}
    for text in comments:
        r = detect_text_lang(text)
        if r==-1:
            dert = derrej(text)
            arabic_text[id] = [r, text, clean_text(dert)]
        else:
            arabic_text[id] = [r, text, clean_text(text)]
        id+=1

    # if stemmer:
    #     # ignored now
    #     stemmed_text = stemmer.stem(cleaned_text)
    # else:
    #     stemmed_text = cleaned_text
    
    label = model.predict([value[2] for value in arabic_text.values()])
    score = model.predict_proba([value[2] for value in arabic_text.values()])

    db_data = []
    for key, value in arabic_text.items():
        hg_label, hg_score = query({"inputs": value[2]}, HG_URL, headers)
        db_data.append({
            "comment": value[1],
            "cleaned_comment": value[2],
            "stemmed_comment": value[2],
            "labels": [[int(label[key]), float(score[key][0 if label[key]==0 else 1])], 
                       [hg_label, hg_score], 
                       [1, 1]]
        })
    insert_many_data(client, db_data, "dcsa", "comments")
    return label, score, arabic_text



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/onecom', methods=['POST', 'GET'])
def onecom():
    if request.method == 'POST':
        comment = request.form['commentInput']
        label, score, artex = predict_api([comment])
        label = "Positive" if label[0]==0 else "Negative"
        score = score[0][0] if label=="Positive" else score[0][1]
        at = artex[0][0]
        comment = artex[0][1]
        cc = artex[0][2]
        if at==1:
            at = "Original"
        elif at==-1:
            at = "Translated"
        else:
            at = "Not Sure"
        return render_template("onecom.html", comment=comment, cc=cc, at=at, label=label, score=f"{score:.4f}", form_submitted=True)
    else:
        return render_template('onecom.html', form_submitted=False)


@app.route('/lapress', methods=['POST', 'GET'])
def lapress():
    if request.method == 'POST':
        link = request.form['linkInput']
        title, comments = run_etl(link)

        if title is not None and comments is not None:
            label, score, artex = predict_api(comments)
            c_label = []
            c_score = []
            for i in range(len(label)):
                l = "Positive" if label[i]==0 else "Negative"
                s = score[i][0] if l=="Positive" else score[i][1]
                c_score.append(s.round(3))
                c_label.append(l)
            
            # suppose to be darija arabic text
            # at = artex[0][0]
            # comment = artex[0][1]
            # cc = artex[0][2]
            return render_template("lapress.html", title=title, comments=comments, c_label=c_label, c_score=c_score, form_submitted=True)
        else:
            error_message = "Unable to retrieve title and comments from the provided link."
            return render_template("lapress.html", error_message=error_message, form_submitted=True)

    else:
        return render_template('lapress.html', form_submitted=False)

@app.route('/dcsa_api', methods=['POST'])
def dcsa_api():
    try:
        text = request.form['text']
        label, score, arabic_text = predict_api([text])
        result = {
            'label': int(label[0]),
            'score': float(score[0][0] if label[0] == 0 else score[0][1]),
            'arabic_text': arabic_text[0][1],
            'cleaned_text': arabic_text[0][2]
        }
        return jsonify({'result': result, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500



if __name__ == "__main__":
    app.run(debug=True)
    