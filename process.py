from grammarbot import GrammarBotClient
from rake_nltk import Metric, Rake
from requests.auth import HTTPBasicAuth
from random import randrange
import requests
import nltk

URL = 'https://api.shutterstock.com/v2/images/search'
USER = 'FafRTlvkHlitOlwLwLZL8qQShuIfXNCz'
PWD = '8eWjIjUYl0UGj1xz'

stopwords = ['today', 'learn']

def master_parser(text):
  if not (text.startswith('and') or text.startswith('or')):
    text = text.capitalize()
  return text

def get_image(text):
  try:
    key_word = extract_key_word(text)
    param = {
      'query': key_word,
      'sort': 'relevance',
      'per_page': 1,
    }
    res = requests.get(URL, params=param, auth=HTTPBasicAuth(USER, PWD)).json()
    index = randrange(10) if len(res['data']) > 9 else 0
    image_url = res['data'][index]['assets']['preview']['url']
    return str(image_url)
  except IndexError:
    pass

def extract_key_word(text):
  nouns = " ".join([group[0] for group in nltk.tag.pos_tag(text.split()) if group[1] == 'NN' or group[1] == 'NNS'])
  r = Rake(stopwords=stopwords, ranking_metric=Metric.WORD_DEGREE)
  r.extract_keywords_from_text(nouns)
  phrases = r.get_ranked_phrases()
  return phrases[0] if phrases else "puppy"

def correct_text(text):
  client = GrammarBotClient(api_key='KS9C5N3Y')
  res = client.check(text)
  for match in res.matches:
    if(match.category != 'TYPOS'):
      print(match.corrections)
      text = match.corrections[0]
  if not text[0].isupper():
    text = text[1:]
  return text

if __name__ == '__main__':
  get_image("today we will learn about dogs" )
