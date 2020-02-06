from newsapi.newsapi_client import NewsApiClient
from textblob import TextBlob
from firebase import firebase
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions
import config


newsapi = NewsApiClient(api_key=config.API_KEY)


def main():
    readSourceFile()


"""
Reads a txt file containing the source of the news and passes it as a parameter to call getContent function.
@return: void
@param: void
"""


def readSourceFile():
    # Read the file containing the news sources.
    source_file = open("sources.txt", "r")
    sources = source_file.readlines()			# Read line by line.
    source_file.close()							# Close.

    # call the getContent function one by one with the news source as parameter.
    for i in range(len(sources)):
        print(sources[i])
        getContent(sources[i])


"""
Calls the newsAPI to get the content and stores the different information associated
with the news articles.
@return : news title, desciption, image link, content, polarity and subjectivity of content
@param: source of the news from where you are extracting the content. eg. 'bbc-news'
"""


def getContent(news_source):

    title = []
    desc = []
    img = []
    content = []
    publish_date = []
    textblob_pol = []
    watson_pol = []
    news_station = []
    news_author = []
    url_to_news = []

   # Call the newsAPI
    news = newsapi.get_everything(
        sources=news_source, language='en', sort_by='relevancy', page=5)

    # Store the articles returned from the API call.
    articles = news['articles']

    authenticator = IAMAuthenticator(config.IBM_API_KEY)
    watson_nlu = NaturalLanguageUnderstandingV1(
        version='2019-07-12', authenticator=authenticator)
    watson_nlu.set_service_url(config.IBM_URL)

    # Loop through all the articles.
    for i in range(len(articles)):
        myarticles = articles[i]
        # Some articles have no content so need to check that.
        if (myarticles['content'] != None):
            print(" \n Actual Content of the News CHECK: ",
                  myarticles['content'], "\n\n")
            textblob_polarity = TextBlob(
                myarticles['content']).sentiment.polarity
            watson_sentiment = watson_nlu.analyze(
                text=myarticles['content'], features={"sentiment": {}})
            watson_polarity = watson_sentiment.result['sentiment']['document']['score']

            if (textblob_polarity > 0.3 and watson_polarity > 0.3):
                if (myarticles['urlToImage'] != None)
                textblob_pol.append(textblob_polarity)
                watson_pol.append(watson_polarity)
                content.append(myarticles['content'])
                title.append(myarticles['title'])
                desc.append(myarticles['description'])
                img.append(myarticles['urlToImage'])
                publish_date.append(myarticles['publishedAt'])
                news_station.append(myarticles['source'])
                url_to_news.append(myarticles['url'])
                news_author.append(myarticles['author'])

        else:
            continue

    postContent(title, desc, img, content, textblob_pol,
                watson_pol, publish_date, news_station, news_author, url_to_news)


"""
Uploads the content of the news to the database.
@return: void
@para: news title, desciption, image link, content, polarity and subjectivity of content
"""


def postContent(title, desc, img, content,  textblob_polarity, watson_polarity, publish_date, news_station, news_author, url_to_news):
    firebase_app = firebase.FirebaseApplication(
        'https://happynews-99c12.firebaseio.com/')
    for i in range(len(title)):

        data = {
            'Title': title[i],
            'Publish_date': publish_date[i],
            'News_station': news_station[i],
            'News_author': news_author[i],
            'Description': desc[i],
            'Url_to_img': img[i],
            'Content': content[i],
            'Url_to_news': url_to_news[i],
            'Textblob_polarity': textblob_polarity[i],
            'Watson_polarity': watson_polarity[i]

        }
        result = firebase_app.post('/happynews-99c12/', data)
        print(result, " \n")


"""
Gets the content from the database.
@return: void
@para: void
"""


if __name__ == '__main__':
    main()
