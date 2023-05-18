from abstract_methods import JobAPI
import requests
import os

'''`HHJobAPI` и `SJJobAPI` используют библиотеку `requests` для выполнения HTTP-запросов к API hh.ru и superjob.ru 
соответственно.'''

API_KEY = os.environ.get('SUPERJOB_API_KEY')

class SJJobAPI(JobAPI):
    #SUPERJOB_API_KEY = os.environ.get('SUPERJOB_API_KEY')
    def __init__(self):
        self.api_url = 'https://api.superjob.ru/2.0/vacancies/'
        self.api_key = API_KEY

    '''Метод `get_vacancies` в `SJJobAPI` используется URL https://api.superjob.ru/2.0/vacancies/ и параметр `keyword`
    и `заголовок `X-Api-App-Id.'''
    def get_vacancies(self, query):#query - ключевое слово # page - position
        response = requests.get(self.api_url, params={'keyword': query,
                                                      #'page': page,
                                                      'count': 100}, headers={'X-Api-App-Id': self.api_key})
        if response.status_code != 200:
            raise ConnectionError(f'Error {response.status_code} {response.text}')
        return response.json()['objects']

    '''метод`get_vacancies` возвращают ответ в формате JSON. Если ответ имеет код статуса отличный от 200, 
    мы генерируем исключение типа `ConnectionError`'''
