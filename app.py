from flask import Flask, render_template
from firebase import firebase


app = Flask(__name__)


@app.route('/')
def Index():
    firebase_app = firebase.FirebaseApplication(
        'https://happynews-99c12.firebaseio.com/')
    content = firebase_app.get('/happynews-99c12/', '')

    print("\n\n", content, "\n\n")
    news_content = []
    title = []
    desc = []
    publish_date = []
    textblob_pol = []
    watson_pol = []
    news_station = []
    url_to_news = []
    url_img = []
    all_info = []
    for key, val in content.items():
        print(key)
        print(val['Url_to_img'])
        title.append(val['Title'])
        desc.append(val['Description'])
        publish_date.append(val['Publish_date'])
        textblob_pol.append(round(val['Textblob_polarity'], 3))
        watson_pol.append(round(val['Watson_polarity'], 3))
        news_station.append(val['News_station']['name'])
        url_to_news.append(val['Url_to_news'])
        news_content.append(val['Content'])
        url_img.append(val['Url_to_img'])

    all_info = (zip(title, desc, publish_date, textblob_pol,
                    watson_pol, news_station, news_content, url_to_news, url_img))
    return render_template('index.html', context=all_info)


if __name__ == "__main__":
    app.run(debug=True)
