import pytest

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def temp_json_file(tmp_path):
    # Переопределяем путь файла для тестов
    saver = JSONSaver()
    saver.FILEPATH = tmp_path / "vacancies.json"
    return saver

@pytest.fixture
def vacancies():
    return [
        Vacancy("Python Dev", "url1", 150000, "Опыт Python, Django"),
        Vacancy("Java Dev", "url2", 90000, "Spring, Java"),
        Vacancy("Senior Python", "url3", 250000, "Python, Data Science"),
        Vacancy("Frontend", "url4", 100000, "JavaScript, React"),
    ]