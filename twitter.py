#!/usr/bin/env python

import tweepy

CONSUMER_KEY = 'sgW7RU6cTl6Onca8dcfkQ'
CONSUMER_SECRET = 'Wl0p0EFgg3nHjPlI6VeVHsrPDVsdszMV1mNnYrmNM'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret