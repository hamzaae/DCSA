from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/onecom')
def onecom():
    return render_template('onecom.html')

@app.route('/lapress')
def lapress():
    return render_template('lapress.html')




if __name__ == "__main__":
    app.run(debug=True)