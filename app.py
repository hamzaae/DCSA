from flask import Flask, jsonify, render_template, url_for, request, redirect
from ws import run_etl

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/onecom', methods=['POST', 'GET'])
def onecom():
    if request.method == 'POST':
        comment = request.form['commentInput']
        return render_template("onecom.html", comment=comment, form_submitted=True)
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





if __name__ == "__main__":
    app.run(debug=True)