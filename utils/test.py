from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Read the JSON file
    with open('derrej.json', encoding='utf-8') as f:
        data = json.load(f)


    # Pass the data to the template
    return render_template('forms.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
