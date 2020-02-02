from newsapi.newsapi_client import NewsApiClient
from textblob import TextBlob
import config

key = config.API_KEY
newsapi = NewsApiClient(api_key=key)

# /v2/top-headlines

# /v2/everything


def main(): 
	news_source = ["abc-news",
	"abc-news-au",
	"al-jazeera-english",
	"ars-technica",
	"associated-press",
	"australian-financial-review",
	"axios",
	"bbc-news",
	"bbc-sport",
	"bleacher-report",
	"bloomberg",
	"breitbart-news",
	"business-insider",
	"business-insider-uk",
	"buzzfeed",
	"cbc-news",
	"cbs-news",
	"cnbc",
	"cnn",
	"crypto-coins-news",
	"engadget",
	"entertainment-weekly",
	"espn",
	"espn-cric-info",
	 "financial-post",
	"football-italia",
	"fortune",
	"four-four-two",
	"fox-news",
	"fox-sports",
	"google-news",
	"google-news-au",
	"google-news-ca",
	"google-news-in",
	"google-news-uk",
	"hacker-news",
	"ign",
	"independent",
	"mashable",
	"medical-news-today",
	"msnbc",
	"mtv-news",
	"mtv-news-uk",
	"national-geographic",
	"national-review",
	"nbc-news",
	"news24",
	"new-scientist",
	"news-com-au",
	"newsweek",
	"new-york-magazine",
	"next-big-future",
	"nfl-news",
	"nhl-news",
	"politico",
	"polygon",
	"recode",
	"reddit-r-all",
	"reuters",
	"rte",
	"talksport",
	"techcrunch",
	"techradar",
	"the-american-conservative",
	"the-globe-and-mail",
	"the-hill",
	"the-hindu",
	"the-huffington-post",
	"the-irish-times",
	"wired", 
	"vice-news", 
	"time",
	"the-washington-times", 
	"the-times-of-india", 
	"the-sport-bible",
	"the-next-web", 
	"the-lad-bible",
	"the-jerusalem-post",
	"the-irish-times",
	"the-huffington-post",
	"the-hindu",
	"the-hill"]

	#print (news_source)
	for i in range (len(news_source)): 
		getContent(news_source[i])


def getContent (news_source):
	title = []
	desc=[]
	img=[]
	content =[]
	polarity =[]
	subjectivity =[]
	news =  newsapi.get_everything(sources=news_source,language='en',sort_by='relevancy', page=5)	
	
	articles = news['articles']
	for i in range(len(articles)):
		myarticles = articles[i]
		if (myarticles['content'] != None):
			opinion = TextBlob(myarticles['content'])
			if (opinion.sentiment.polarity > 0.5):
				polarity.append(opinion.sentiment.polarity)
				subjectivity.append(opinion.sentiment.subjectivity)
				content.append(myarticles['content'])
				title.append(myarticles['title'])				
				desc.append(myarticles['description'])
				img.append(myarticles['urlToImage'])
		else: 
			continue

	for i in range(len(title)):
		print ("title: ", title[i], "\n\n")










if __name__ == '__main__': 
	main()