from newsapi.newsapi_client import NewsApiClient
from textblob import TextBlob
from firebase import firebase
import config


key = config.API_KEY
newsapi = NewsApiClient(api_key=key)

# /v2/top-headlines

# /v2/everything


def main(): 
	readSourceFile()
	
"""
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
@return : news title, desciption, image link, content, polarity and subjectivity of content
@param: source of the news from where you are extracting the content. eg. 'bbc-news' 

"""
def getContent (news_source):

	title = []
	desc = []
	img = []
	content = []
	polarity = []
	subjectivity = []

	# Call the newsAPI 
	news =  newsapi.get_everything(sources=news_source,language='en',sort_by='relevancy', page=5)	
	articles = news['articles']											# Store the articles returned from the API call.


	for i in range(len(articles)):										# Loop through all the articles. 
		myarticles = articles[i]
		if (myarticles['content'] != None):								# Some articles have no content so need to check that. 
			opinion = TextBlob(myarticles['content'])					# Check the sentiment of the news content. 
			if (opinion.sentiment.polarity > 0.5):
				polarity.append(opinion.sentiment.polarity)
				subjectivity.append(opinion.sentiment.subjectivity)
				content.append(myarticles['content'])
				title.append(myarticles['title'])				
				desc.append(myarticles['description'])
				img.append(myarticles['urlToImage'])
		else: 
			continue
	postContent(title, desc, img, content,polarity, subjectivity)



"""
@return: void 
@para: news title, desciption, image link, content, polarity and subjectivity of content
"""

def postContent(title, desc, img, content,polarity, subjectivity):
	for i in range(len(title)):
		print ("title: ", title[i], "\n\n")










if __name__ == '__main__': 
	main()