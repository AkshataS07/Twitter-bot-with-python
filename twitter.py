import tweepy

api_key = "oBouZBFt8azTutPBVEgz9zQq3"
api_secret = "0X4zoAQoS8Af7LjfJ2PXeaLlsFAUbXRh9uQoYmncnXnxhaAAJO"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAJYvrgEAAAAAXGmjzq73MCH3dRkGEXgib19uAsM%3DjRMNzLraa6KjkMjIfWF8fzeYQ4pfGaWwolz5fjF2U5eWhDOzhK"
access_token = "1500494651681239045-4O8YcJ9Mkxg4ChH5HggefqUpDvvXR7"
access_token_secret = "FibzAi2a2TlxZ6KeGeQxzOoV5Y5Ei9CY1iiK7eTmzjMKV"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#client.create_tweet(text = "Hello World")
#client.like("1737073451377238022")

# client.retweet("1613078224539615233")

# client.create_tweet(in_reply_to_tweet_id="1613078224539615233", text = "Keep learning Simplilearners")

# for tweet in api.home_timeline():
#     print(tweet.text)

# person = client.get_user(username = "narendramodi").data.id

# for tweet in client.get_users_tweets(person).data:
#     print(tweet.text)


