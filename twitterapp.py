import sys
import tweepy

CONSUMER_KEY = 'sgW7RU6cTl6Onca8dcfkQ'
CONSUMER_SECRET = 'Wl0p0EFgg3nHjPlI6VeVHsrPDVsdszMV1mNnYrmNM'
ACCESS_KEY = '54087948-3KE3JkEvmeWa6sARbHyZAAvUN5EuevcaOh1Utz4WV'
ACCESS_SECRET = '5oC3VEca0szYwd3LpIy1EpEoChr55gMgFYdpd7z6pM'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(sys.argv[1])