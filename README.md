# HappyNews
Contrary to the regular news website, HappyNews will display only contents that are positive. 
Happynews scraps news from all the news sources provided by <a href="https://newsapi.org/"> NewsAPI.org</a> and then uses <b> TextBlob library </b> and <b> IBM Watson Natural Language Understanding</b> to check the polarity of the content. The news content will be displayed if the two libraries detect a high positive polarity. Although the goal of this project is to allow people to read all the news on this website, this is not possible since the developer version (free) of NewsAPI only returns 250 characters of the content.