import tweepy
import time

api_key = "Obi6h2ZSVCUaYqtAK6VlzkaOq"
api_secret = "AzNkihrrsssBvLdfr8WEdxD4jgKGAsFrHjWgVgq0cDtUkDkdUI"
bearer_token = "AAAAAAAAAAAAAAAAAAAAALufngEAAAAAjpoLfgV%2FZOoQYNAxZ81Ag6pkfFc%3D1lTF58AVppiSWcPpj5bi4b7lsBReCTfdv9MiTEUyWdLkLYP3sp"
access_token = "1660297853355573248-rPZCnLP96Fex4ATaIO40qKjE34afaK"
access_token_secret = "wVAIpsg14Poe4Ln0g1xROfHnkubeV2KDQBDW20DeTACbQ"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

##client.create_tweet(text= "Hello @HoneyBunnyxxo")

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        try:
            print(tweet.text)
            client.like(tweet.id)
        except Exception as error:
            print(error)

        time.sleep(30)

stream = MyStream(bearer_token=bearer_token)

stream.add_rules(tweepy.StreamRule("#python -is:retweet -is:reply"), dry_run=True)

stream.filter()