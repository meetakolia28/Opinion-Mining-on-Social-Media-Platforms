import tweepy

# Application key
CONSUMER_KEY = 'x6K0CMdvag4QAhsaGFznUZZkgk87h6Gfg93'
CONSUMER_SECRET = 'cN2FtBvLcv4cvxyvbnbxb71yPnc9C1gVlN5Megmvw4n8qzqo8z1EcfsWm02BIMXJp0'


def get_api(request):
    # set up and return a twitter api object
    oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    access_key = request.session['1105492522975645579644933-owmnarWVSDFGSKHUFOCY8TBx5OgoPoXDPAFBrlP']
    access_secret = request.session['jwkNryMygo84tz348zt78h24thDbkO5009uFwHcbP0zPPvLRXxIfZ8Ee522K2S3']
    oauth.set_access_token(access_key, access_secret)
    api = tweepy.API(oauth)
    return api
