from typing import Union, Self


class Vacancy:
    """
    Класс содержащий данные вакансии
    """
    __slots__ = ['title', 'url', 'salary', 'description']

    def __init__(self, title: str, url: str, salary: int | float | None, description: str):
        self.title = title
        self.url = url
        self.salary = self._validate_salary(salary)
        self.description = description

    @staticmethod
    def _validate_salary(salary) -> int | float:
        """
        Проверять значение заработной платы (должно быть числом или отсутствовать)
        :param salary: значение заработной платы
        :return:
        """
        if salary is None:
            return 0
        if not isinstance(salary, Union[int, float]):
            raise ValueError("Значение заработной платы должно быть числом или отсутствовать (None)")
        return salary

    def __lt__(self, other) -> bool:
        """
        Сравнить "<" вакансии по заработной плате
        :param other: вторая вакансия
        :return: если ЗП первой вакансии меньше ЗП второй вакансии, то True, иначе - False
        """
        return self.salary < other.salary

    def __eq__(self, other) -> bool:
        """
        Сравнить "=" вакансии по заработной плате
        :param other: вторая вакансия
        :return: если ЗП первой вакансии равна ЗП второй вакансии, то True, иначе False
        """
        return self.salary == other.salary

    @classmethod
    def cast_to_object_list(cls, vacancies_json) -> list:
        """
        Перевести описание вакансии из JSON в список
        :param vacancies_json: описание вакансии в JSON
        :return: описание вакансии в виде списка
        """
        result = []
        for v in vacancies_json:
            salary = None
            if v.get('salary') and v['salary'].get('from'):
                salary = v['salary']['from']
            result.append(cls(
                v.get('name'),
                v.get('alternate_url'),
                salary,
                v.get('snippet', {}).get('requirement', '') or v.get('snippet', {}).get('responsibility', '')
            ))
        return result

    def to_dict(self) -> dict:
        """
        Перевести описание вакансии в словарь
        :return: описание вакансии в виде словаря
        """
        return {
            'title': self.title,
            'url': self.url,
            'salary': self.salary,
            'description': self.description
        }

    def __repr__(self) -> str:
        """
        Преобразовать данные о вакансии в строку
        :return: строка с данными о вакансии
        """
        return f"{self.title} ({self.salary}): {self.url}\n{self.description}\n"