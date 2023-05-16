'''класс для работы с вакансиями, полученными с помощью метода get_vacancies в классах HHJobAPI и SJJobAPI.
В этом классе определить атрибуты, такие как название вакансии, ссылка на вакансию, зарплата, краткое описание
 или требования. Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать
 (то есть делать читаемыми для пользователя) данные, которыми инициализируются его атрибуты'''
class Vacancy:
    def __init__(self, data): #, salary_from=None, salary_to=None
        self.data = data
        self.name = self.data['profession'] if 'profession' in self.data else self.data['name']
        self.url = self.data['url'] if 'url' in self.data else self.data['client']['link']
        self.__salary_from = None #self.data['payment_from'] if 'payment_from' in self.data else self.data['salary']['from']
        self.__salary_to = None #self.data['payment_to'] if 'payment_to' in self.data else self.data['salary']['to']
        #self.currency = self.data['currency'] if 'currency' in self.data else self.data['salary']['currency']
        #self.snippet = snippet_validator(data)

    @property
    def salary_from(self):  # возвращает нижний уровень зарплаты по конкретной вакансии
        return self.__salary_from

    @salary_from.setter
    def salary_from(self):  # находит нижний уровень зарплаты по ключам в словарях hh и sj и записывает ее в инициализацию
        if 'payment_from' in self.data:
            self.__salary_from = self.data['payment_from'] if 'payment_from' else ''
        elif 'salary' in self.data:
            self.__salary_from = self.data['salary']['from'] if 'salary' else ''

    @property
    def salary_to(self):  # возвращает верхний уровень зарплаты по конкретной вакансии
        return self.__salary_to

    @salary_to.setter
    def salary_to(self):  # находит верхний уровень зарплаты по ключам в словарях hh и sj и записывает ее в инициализацию
        if 'payment_to' in self.data:
            self.__salary_to = self.data['payment_to'] if 'payment_to' else ''
        elif 'salary' in self.data:
            self.__salary_to = self.data['salary']['to'] if 'salary' else ''

    def __str__(self):
        result = self.name + '\n'
        result += f"Зарплата: {self.__salary_from} - {self.__salary_to}" + '\n'
       #result += f"Краткое описание: {self.snippet}\n" if self.snippet else ""
        result += f"Ссылка: {self.url}\n"
        return result.strip()


    '''Метод `set_salary` устанавливает значения зарплаты на основе информации об этом, который передается в виде словаря.'''

    def set_salary(self, salary_info):
        if "salary" in salary_info:
            salary = salary_info["salary"]  #получаем словарик по ключу 'salary'
            self.salary_from = salary.get("from")
            self.salary_to = salary.get("to")
            self.currency = salary.get("currency")
        elif ("payment_from" in salary_info) and ("payment_to" in salary_info):
            self.salary_from = salary_info["payment_from"]
            self.salary_to = salary_info["payment_to"]
            self.currency = salary_info.get("currency")

    def get_salary(self):
        return {"salary_from": self.salary_from, "salary_to": self.salary_to, "currency": self.currency}

    def compare_salary(self, other_vacancy):
        if not isinstance(other_vacancy, Vacancy):
            raise ValueError("Can't compare salaries with non-Vacancy object")
        if self.salary_to and self.salary_from:
            self_avg = (self.salary_to + self.salary_from) / 2
        elif self.salary_from:
            self_avg = self.salary_from
        else:
            self_avg = self.salary_to
        if other_vacancy.salary_to and other_vacancy.salary_from:
            other_avg = (other_vacancy.salary_to + other_vacancy.salary_from) / 2
        elif other_vacancy.salary_from:
            other_avg = other_vacancy.salary_from
        else:
            other_avg = other_vacancy.salary_to
        if self_avg is None or other_avg is None:
            return None
        return self_avg - other_avg



'''Класс `Vacancy` определяет атрибуты, которые должны быть доступны в работе с вакансиями,
 полученными с помощью метода `get_vacancies` в классах `HHJobAPI` и `SJJobAPI`. 
 В нашем случае в атрибутах включено название вакансии, ссылка на вакансию, 
 зарплата и краткое описание или требования.

Класс также имеет метод `__str__`, который возвращает строковое представление экземпляра класса, 
использующееся для отображения данного объекта в текстовом виде. 
В методе используются все определенные атрибуты вакансии.

Метод `_clean_text` предназначен для удаления HTML-разметки из значений атрибутов класса. 
Этот метод является вспомогательным и используется в конструкторе и других методах класса.

Класс поддерживает методы сравнения `==` и `<` между двумя экземплярами класса, 
которые сравнивают зарплаты вакансий и опираются на значения salay атрибута. 
Если значение salary не задано, оно рассматривается как 0.
'''
# hh = HHJobAPI()
# hh.connect('...')
# results = hh.get_vacancies('python')
# vacancies = [Vacancy(**item) for item in results['items']]
# sorted_vacancies = sorted(vacancies)
# for vacancy in sorted_vacancies:
#     print(vacancy)
'''В этом примере мы создаем экземпляр класса `HHJobAPI`, 
устанавливаем соединение с API и получаем список вакансий по запросу "python". 
Создаем экземпляры класса `Vacancy` для всех элементов списка, используя распаковку словаря (`**item`). 
Затем мы сортируем список вакансий по зарплате и выводим информацию о каждой вакансии на экран.'''