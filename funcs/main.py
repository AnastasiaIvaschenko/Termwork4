from hh import HHJobAPI
from superjob import SJJobAPI
from vac import Vacancy
from json_file import JSONJobFileManager

'''функция для взаимодействия с пользователем, 
которая позволяет выбрать платформу, ввести поисковой запрос 
и распечатать список вакансий отсортированных по зарплате, 
а также распечатать вакансии, которые содержат определенные ключевые слова.
1) Получение через API
2) Добавление вакансий в файл.
3) Получаем вакансии из файла -> Список экземпляров Vacancy
4) Манипуляция с данными (while True):

-Вывести как есть
-Отсортировать по зарплате (от мин к макс и обратно)
-Отфильтровать по заданному критерию'''

# user_platforms = input('Введите платформы через запятую (hh.ru, superjob.ru) или нажмите Enter для выбора обоих: ')
# search_text = input('Введите поисковый запрос: ')
# num_of_vacancies = int(input('Введите количество вакансий для вывода: '))
#
# vacancies = []
#
# if user_platforms == 'hh.ru':
#     vacs = HHJobAPI()
# elif user_platforms == 'superjob.ru':
#     vacs = SJJobAPI()
#
# for page in range(int(num_of_vacancies)):
#     vacancy = vacs.get_vacancies(search_text, page)
#     vacancies.extend(vacancy)
#
# print(vacancies)
# print(len(vacancies))

def get_vacancies_from_platforms(platforms, search_text, num_of_vacancies, sorting_order):
    job_apis = [] #список экземпляров классов HHJobAPI() и\или SJJobAPI

    for platform in platforms:
        if platform == 'hh.ru':
            job_apis.append(HHJobAPI())
        elif platform == 'superjob.ru':
            job_apis.append(SJJobAPI())

    vacancies = [] #список словарей с вакансиями по ключевым словам, введенным пользователем

    for job_api in job_apis:
        '''В этой строке кода происходит обращение к методу `get_vacancies`
        каждого экземпляра класса `JobAPI`, который был создан для каждой платформы в списке `platforms`.
        Метод `get_vacancies` возвращает список вакансий с сайта, используя запросы к API или web-скрапинг,
        в зависимости от платформы'''

        vacancies.extend(job_api.get_vacancies(search_text))
        '''`vacancies.extend` - это метод, который расширяет список `vacancies`, 
        добавляя вакансии из каждого экземпляра класса `JobAPI`.'''
    print(vacancies[:num_of_vacancies])

    job_file_manager = JSONJobFileManager(vacancies)
    job_file_manager.add_vacancies(vacancies)
    '''Эта строка кода вызывает метод `add_vacancies`
    объекта класса `JSONJobFileManager`. Метод сохраняет переданный ему список вакансий (`vacancies`)
    в файле JSON для дальнейшей обработки, такой как получение дополнительной информации о вакансиях по их ID.
    Класс `JSONJobFileManager` реализует интерфейс `JobFileManager`, который позволяет сохранять,
    загружать и обновлять вакансии из файла'''
    #
    # for vacancy in top_vacancies:
    #     print(f'Название: {vacancy.name}, Зарплата: {vacancy.salary}, Ссылка: {vacancy.link}')
    #

    formatted_vacancies = []
    for vacancy in vacancies:
        each_vacancy = Vacancy(vacancy)
        formatted_vacancies.append(each_vacancy)
    top_vacancies = formatted_vacancies[:num_of_vacancies]

    print(top_vacancies)


    # if sorting_order == 'asc':
    #     formatted_vacancies = sorted(formatted_vacancies, key=lambda x: x.salary_from)
    # elif sorting_order == 'desc':
    #     formatted_vacancies = sorted(formatted_vacancies, key=lambda x: x.salary_to, reverse=True)
    # print(formatted_vacancies[:num_of_vacancies])
    #
    # top_vacancies = vacancies[:num_of_vacancies]
    #

    # keyword = input('Введите ключевые слова для поиска в описании: ')
    # filtered_vacancies = [vacancy for vacancy in vacancies if keyword.lower() in vacancy.snippet.lower()]
    #
    # if len(filtered_vacancies) > 0:
    #     print(f'\nВакансии, отфильтрованные по ключевым словам ({keyword}):')
    #     for vacancy in filtered_vacancies:
    #         print(f'Название: {vacancy.name}, Зарплата: {vacancy.salary}, Ссылка: {vacancy.link}')
    # else:
    #     print(f'Нет вакансий, соответствующих поиску по ключевым словам ({keyword}).')


def ask_user():
    platforms = input('Введите платформы через запятую (hh.ru, superjob.ru) или нажмите Enter для выбора обоих: ')
    search_text = input('Введите поисковый запрос: ')
    num_of_vacancies = int(input('Введите количество вакансий для вывода: '))
    sorting_order = input('Выберите порядок сортировки зарплаты (asc - по возрастанию, desc - по убыванию): ')

    if platforms == '':
        platforms = ['hh.ru', 'superjob.ru']
    else:
        platforms = [platform.strip() for platform in platforms.split(',')]

    get_vacancies_from_platforms(platforms, search_text, num_of_vacancies, sorting_order)


if __name__ == '__main__':
    ask_user()

'''Функция `get_vacancies_from_platforms` создает экземпляры `HHJobAPI` и `SJJobAPI` в зависимости от того, 
какие платформы были выбраны пользователем, и использует их для получения списка вакансий. 
Затем сортирует вакансии в соответствии с выбранным порядком сортировки (по возрастанию или по убыванию зарплаты), 
выбирает топ N вакансий и выводит их в консоль. 
Затем запрашивает ключевые слова от пользователя для процесса фильтрации вакансий по ним, 
выводит результаты в консоль'''


