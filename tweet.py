import secrets
import tweepy

def get_api(secrets: dict):
    auth = tweepy.OAuthHandler(
        secrets.consumer_key,
        secrets.consumer_secret
    )
    auth.set_access_token(
        secrets.access_token,
        secrets.access_token_secret
    )

    return tweepy.API(auth)

def send_tweet(api, tweet):
    return api.update_status(status=tweet) 

def main():
    api = get_api(secrets)
    tweet = "Hello world from 🐍"
    status = send_tweet(api, tweet)
    print(status)


if __name__ == "__main__":
    main()
