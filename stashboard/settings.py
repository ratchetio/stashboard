import os

DEBUG = False

SITE_NAME = "Ratchet.io Status"
SITE_AUTHOR = "Cory Virok"
SITE_URL = "http://ratchetstatus.appspot.com"
REPORT_URL = "mailto:help@ratchet.io"

# Twitter update settings
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
TWITTER_HANDLE = 'ratchetio'

# RSS Feed settings
RSS_NUM_EVENTS_TO_FETCH = 50

# OAuth Consumer Credentials
CONSUMER_KEY = 'anonymous'
CONSUMER_SECRET = 'anonymous'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)
