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
def readSourceFile (): 
	source_file = open("sources.txt", "r")		# Read the file containing the news sources.
	sources = source_file.readlines()			# Read line by line.
	source_file.close()							# Close. 

	for i in range (len(sources)):				# call the getContent function one by one with the news source as parameter.
		print(sources[i]) 
		getContent(sources[i])



"""
Calls the newsAPI to get the content and stores the different information associated 
with the news articles. 
@return : news title, desciption, image link, content, polarity and subjectivity of content
@param: source of the news from where you are extracting the content. eg. 'bbc-news' 
"""
def getContent (news_source):

	title = []
	desc = []
	img = []
	content = []
	polarity = []
	# Call the newsAPI 
	news =  newsapi.get_everything(sources=news_source,language='en',sort_by='relevancy', page=5)	
	articles = news['articles']											# Store the articles returned from the API call.

	authenticator = IAMAuthenticator(config.IBM_API_KEY)
	watson_nlu = NaturalLanguageUnderstandingV1(version='2019-07-12',authenticator=authenticator)
	watson_nlu.set_service_url(config.IBM_URL)



	for i in range(len(articles)):										# Loop through all the articles. 
		myarticles = articles[i]
		if (myarticles['content'] != None):								# Some articles have no content so need to check that. 
			textblob_polarity = TextBlob(myarticles['content']).sentiment.polarity			# Check the sentiment of the news content. 
			watson_sentiment = watson_nlu.analyze( text = myarticles['content'], features = {"sentiment": {}})
			watson_polarity = watson_sentiment.result['sentiment']['document']['score']

			if (textblob_polarity > 0 and watson_polarity > 0):
				polarity.append(textblob_polarity)
				content.append(myarticles['content'])
				title.append(myarticles['title'])				
				desc.append(myarticles['description'])
				img.append(myarticles['urlToImage'])

		else: 
			continue
	postContent(title, desc, img, content,polarity)



"""
Uploads the content of the news to the database. 
@return: void 
@para: news title, desciption, image link, content, polarity and subjectivity of content
"""
def postContent(title, desc, img, content, polarity):
	for i in range(len(title)): 
		print (i , "  ", title[i], "\n")
		
   

if __name__ == '__main__': 
	main()











