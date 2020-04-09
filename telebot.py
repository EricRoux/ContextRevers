"""
Модуль класса Бот. Осуществляет связь между проектом и API телеграмма
"""

import requests
from parser import parse

# TODO: Создание полноценного бота с возможностями получения и отправки сообщений, а так же сохранения переписок в базе данных

# TODO: Функция получения сообщений:    Постоянное обновление сообщений
#                                       Работа на основе offset - номера последнего полученного сообщения, для исключения повторов
#                                       Сохранение сообщений в базу данных

# TODO: Функция оправки сообщение:  Отправка сообщений на основе индентификатора пользователя с возможностью отправки кнопок, и сохранение в БД

# TODO: Функция оправки аудио:  Отправка аудио на основе индентификатора пользователя

# TODO: Функция обработки нажатия кнопки


class Bot:
    # TODO: Добавить подключение к базе данных
    """
    Класс взаимодействия проекта и telegram API
    """
    def __init__(self, token, proxy):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(self.token)
        self.request = requests.Session()
        self.request.proxies = proxy

    # TODO: Реализовать возможность сохранения сообщений в базу данных
    def get_updates(self, new_offset):
        """
        Use this method to receive incoming updates. It returns a json list of Update objects.
        :param new_offset:  Identifier of the first update to be returned.
        :return:            json result
        """
        method = 'getUpdates'
        params = {'offset': new_offset}
        resp = self.request.get(self.api_url + method, data=params)
        return resp.json()['result']

    # TODO: Реализовать возможность сохранения сообщений в базу данных
    def send_messange(self, chat_id, text, reply_markup=None):
        """
        Sending a messange(text) by chat_id

        :param chat_id:  person number id
        :param text:    messange text
        :param reply_markup:        creating buttons
        :return:    answer from Telegram API
        """
        params = {'chat_id': chat_id, 'text': text, 'reply_markup': reply_markup}
        method = 'sendMessage'
        answer = self.request.post(self.api_url + method, params)  # Сервер возвращает ответ на запрос
        return answer

    def get_start(self, message):
        self.send_message(message['chat']['id'], 'Привет')
        self.array_of_countries = search_country(self.url)
        keyboard = dumps({"inline_keyboard":
                              [[{'text': "{}:\t{}".format(i, self.array_of_countries[i][1]), 'callback_data': i}]
                               for i in self.array_of_countries.keys()]})
        self.send_message(message['chat']['id'],
                          'Данный бот выполняет функцию "Receive Free SMS"\n'
                          'Выберите страну, номер которой вы хотите использовать.\n'
                          'Через двоеточие указано количество доступных номеров.',
                          reply_markup=keyboard)

    # TODO: Обработка нажатий и сохранения нажатий в базу данных
    def get_callback_query(self, message):
        keyboard = dumps(
            {"inline_keyboard": [[{'text': '{} - {}'.format(i, self.array_of_phones[i][1]), 'callback_data': i}]
                                 for i in self.array_of_phones.keys()]})
        self.send_message(message['message']['chat']['id'],
                          'Выберите удобный номер телефона - количество сообщений', reply_markup=keyboard)

    def get_none(self, message):
        self.send_message(message['chat']['id'], 'Пожалуйста нажмите /start')
