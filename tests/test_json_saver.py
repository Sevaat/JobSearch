import json

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def test_add_vacancy(temp_json_file):
    v = Vacancy("text", "url", 1, "description")
    temp_json_file.add_vacancy(v)
    with open(temp_json_file.FILEPATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]['title'] == "text"
    assert data[0]['url'] == "url"
    assert data[0]['salary'] == 1
    assert data[0]['description'] == "description"

def test_get_vacancies_filter_keyword_and_salary(temp_json_file):
    v1 = Vacancy("Test1", "url1", 50000, "Python developer")
    v2 = Vacancy("Test2", "url2", 150000, "Senior Python")
    v3 = Vacancy("Test3", "url3", 200000, "Java developer")
    temp_json_file._write([v1.to_dict(), v2.to_dict(), v3.to_dict()])

    # По ключевому слову Python и минимальной зарплате
    result = temp_json_file.get_vacancies(keyword="Python", salary_min=100000)
    assert len(result) == 1
    assert result[0].title == "Test2"

    # По максимальной зарплате
    result = temp_json_file.get_vacancies(salary_max=100000)
    assert len(result) == 1
    assert result[0].title == "Test1"

def test_delete_vacancy(temp_json_file):
    v1 = Vacancy("Test1", "url1", 50000, "desc")
    v2 = Vacancy("Test2", "url2", 150000, "desc2")
    temp_json_file._write([v1.to_dict(), v2.to_dict()])

    temp_json_file.delete_vacancy(v1)
    with open(temp_json_file.FILEPATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]['url'] == "url2"

def test_read_returns_empty_on_missing_file(tmp_path):
    saver = JSONSaver()
    saver.FILEPATH = tmp_path / "missing.json"
    assert saver._read() == []

def test_write_and_read(temp_json_file):
    vacancies = [
        Vacancy("A", "u1", 1000, "d1").to_dict(),
        Vacancy("B", "u2", 2000, "d2").to_dict()
    ]
    temp_json_file._write(vacancies)
    read_vacancies = temp_json_file._read()
    assert read_vacancies == vacancies