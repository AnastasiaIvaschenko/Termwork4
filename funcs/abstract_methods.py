from abc import ABC, abstractmethod


class JobAPI(ABC):

    @abstractmethod
    def get_vacancies(self, query, page):
        pass

'''В этом коде мы определили абстрактный класс `JobAPI`, который содержит два абстрактных метода: `connect` и `
get_vacancies`. Метод `connect` должен использоваться для установки соединения с API платформы, 
а метод `get_vacancies` для получения вакансий. Конкретные классы `HHJobAPI` и `SJJobAPI` реализуют эти методы
 и наследуются от абстрактного класса `JobAPI`.'''

class JobFileManager(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass
'''Для обобщения операций по сохранению и управлению данными о вакансиях 
был создан абстрактный класс `JobFileManager`, определяющий абстрактные методы
 `add_vacancy`, `get_vacancies` и `delete_vacancies`'''

