import pytest

from src.json_saver import JSONSaver


@pytest.fixture
def temp_json_file(tmp_path):
    # Переопределяем путь файла для тестов
    saver = JSONSaver()
    saver.FILEPATH = tmp_path / "vacancies.json"
    return saver