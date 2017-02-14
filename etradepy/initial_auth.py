#!/usr/bin/env python

import logging
import requests_oauthlib
import settings

from requests_oauthlib import OAuth1Session


logging.basicConfig(level=logging.DEBUG)

client_key=settings.oauth_consumer_key
client_secret=settings.consumer_secret

request_token_url = 'https://etws.etrade.com/oauth/request_token'
oauth = OAuth1Session(client_key, client_secret, callback_uri='oob')
fetch_response = oauth.fetch_request_token(request_token_url)
print('Successfully fetched a request token.')

print('Now go here in the browser, and go through the authorization steps:')
print('https://us.etrade.com/e/t/etws/authorize?key={oauth_consumer_key}&token={oauth_token}'.format(oauth_consumer_key='7ec3723ba365d76b8bb0728d89628f3a', oauth_token=fetch_response['oauth_token']))
verifier = input('Enter the verifier code here: ').strip()

access_token_url = 'https://etws.etrade.com/oauth/access_token'
oauth = OAuth1Session(
    client_key,
    client_secret,
    resource_owner_key=fetch_response['oauth_token'],
    resource_owner_secret=fetch_response['oauth_token_secret'],
    verifier=verifier
)
oauth_tokens = oauth.fetch_access_token(access_token_url)
print('Successfully fetched access tokens! These should be valid until midnight ET.')
print('Save them wherever you need to-- but they will be pickled in user_tokens.p.')
print(oauth_tokens)
print('Retrieve with `pickle.load(open('user_tokens.p', 'rb'))`')
pickle.dump(tokens, open('user_tokens.p', 'wb'))
