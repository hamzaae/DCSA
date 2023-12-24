from flask import Flask, jsonify, render_template, url_for, request, redirect
from use_api import predict_api
from ws import run_etl
# main branch
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/onecom', methods=['POST', 'GET'])
def onecom():
    if request.method == 'POST':
        comment = request.form['commentInput']
        label, score = predict_api(comment)
        return render_template("onecom.html", comment=comment, label=label, score=f"{score:.4f}", form_submitted=True)
    else:
        return render_template('onecom.html', form_submitted=False)


@app.route('/lapress', methods=['POST', 'GET'])
def lapress():
    if request.method == 'POST':
        link = request.form['linkInput']
        title, comments = run_etl(link)

        if title is not None and comments is not None:
            return render_template("lapress.html", title=title, comments=comments, form_submitted=True)
        else:
            error_message = "Unable to retrieve title and comments from the provided link."
            return render_template("lapress.html", error_message=error_message, form_submitted=True)

    else:
        return render_template('lapress.html', form_submitted=False)

@app.route('/dcsa_api', methods=['POST'])
def dcsa_api():
    try:
        text = request.form['text']
        
        prediction = f"Processed result for: {text}"

        return jsonify({'prediction': prediction, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500



if __name__ == "__main__":
    app.run(debug=True)