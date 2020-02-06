from flask import Flask, render_template
from firebase import firebase


app = Flask(__name__)


@app.route('/')
def Index():
    firebase_app = firebase.FirebaseApplication(
        'https://happynews-99c12.firebaseio.com/')
    content = firebase_app.get('/happynews-99c12/', '')

    for key, val in content.items():
        return render_template('index.html', url_to_news=val['Url_to_news'], news_source=val['News_station']['name'], date=val['Publish_date'], url_to_img=val['Url_to_img'],
                               content=val['Content'], title=val['Title'], description=val['Description'])


if __name__ == "__main__":
    app.run(debug=True)
