import requests
import json


class Dora_client():
    def __init__(self):
        self.key = 'Your partner key'
        self.service = 'http://otherwave.ru/dora'

    def answer(self, quest):
        form = f'?&text={quest}&key={self.key}'
        response = requests.get(self.service + form)
        answer = json.loads(response.content)
        return answer

    def learn(self, quest, answer, author):
        form = f'?&quest={quest}&answer={answer}&author={author}&key={self.key}'
        response = requests.get(self.service + form)
        answer = json.loads(response.content)
        return answer

    def rating(self, operator, response_id):
        form = f'?&operator={operator}&response_id={response_id}&key={self.key}'
        response = requests.get(self.service + form)
        answer = json.loads(response.content)
        return answer
    
client = Dora_client()

last_id = None
while True:
    quest = input(">>")
    op = quest.split()
    try: arg1, arg2 = quest.split('=')
    except: pass

    if quest.startswith('rup') or quest.startswith('rdown'):
        response = client.rating(op[0], last_id)

    elif '=' in quest: 
        response = client.learn(arg1, arg2, 'From dora client')

    else:    
        response = client.answer(quest)
        last_id = response['response_id']

    print(response)