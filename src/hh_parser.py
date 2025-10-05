from typing import Any, Dict, List

import requests

from src.parser import Parser


class HeadHunterParser(Parser):
    """
    Класс поисковика вакансий на HH
    """

    BASE_URL = "https://api.hh.ru/vacancies"

    def load_vacancies(
        self, search_query: str, area: int = 113, page_start: int = 0, page_end: int = 20, per_page: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Получить список вакансий по запросу
        :param search_query: содержание поискового запроса
        :param area: № региона, где производится поиск (113 - Россия)
        :param page_start: № первой страницы для просмотра
        :param page_end: № последней страницы для просмотра
        :param per_page: количество элементов (вакансий) на одной странице
        :return: данные вакансий
        """
        params = {"text": search_query, "area": area, "page": page_start, "per_page": per_page}

        vacancies = []

        while params["page"] != page_end:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            vacancies_on_page = response.json()["items"]
            vacancies.extend(vacancies_on_page)
            params["page"] += 1

        return vacancies
