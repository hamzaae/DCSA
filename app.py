from flask import Flask, jsonify, render_template, url_for, request, redirect
from ws import run_etl

app = Flask(__name__)





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/onecom')
def onecom():
    return render_template('onecom.html')

@app.route('/lapress', methods=['POST', 'GET'])
def lapress():
    if request.method == 'POST':
        # data = request.get_json()
        # link = data.get('link', '')
        link = request.form['linkInput']
        title, comments = run_etl(link)
        return render_template("lapress.html", title=title, comments=comments)
    else:
        return render_template('lapress.html')

    # return render_template('lapress.html')




if __name__ == "__main__":
    app.run(debug=True)