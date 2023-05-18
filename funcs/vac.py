'''класс для работы с вакансиями, полученными с помощью метода get_vacancies в классах HHJobAPI и SJJobAPI.
В этом классе определить атрибуты, такие как название вакансии, ссылка на вакансию, зарплата, краткое описание
 или требования. Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать
 (то есть делать читаемыми для пользователя) данные, которыми инициализируются его атрибуты'''


class Vacancy:
    '''Класс `Vacancy` определяет атрибуты, которые должны быть доступны в работе с вакансиями,
     полученными с помощью метода `get_vacancies` в классах `HHJobAPI` и `SJJobAPI`.
     В нашем случае в атрибутах включено название вакансии,
     зарплата и краткое описание или требования'''
    def __init__(self, data):
        self.data = data
        self.id = data['id']
        self.name = data['profession'] if 'profession' in data else data['name']

        salary = data.get('salary')
        if salary:
            self.__salary_from = salary.get('from', 0) if isinstance(salary.get('from'), int) else 0
            self.__salary_to = salary.get('to', 0) if isinstance(salary.get('to'), int) else 0
        elif 'salary' not in data:
            self.__salary_from = data.get('payment_from', 0) if isinstance(data.get('from'), int) else 0
            self.__salary_to = data.get('payment_to', 0) if isinstance(data.get('to'), int) else 0
        else:
            self.__salary_from = 0
            self.__salary_to = 0

        url = data.get('url')
        if url:
            self.url = data['url']
        elif 'url' not in data:
            self.url = data.get('client', None)
        else:
            self.url = None

        snip = data.get('snippet')
        if snip:
            self.snippet = snip.get('requirement', None)
        elif 'snippet' not in data:
            self.snippet = data.get('candidat', None)

    @property
    def salary_from(self):  # возвращает нижний уровень зарплаты по конкретной вакансии
        return self.__salary_from

    @property
    def salary_to(self):  # возвращает верхний уровень зарплаты по конкретной вакансии
        return self.__salary_to

    '''Класс также имеет метод `__str__`, который возвращает строковое представление экземпляра класса, 
    использующееся для отображения данного объекта в текстовом виде. 
    В методе используются все определенные атрибуты вакансии.'''
    def __str__(self):
        result = self.name + '\n'
        result += f"Зарплата: {self.salary_from} - {self.salary_to}" + '\n'
        result += f"Краткое описание: {self.snippet}\n"
        result += f"Ссылка: {self.url}\n"
        return result.strip()

    def salary_average(self):
        return (int(self.salary_from) + int(self.salary_to)) / 2

    def __lt__(self, other):
        return self.salary_average() < other.salary_average()

    def __gt__(self, other):
        return self.salary_average() > other.salary_average()

    def __eq__(self, other):
        return self.salary_average() == other.salary_average()

    def __le__(self, other):
        return self.salary_average() <= other.salary_average()

    def __ge__(self, other):
        return self.salary_average() >= other.salary_average()
    '''Класс поддерживает магические методы сравнения `==` и `<` между двумя экземплярами класса, 
    которые сравнивают зарплаты вакансий и опираются на значения salary атрибута. 
    Срабатывают автоматически при последующем
    сравнении экземпляров класса Vacancy по заданному критерию(зарплате) методами sort или max '''
