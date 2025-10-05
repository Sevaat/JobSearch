import json
import os
from pathlib import Path
from typing import List
from src.file_saver import Saver
from src.vacancy import Vacancy

class JSONSaver(Saver):
    FILEPATH = Path(__file__).resolve().parent.parent / "data"
    os.makedirs(FILEPATH, exist_ok=True)
    FILEPATH = f"{FILEPATH}/vacancies.json"

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавить данные вакансии в файл
        :param vacancy: данные вакансии
        :return: None
        """
        vacancies = self._read()
        vacancies.append(vacancy.to_dict())
        self._write(vacancies)

    def get_vacancies(self, **criteria) -> List[Vacancy]:
        """
        Получить отфильтрованные данные вакансий
        :param criteria: критерии фильтрации вакансий
        :return: список вакансий
        """
        vacancies = self._read()
        result = []
        for v in vacancies:
            match = True
            for k, val in criteria.items():
                if k == 'keyword':
                    if val.lower() not in v['description'].lower():
                        match = False
                elif k == 'salary_min':
                    if v['salary'] < val:
                        match = False
                elif k == 'salary_max':
                    if v['salary'] > val:
                        match = False
            if match:
                result.append(Vacancy(**v))
        return result

    def delete_vacancy(self, vacancy: Vacancy):
        """
        Удалить данные вакансии из файла
        :param vacancy: данные вакансии
        :return: None
        """
        vacancies = self._read()
        vacancies = [v for v in vacancies if v['url'] != vacancy.url]
        self._write(vacancies)

    def _read(self) -> list:
        """
        Получить данные вакансий из JSON-файла
        :return: словарь вакансий
        """
        try:
            with open(self.FILEPATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f'Ошибка: {e}')
            return []

    def _write(self, vacancies: list) -> None:
        """
        Записать данные вакансии в JSON-файл
        :param vacancies: данные вакансии
        :return: None
        """
        try:
            with open(self.FILEPATH, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f'Ошибка: {e}')