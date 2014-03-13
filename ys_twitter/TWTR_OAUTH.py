import twitter

CONSUMER_KEY = 'OhdRwz4IVGqToTVNDtTLw'
CONSUMER_SECRET = '1ySO7qE6noQOu6BDFsEFiGMdMd4VPpBPhJdUt5A'
OAUTH_TOKEN = '147043275-22wVb1KaU1YdpDKFR1mCJXmjCpqKM8t0J5h4szmS'
OAUTH_TOKEN_SECRET = 'fAWzhULBcDHeYByIIDwyH9DddtDj3Rjvp8PDuqMthKtWy'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable
#print(twitter_api)
