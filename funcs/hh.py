from abstract_methods import JobAPI
import requests
import os

class HHJobAPI(JobAPI):
    # HH_API_KEY = os.environ.get('HH_API_KEY')
    # api_kei = HH_API_KEY
    def __init__(self):
        #self.session = requests.Session()
        self.api_url = 'https://api.hh.ru/vacancies'

    # def connect(self, api_key): #получить апикей
    #     self.session.headers.update({'Authorization': f'Bearer {api_key}'})

    def get_vacancies(self, query): #query - ключевое слово поиска #page - position
        response = requests.get(self.api_url, params={'text': query,
                                                      'per_page': 100})
                                                      #'page': page})
        if response.status_code != 200:
            raise ConnectionError(f'Error {response.status_code} {response.text}')
        return response.json()['items']

'''`HHJobAPI` и `SJJobAPI` используют библиотеку `requests` для выполнения HTTP-запросов к API hh.ru и superjob.ru 
соответственно.

Метод `connect` в `HHJobAPI` устанавливает заголовок с авторизационным токеном, который передается в качестве 
аргумента метода `connect`.

Метод `get_vacancies` в `HHJobAPI` вызывает GET-запрос к URL https://api.hh.ru/vacancies с параметром `text`, 
содержащим текст запроса.

Оба метода `get_vacancies` возвращают ответ в формате JSON. Если ответ имеет код статуса отличный от 200, 
мы генерируем исключение типа `ConnectionError`'''

# hh = HHJobAPI()
#
# vacancies = []
# for page in range(10):
#     vacancy = hh.get_vacancies('python', page)
#     vacancies.extend(vacancy)
# print(vacancies)
# print(len(vacancies))

