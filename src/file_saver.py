from abc import ABC, abstractmethod
from typing import List
from src.vacancy import Vacancy

class Saver(ABC):
    @abstractmethod
    def get_vacancies(self, **criteria) -> List[Vacancy]:
        """
        Получить отфильтрованные данные вакансий
        :param criteria: критерии фильтрации вакансий
        :return: список вакансий
        """
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавить данные вакансии в файл
        :param vacancy: данные вакансии
        :return: None
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удалить данные вакансии из файла
        :param vacancy: данные вакансии
        :return: None
        """
        pass