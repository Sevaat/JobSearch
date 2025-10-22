from abc import ABC, abstractmethod
from typing import Any, Dict, List


class Parser(ABC):
    """
    Абстрактный класс поисковика вакансий
    """

    @abstractmethod
    def load_vacancies(
        self, search_query: str, area: int = 113, page_start: int = 0, page_end: int = 0, per_page: int = 20
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
        pass
