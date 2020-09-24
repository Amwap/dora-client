from dora_client import Dora_client

# Инициализируем клиент
client = Dora_client()
# Указываем партнёрский ключ если он имеется
client.key = 'key'
# id последнего сообщения для отправки его при выставлении рейтинга
last_id = None

# Основной цикл
while True:
    # Ввод сообщения
    quest = input(">>")
    # Проверка на введение рейтинга rup=повышение rdown=понижение
    if quest.startswith('rup') or quest.startswith('rdown'):
        # Отправляем запрос, где quest=оператор рейтинга last_id=id последнего сообщения
        response = client.rating(operator=quest, response_id=last_id)

    # Проверка на добавление новой связки
    elif '=' in quest: 
        # Делим сообщение на вопрос и ответ на него
        arg1, arg2 = quest.split('=')
        # Отправляем запрос 
        author = 'From dora client'
        response = client.learn(quest=arg1, answer=arg2, author=author)

    else:    
        # Запрос на получение ответа
        response = client.answer(quest=quest)
        # Сохраняем id последнего сообщения
        last_id = response['response_id']
    
    # Выводим ответ сервера
    print(response)