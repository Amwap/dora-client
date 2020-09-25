import requests
import json

while True:
    question = input(">>")
    # Формируем запрос
    request = f'http://otherwave.ru/dora?&text={question}'
    # Отправляем запрос, получаем json строку
    response = requests.get(request)
    # Парсим json строку, получаем словарь
    json_parse = json.loads(response.content)
    # Берём ответ из словаря
    answer = json_parse['answer']
    # Выводим ответ
    print(answer)