import sys
import tweepy

CONSUMER_KEY = 'sgW7RU6cTl6Onca8dcfkQ'
CONSUMER_SECRET = 'Wl0p0EFgg3nHjPlI6VeVHsrPDVsdszMV1mNnYrmNM'
ACCESS_KEY = '54087948-eY7VuwwQzlOTa4oyhBsAtMbqEf0eKul61pJr4Bs6W'
ACCESS_SECRET = 'IP4EI6kkB6egxzlwFhruSfSI6yMat1Xu2h4x8898Ho'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(sys.argv[1])