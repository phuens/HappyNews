from flask import Flask, render_template
from firebase import firebase


app = Flask(__name__)


@app.route('/')
def Index():
    firebase_app = firebase.FirebaseApplication(
        'https://happynews-99c12.firebaseio.com/')
    content = firebase_app.get('/happynews-99c12/', '')

    for key, val in content.items():
        return render_template('index.html', title=val['Description'])


if __name__ == "__main__":
    app.run(debug=True)
