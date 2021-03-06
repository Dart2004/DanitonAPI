import requests
import time
import asyncio

token = ''

#testRequest: wait for request
class testRequest:
  def __init__(self):
    self.text = 'Thinking'

class ChatBot:
  #getAnswer: wait for answer and return it
  def __init__(self, id, name, language):
    self.thinking = False
    self.id = id
    self.name = name
    self.language = language
  def getAnswer(self, message):
    if self.thinking:
      return False
    try:
      x = testRequest()
      self.thinking = True
      while x.text == 'Thinking':
        x = requests.get('https://api.daniton999.ml/chatbot', json = {'token': token, 'id': self.id, 'language': self.language, 'name': self.name, 'message': message}, stream = True)
        time.sleep(3)
      x = x.json()['message']
    except Exception as es:
      print(es)
      x = ''
    self.thinking = False
    return x
    #reset: reset the chatbot
  async def getAsyncAnswer(self, message):
    if self.thinking:
      return False
    try:
      x = testRequest()
      self.thinking = True
      while x.text == 'Thinking':
        x = requests.get('https://api.daniton999.ml/chatbot', json = {'token': token, 'id': self.id, 'language': self.language, 'name': self.name, 'message': message}, stream = True)
        await asyncio.sleep(3)
      x = x.json()['message']
    except Exception as es:
      print(es)
      x = ''
    self.thinking = False
    return x
    #reset: reset the chatbot
  def reset(self):
    requests.patch('https://api.daniton999.ml/chatbot', json = {'token': token, 'id': self.id, 'language': self.language, 'name': self.name})
