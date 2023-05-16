from abstract_methods import JobAPI
import requests
import os

API_KEY = os.environ.get('SUPERJOB_API_KEY')
class SJJobAPI(JobAPI):
    #SUPERJOB_API_KEY = os.environ.get('SUPERJOB_API_KEY')
    def __init__(self):
        self.api_url = 'https://api.superjob.ru/2.0/vacancies/'
        self.api_key = API_KEY

    def get_vacancies(self, query):#query - ключевое слово # page - position
        #response = self.session.get(self.api_url, params={'keyword': query})
        #api_key =  "v3.r.137457996.07015388417e5f7aa57420a11e334e3aaee2ae53.3ad6bac81f2bddf053a21a1416007e3c290b0508"  #os.environ.get('SUPERJOB_API_KEY')
        response = requests.get(self.api_url, params={'keyword': query,
                                                      #'page': page,
                                                      'count': 100}, headers={'X-Api-App-Id': self.api_key})
        if response.status_code != 200:
            raise ConnectionError(f'Error {response.status_code} {response.text}')
        return response.json()['objects']

# sj = SJJobAPI()
# vacancies = []
# for page in range(10):
#     print(page)
#     vacancy = sj.get_vacancies('python', page)
#     vacancies.extend(vacancy)
# print(vacancies)
# print(len(vacancies))



'''`HHJobAPI` и `SJJobAPI` используют библиотеку `requests` для выполнения HTTP-запросов к API hh.ru и superjob.ru 
соответственно.

Метод `connect` в `SJJobAPI` используется заголовок `X-Api-App-Id`, также передаваемый в метод `connect`.

Метод `get_vacancies` в `SJJobAPI` используется URL https://api.superjob.ru/2.0/vacancies/ и параметр `keyword`.

метод`get_vacancies` возвращают ответ в формате JSON. Если ответ имеет код статуса отличный от 200, 
мы генерируем исключение типа `ConnectionError`'''