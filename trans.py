'''
Задача №2 Автотест API Яндекса
Проверим актуальность API Яндекс.Переводчик'а для потенциального сервиса переводов. Используя библиотеку request напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой

Пример положительных тестов:

Код ответа соответствует 200
результат перевода правильный - "привет"
'''



import requests
import json
import os


class Trans:
    '''
            File secret.json required in app dir.
            File format is dict with key "api_key" and value is Yandex API key.
    '''
    def __init__(self):
        self.read_key()

    def read_key(self):

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.keyfile = os.path.join(dir_path,'secret.json')
        with open(self.keyfile, encoding='utf-8') as f:
            self.key = json.load(f).get("api_key", None)

    def trans_text(self, text):
        url = r'https://translate.yandex.net/api/v1.5/tr.json/translate'
        params = {
            "key": self.key,
            "text": text,
            "lang": "en-ru"
        }
        response = requests.get(url=url, params=params)
        return response


if __name__ == '__main__':
    tr = Trans()
    print(tr.trans_text("buy").text)

 #
 # ? key=<API key>
 # & text=<text to translate>
 # & lang=<translation direction>
 # & [format=<text format>]
 # & [options=<translation options>]
 # & [callback=<name of the callback function>]