from src.user_interaction import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, \
    print_vacancies


def test_filter_vacancies(vacancies):
    filtered = filter_vacancies(vacancies, ["python"])
    assert len(filtered) == 2
    titles = [v.title for v in filtered]
    assert "Python Dev" in titles
    assert "Senior Python" in titles

    filtered = filter_vacancies(vacancies, ["react"])
    assert len(filtered) == 1
    assert filtered[0].title == "Frontend"

    # Тест с некорректным ключевым словом
    filtered = filter_vacancies(vacancies, ["word"])
    assert filtered == []

def test_get_vacancies_by_salary(vacancies):
    # Валидный диапазон
    filtered = get_vacancies_by_salary(vacancies, "100000-200000")
    assert len(filtered) == 2
    assert {v.title for v in filtered} == {"Python Dev", "Frontend"}

    # Диапазон с пробелами
    filtered = get_vacancies_by_salary(vacancies, " 80000 - 100000 ")
    assert len(filtered) == 2
    assert {v.title for v in filtered} == {"Java Dev", "Frontend"}

    # Некорректный диапазон: все
    filtered = get_vacancies_by_salary(vacancies, "bad-input")
    assert len(filtered) == 4

def test_sort_vacancies(vacancies):
    sorted_list = sort_vacancies(vacancies)
    salaries = [v.salary for v in sorted_list]
    assert salaries == sorted(salaries, reverse=True)
    assert sorted_list[0].title == "Senior Python"

def test_get_top_vacancies(vacancies):
    sorted_list = sort_vacancies(vacancies)
    top2 = get_top_vacancies(sorted_list, 2)
    assert len(top2) == 2
    assert top2[0].salary >= top2[1].salary
    assert top2[0].title == "Senior Python"
    assert top2[1].title == "Python Dev"

def test_print_vacancies(capsys, vacancies):
    print_vacancies(vacancies)
    captured = capsys.readouterr()
    # Проверяем, что все вакансии напечатаны
    for v in vacancies:
        assert v.title in captured.out
        assert str(v.salary) in captured.out