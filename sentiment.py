import matplotlib.pyplot as plt
# mpl plotting lib for creating interactive virtsualization in python
#pyplot: sub-modeule, that creates vaious plots like histogram,piechart,graphs
import tweepy
# Tweepy is an open-sourced  for accessing the Twitter API.
# twitter allows us to mine data from twitter API
from textblob import TextBlob
#python lib which offers simple api to process textual data and perform basic NLP tasks
#built ipon NLTK(a toolkit built to work on NLP in python:text processing lib)
#1.data processing 2.tokenization 3.stopwords removal 4.lemmitization and stemming 5.categorizing
def percentage(portion,whole):
    return 100* float(portion)/float(whole)

# authorization tokens
api_key = "..."
api_key_secret = "..."
access_token = "..."
access_token_secret = "..."

#auth failed if key is wrong/search term
try:
      # OAuth :OAuth is an open-standard authorization protocol or framework that provides
      # applications the ability for “secure designated access.”
      # OAuth doesn’t share password data but instead uses authorization tokens to prove an
      # identity between consumers and service providers.
    # authorization to API key
    auth_handler = tweepy.OAuthHandler(consumer_key=api_key,consumer_secret=api_key_secret)
    # .set_access gives the access to the access token and access secret
    auth_handler.set_access_token(access_token,access_token_secret)
    # calling the API
    api=tweepy.API(auth_handler)
    search_term = input("enter the keyword you want to search about:")
    search_term = str(search_term)
    tweet_amount = input("enter number of tweets you want to analyze:")
    tweet_amount = int(tweet_amount)
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
      # json is used for serialising and transmiting  structured data over a network.
    results = [status._json for status in
               tweepy.Cursor(api.search_tweets, q=search_term, tweet_mode='extended', lang='en').items(tweet_amount)]
    # tweepy provides the conveninet cursor interface to iterate through different types of objects
    # Now you can iterate over 'results' and store the complete message from each tweet.
    my_tweets = [] #creating a empty list
    for result in results:
        my_tweets.append(result["full_text"]) #adding the tweet
    #print(my_tweets)

    for tweet in my_tweets: #traversing one tweet at a time
        print(tweet)
        analysis = TextBlob(tweet)
        #analysing the polarity which can be between [-1,1]
        if analysis.sentiment.polarity == 0: # analysing the polarity which can be [-1,1]
            neutral += 1
        elif analysis.sentiment.polarity > 0.00:
            positive += 1
        if analysis.sentiment.polarity < 0.00:
            negative += 1
    positive = percentage(positive, tweet_amount)
    negative = percentage(negative, tweet_amount)
    neutral = percentage(neutral, tweet_amount)
    print(analysis.sentiment)
    positive = round(positive, 2)
    negative = round(negative, 2)
    neutral = round(neutral, 2)

    if positive > negative and positive > neutral:
        print("POSITIVE")
    elif neutral > positive and neutral > negative:
        print("NEUTRAL")
    elif polarity < 0:
        print("NEGATIVE")
    lables = ['Positive[' + str(positive) + '%]', 'Neutral[' + str(neutral) + '%]', 'Negative[' + str(negative) + '%]']
    sizes = [positive, neutral, negative]
    colors = ['blue', 'yellow', 'brown']
    label = ["POSITIVE", "NEUTRAL", "NEGATIVE"]
    
    # The statement, startangle=90, makes the plotting right at the top middle of the pie chart.
    # The first elements are then plotted and the next sequential elements are plotted in a counterclockwise direction.
    # for includeing percentages inside the pie chart
    
    plt.pie(sizes, labels=label, colors=colors,startangle=90, autopct='%1.1f%%')
    
    # autopct it is used to show the percentage inside the piechart
    # for including title bar
    
    plt.legend(lables, loc='upper left') 
    
    # used to create the text bar
    
    plt.title("SENTIMENT ANALYSIS ON " + search_term)
    plt.show()

except:
    print("Authentication failed!")