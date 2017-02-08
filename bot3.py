import tweepy # for tweeting
import secrets # shhhh
from book_manager import BookManager # for getting sentences out of our book file
import requests
import json

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
  #chunk = 'https://unsplash.it/200/300/?random'
  return chunk

def tweet(message):
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True

  poke_data = requests.get('http://pokeapi.co/api/v2/pokemon/1/', headers={'Accept-Encoding':'none'})
  poke_json = poke_data.json
  print("{}".format(poke_json))
  #poke_json = json.loads(js.decode("utf-8"))
  message = poke_json['name'] + message


  print("Posting message {}".format(message))
  api.update_status(status=message)

if __name__ == '__main__':
  tweet(get_next_chunk())
