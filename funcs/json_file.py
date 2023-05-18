from abstract_methods import JobFileManager
from vac import Vacancy
import json

'''дочерний класс `JSONJobFileManager`, который наследует поведение абстрактного класса 
и реализует конкретное сохранение вакансий в JSON-файл. '''
class JSONJobFileManager(JobFileManager):
    def __init__(self):
        self.file_path = 'list_vacancies.json'

    '''Метод `add_vacancy` принимает экземпляр класса `Vacancy` 
    и сериализует его атрибуты в формат JSON, записывая их в указанный файл.'''
    def add_vacancy(self, vacancy):
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(vacancy, ensure_ascii=False) + '\n')

    '''Метод `get_vacancies` читает содержимое JSON-файла, десериализует его в экземпляры класса `Vacancy` 
    и возвращает результаты, соответствующие заданным критериям фильтрации.'''
    def get_vacancies(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            vacancies = [Vacancy(json.loads(line)) for line in f.readlines()]
        return vacancies

    '''Метод `delete_vacancies` находит в файле вакансии, соответствующие заданным критериям, и удаляет их'''
    def delete_vacancies(self): #не получается отфильтровать вакансии по заданному ключу,
        # чтобы перезаписывать в файл json только отфильтрованные
        filtered_vacancies = self.get_vacancies()

        with open(self.file_path, 'w', encoding='utf-8') as f:
            for line in f:
                vacancy = Vacancy(json.loads(line))
                if vacancy not in filtered_vacancies:
                    f.write(line)
