import tweepy # for tweeting
import secrets # shhhh

def retweet():
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True

  searchQuery = 'alice in wonderland'  # this is what we're searching for
  tweetsPerQry = 1  # this is the max the API permits
  #new_tweet = api.search(q=searchQuery, count=tweetsPerQry) #its a list
  for tweet in tweepy.Cursor(api.search,q=searchQuery,result_type="recent",include_entities=True).items(tweetsPerQry):
    print("Posting RT {}".format(tweet.text))
    api.retweet(tweet.id)
  #api.update_status(status=message)

if __name__ == '__main__':
  retweet()
