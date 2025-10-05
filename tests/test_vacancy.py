import pytest

from src.vacancy import Vacancy


def test_vacancy_creation_with_valid_salary():
    v = Vacancy("Python", "url", 1, "description")
    assert v.title == "Python"
    assert v.url == "url"
    assert v.salary == 1
    assert v.description == "description"

def test_vacancy_creation_with_none_salary():
    v = Vacancy("Python", "url", None, "description")
    assert v.salary == 0

def test_vacancy_creation_with_float_salary():
    v = Vacancy("Python", "url", 1.0, "description")
    assert v.salary == 1.0

def test_vacancy_creation_with_invalid_salary_type():
    with pytest.raises(ValueError):
        Vacancy("Python", "url", "salary", "description")

def test_vacancy_comparison_lt_eq():
    v1 = Vacancy("vac1", "url1", 1, "description")
    v2 = Vacancy("vac2", "url2", 1.5, "description")
    v3 = Vacancy("vac3", "url3", 1, "description")
    assert v1 < v2
    assert not v2 < v1
    assert v1 == v3
    assert not v1 == v2

def test_vacancy_to_dict():
    v = Vacancy("vac", "url", 1, "description")
    d = v.to_dict()
    assert isinstance(d, dict)
    assert d['title'] == "vac"
    assert d['url'] == "url"
    assert d['salary'] == 1
    assert d['description'] == "description"

def test_vacancy_repr():
    v = Vacancy("vac", "url", 1, "description")
    r = repr(v)
    assert "vac" in r
    assert "1" in r
    assert "url" in r
    assert "description" in r

def test_cast_to_object_list_parsing():
    sample_json = [
        {
            "name": "Python1",
            "alternate_url": "url1",
            "salary": {"from": 1},
            "snippet": {"requirement": "requirement", "responsibility": ""}
        },
        {
            "name": "Python2",
            "alternate_url": "url2",
            "salary": None,
            "snippet": {"requirement": "", "responsibility": "responsibility"}
        }
    ]
    vacancies = Vacancy.cast_to_object_list(sample_json)
    assert len(vacancies) == 2
    assert vacancies[0].title == "Python1"
    assert vacancies[0].salary == 1
    assert vacancies[0].description == "requirement"
    assert vacancies[1].title == "Python2"
    assert vacancies[1].salary == 0
    assert vacancies[1].description == "responsibility"