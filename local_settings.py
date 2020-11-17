from os import environ

'''
Local Settings for a rya_ebooks account.
'''

# Configuration for Twitter API
ENABLE_TWITTER_SOURCES = True # Fetch twitter statuses as source
ENABLE_TWITTER_POSTING = True # Tweet resulting status?
MY_CONSUMER_KEY = 'lZ62tI9NIgY3rFjBGzYDzdrii' #Your Twitter API Consumer Key
MY_CONSUMER_SECRET = '0UMQYAzjD8t56eXTRN6LMrMJxkfex1fKGI4gosBFtgnwQ9nKhN' #Your Consumer Secret Key
MY_ACCESS_TOKEN_KEY = '4720135352-eU5Yoq4IfHEAlwYKEFV47pwvQOQgu65YCIMz3MN' #Your Twitter API Access Token Key
MY_ACCESS_TOKEN_SECRET = 'PtyZnD0DDoEB4JanBRqv6xOSrjCFhyic9AHNkCuNUaFB1' #Your Access Token Secret

# Configuration for Mastodon API
ENABLE_MASTODON_SOURCES = False # Fetch mastodon statuses as a source?
ENABLE_MASTODON_POSTING = False # Toot resulting status?
MASTODON_API_BASE_URL = "" # an instance url like https://botsin.space
CLIENT_CRED_FILENAME = '' # the MASTODON client secret file you created for this project
USER_ACCESS_FILENAME = '' # The MASTODON user credential file you created at installation.

# Sources (Twitter, Mastodon, local text file or a web page)
TWITTER_SOURCE_ACCOUNTS = ["@wheredthesodago", "names"]  # A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
MASTODON_SOURCE_ACCOUNTS = [""] # A list, e.g. ["@user@instance.tld"]
SOURCE_EXCLUDE = r'^$'  # Source tweets that match this regexp will not be added to the Markov chain. You might want to filter out inappropriate words for example.
STATIC_TEST = False  # Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = "tweets.txt"  # The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
SCRAPE_URL = False  # Set this to true to scrape a webpage.
SRC_URL = ['http://www.example.com/one', 'https://www.example.com/two']  # A comma-separated list of URLs to scrape
WEB_CONTEXT = ['span', 'h2']  # A comma-separated list of the tag or object to search for in each page above.
WEB_ATTRIBUTES = [{'class': 'example-text'}, {}] # A list of dictionaries containing the attributes for each page.

ODDS = 0  # How often do you want this to run? 1/8 times?
ORDER = 2  # How closely do you want this to hew to sensical? 2 is low and 4 is high.

DEBUG = False  # Set this to False to start Tweeting live
TWEET_ACCOUNT = "account_without_@"  # The name of the account you're tweeting to.

#Configuration for Twitter parser. TEST_SOURCE will be re-used as as the corpus location.
TWITTER_ARCHIVE_NAME = "tweets.csv" #Name of your twitter archive
IGNORE_RETWEETS = True #If you want to remove retweets
