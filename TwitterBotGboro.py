import tweepy
import time

API_KEY = "key"
API_SECRET = "secret"
ACCESS_TOKEN = "token"
ACCESS_SECRET = "secret_token"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

askUser = input("Would you like to tweet? 1 for yes, 0 for no ")

if askUser == '1':
    print("Enter Tweet: ")
    x = input()

    api.update_status(x)
    print("You tweeted: " + x)

    # Retweet Mentioned Tweets
mention_id = 1

while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        print(mention.text)
        mention_id = mention.id
        if not mention.retweeted:
            try:
                api.retweet(mention.id)
            except Exception as err:
                print(err)
        else:
            print("Not retweeted")

    time.sleep(15)