import argparse
import sys
import secrets
import tweepy
from assets.tweets import tweets
from models.Tweet import Tweet


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
        return api.update_status(status=tweet.status) 
    return api.update_with_media(tweet.media, status=tweet.status)


def main():

    parser = argparse.ArgumentParser(description='Posts tweets to tweeter')
    parser.add_argument(
        '--status',
        '-s',
        help='Text of tweet',
        required=True
    )
    parser.add_argument(
        '--media',
        '-m',
        help='Path to media file'
    )
    args = parser.parse_args()
    status = args.status
    media = args.media

    tweet = Tweet(status, media=media)
    api = get_api(secrets)

    res = send_tweet(api, tweet)
    print(res)


if __name__ == "__main__":
    main()
