from typing import List

from src.hh_parser import HeadHunterParser
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    """
    Фильтровать вакансии
    :param vacancies: список вакансий
    :param keywords: ключевые слова для фильтрации в описании вакансии
    :return: список отфильтрованных вакансий
    """
    return [v for v in vacancies if any(word.lower() in v.description.lower() for word in keywords)]


def get_vacancies_by_salary(vacancies: List[Vacancy], salary_range: str) -> List[Vacancy]:
    """
    Отфильтровать вакансии по величине зарплаты
    :param vacancies: список вакансий
    :param salary_range: диапазон зарплаты 'MIN-MAX'
    :return: список отфильтрованных вакансий
    """
    try:
        min_salary, max_salary = map(int, salary_range.replace(" ", "").split("-"))
    except Exception as e:
        print(f"Ошибка: {e}")
        min_salary, max_salary = 0, float("inf")
    return [v for v in vacancies if min_salary <= v.salary <= max_salary]


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """
    Сортировка вакансий по убыванию
    :param vacancies: список вакансий
    :return: отсортированный по убыванию список вакансий
    """
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    """
    Вывести n лучших вакансий
    :param vacancies: список вакансий
    :param n: число вакансий для вывода
    :return: список лучших вакансий длинной n
    """
    return vacancies[:n]


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """
    Вывести на экран список вакансий
    :param vacancies: список вакансий
    :return: None
    """
    for v in vacancies:
        print(v)


def user_interaction() -> None:
    """
    Пользовательский интерфейс
    :return:
    """
    hh_api = HeadHunterParser()
    json_saver = JSONSaver()

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий (через пробел): ").split()
    salary_range = input("Введите диапазон зарплат (например: 100000-150000): ")

    raw_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(raw_vacancies)

    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
