import tweepy # for tweeting
import secrets # shhhh
from book_manager import BookManager # for getting sentences out of our book file
import random

def get_next_chunk():
  # open text file
  book = BookManager()
  first_sentence = book.first_sentence()
  # tweet the whole sentence if it's short enough
  if len(first_sentence) <= 140:
    chunk = first_sentence
  # otherwise just print the first 140 characters
  else:
    chunk = first_sentence[0:140]

  # delete what we just tweeted from the text file
  book.delete_message(chunk)
  #chunk = 'https://unsplash.it/200/300/?random'
  return chunk

def tweet(message):
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True

  print("Posting message {}".format(message))
  api.update_status(status=message)

def retweet():
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True
  try:
    searchQuery = 'alice in wonderland'  # this is what we're searching for
    tweetsPerQry = 1  # this is the max the API permits
    #new_tweet = api.search(q=searchQuery, count=tweetsPerQry) #its a list
    for tweet in tweepy.Cursor(api.search,q=searchQuery,result_type="recent",include_entities=True).items(tweetsPerQry):
      print("Posting RT {}".format(tweet.text))
      api.retweet(tweet.id)
  except tweepy.TweepError as e:
    print("TweepError. Posting a message from the book...")
    tweet(get_next_chunk())

if __name__ == '__main__':
  if random.randint(0,1) == 0:
    tweet(get_next_chunk())
  else:
    retweet()
