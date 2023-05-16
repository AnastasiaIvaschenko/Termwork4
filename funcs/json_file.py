''' дочерний класс для сохранения информации о вакансиях,
полученных методами классов HHJobAPI и SJJobAPI  в JSON-файл'''

from abstract_methods import JobFileManager
from vac import Vacancy
import json

class JSONJobFileManager(JobFileManager):
    def __init__(self):
        self.file_path = 'list_vacancies.json'

    def add_vacancy(self, vacancy):
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(vars(vacancy), ensure_ascii=False) + '\n')

    def get_vacancies(self, **filters):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            vacancies = [Vacancy(**json.loads(line)) for line in f.readlines()]

        if not filters:
            return vacancies

        filtered_vacancies = list(filter(lambda v: all(getattr(v, k) == v for k, v in filters.items()), vacancies))
        return filtered_vacancies

    def delete_vacancies(self, **filters):
        filtered_vacancies = self.get_vacancies(**filters)

        with open(self.file_path, 'w', encoding='utf-8') as f:
            for line in f:
                vacancy = Vacancy(**json.loads(line))
                if vacancy not in filtered_vacancies:
                    f.write(line)

'''дочерний класс `JSONJobFileManager`, который наследует поведение абстрактного класса 
и реализует конкретное сохранение вакансий в JSON-файл. 

Метод `add_vacancy` принимает экземпляр класса `Vacancy` 
и сериализует его атрибуты в формат JSON, записывая их в указанный файл. 

Метод `get_vacancies` читает содержимое JSON-файла, десериализует его в экземпляры класса `Vacancy` 
и возвращает результаты, соответствующие заданным критериям фильтрации. 

Метод `delete_vacancies` находит в файле вакансии, соответствующие заданным критериям, и удаляет их'''

# hh = HHJobAPI()
# hh.connect('...') #cюда вставляем апикей
# results = hh.get_vacancies('python')
# vacancies = [Vacancy(**item) for item in results['items']]
#
# file_manager = JSONJobFileManager()
# for vacancy in vacancies:
#     file_manager.add_vacancy(vacancy)
#
# python_vacancies = file_manager.get_vacancies(title='Python Developer')
# print(python_vacancies)
#
# file_manager.delete_vacancies(title='Java Developer')

'''В этом примере мы создаем экземпляр класса `HHJobAPI`, 
устанавливаем соединение с API и получаем список вакансий по запросу "python". 
Создаем экземпляры класса `Vacancy` для всех элементов списка, используя распаковку словаря (`**item`).

Затем мы создаем экземпляр класса `JSONJobFileManager` для работы с файлом `vacancies.json` 
и сохраняем все вакансии в этот файл при помощи метода `add_vacancy`.

Мы затем можем получить все сохраненные вакансии, соответствующие "Python Developer", 
используя метод `get_vacancies`. При помощи метода `delete_vacancies` мы можем удалить все вакансии, 
соответствующие "Java Developer'''