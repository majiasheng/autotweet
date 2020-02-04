import argparse
import sys
import secrets
import tweepy
from assets.tweets import tweets


parser = argparse.ArgumentParser(description='Posts tweets to tweeter')

parser.add_argument(
    '--status',
    '-s',
    dest='accumulate', 
    action='store_const',
    help='Text of tweet'
)
parser.add_argument(
    '--media',
    '-m',
    action='store_const',
    help='Path to media file'
)

def get_api(secrets: dict) -> tweepy.API:
    auth = tweepy.OAuthHandler(
        secrets.consumer_key,
        secrets.consumer_secret
    )
    auth.set_access_token(
        secrets.access_token,
        secrets.access_token_secret
    )

    return tweepy.API(auth)


def send_tweet(api: tweepy.API, tweet: str, path_to_media: str = None) -> tweepy.Status:
    if tweet.media is None:
        return api.update_status(status=tweet.text) 
    return api.update_with_media(tweet.media, status=tweet.text)


def main():
    # api = get_api(secrets)
    
    
    # tweet = tweets[0]
    for a in sys.argv:
        print(a)

    # status = send_tweet(api, tweet)
    # print(status)


if __name__ == "__main__":
    main()
