import tweepy # for tweeting
import secrets # shhhh
from book_manager import BookManager # for getting sentences out of our book file
import requests
import os

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
  #book.delete_message(chunk)
  chunk = 'https://unsplash.it/200/300/?random'
  return chunk

def tweet(message):
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True

  filename = 'temp.jpg'
  s = requests.Session()
  s.trust_env=False
  request = s.get("http://unsplash.it/100?random", stream=True)
  if request.status_code == 200:
    with open(filename, 'wb') as image:
        for chunk in request:
            image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
  else:
    print("Unable to download image")


  #print("Posting message {}".format(message))
  #api.update_status(status=message)

if __name__ == '__main__':
  tweet(get_next_chunk())
