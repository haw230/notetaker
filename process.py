from grammarbot import GrammarBotClient
from rake_nltk import Metric, Rake
from requests.auth import HTTPBasicAuth 
import requests
import nltk

URL = 'https://api.shutterstock.com/v2/images/search'
USER = 'FafRTlvkHlitOlwLwLZL8qQShuIfXNCz'
PWD = '8eWjIjUYl0UGj1xz'

stopwords = ['today', 'learn']

def master_parser(text):
  parsed_text = correct_text(text)
  print(parsed_text)
  return parsed_text

def get_image(text):
  try:
    key_word = extract_key_word(text)
    param = {
      'query': key_word,
      'sort': 'relevance',
      'per_page': 1,
    }
    res = requests.get(URL, params=param, auth=HTTPBasicAuth(USER, PWD)).json()
    print(res['data'][0]['assets']['preview']['url'])
  except IndexError:
    pass

def extract_key_word(text):
  nouns = " ".join([group[0] for group in nltk.tag.pos_tag(text.split()) if group[1] == 'NN' or group[1] == 'NNS'])
  r = Rake(stopwords=stopwords, ranking_metric=Metric.WORD_DEGREE)
  r.extract_keywords_from_text(nouns)
  return(r.get_ranked_phrases()[0])

def correct_text(text):
  client = GrammarBotClient(api_key='KS9C5N3Y')
  res = client.check(text)
  for i in range(len(res.matches)):
    print(res.matches[0].corrections)
    text = res.matches[0].corrections[0]
  if not text[0].isupper():
    text = text[1:]
  return text

if __name__ == '__main__':
  get_image("today we will learn about dogs" )
