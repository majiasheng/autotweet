# what is this?
A tool to post tweets to twitter

## how to set up?
1. Go to your twitter account (or skip to 5 if you've already set up phone number)
2. On the right of the home page, click on `more`
3. Go to `Settings and privacy`
4. Set up your phone number
5. Go to https://developer.twitter.com/en/apps
6. Click on `Create an app` and fill in required fields
7. Once you have your app approved, go to `Keys and tokens`
8. Generate Access token & access token secret, and make sure access level is `Read and write`
9. Copy `access token secret` to as `access_token_secret`, `API key` as `consumer_key`, `API secret key` as `consumer_secret`, and `Access token` as `access_token` to `__secrets.py` file
10. Rename `__secrets.py` to `secrets.py`


## how to run
`python3 tweet.py` -s STATUS -m PATH_TO_MEDIA_FILE

 
