import requests
import json


class Dora_client():
    def __init__(self):
        self.key = 'Your partner key' # Партнёрский ключ
        self.service = 'http://otherwave.ru/dora' # Куда уходит запрос
        

    def answer(self, quest):
    # Формирует get запрос к базе данных
    # Возвращает json dict
        form = f'?&text={quest}&key={self.key}'
        return self._request(form)

    def learn(self, quest, answer, author):
    # Формирует get запрос на обучение 
    # Работает при указании key
        form = f'?&quest={quest}&answer={answer}&author={author}&key={self.key}'
        return self._request(form)

    def rating(self, operator, response_id): 
    # Формирует get запрос на проставление рейтинга
    # Работает при указании key
        form = f'?&operator={operator}&response_id={response_id}&key={self.key}'
        return self._request(form)

    def _request(self, form):
    # Отправляет запрос на сервер
    # В возвращает ответ сервера формата json
        response = requests.get(self.service + form)
        return json.loads(response.content)