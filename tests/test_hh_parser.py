import pytest
from unittest.mock import patch, MagicMock
from src.hh_parser import HeadHunterParser


def test_load_vacancies_requests_called():
    parser = HeadHunterParser()
    with patch("src.hh_parser.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"items": [{"id": 1}]}
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        result = parser.load_vacancies("Python", page_start=0, page_end=2, per_page=1)
        assert mock_get.call_count == 2
        assert isinstance(result, list)
        assert result == [{"id": 1}, {"id": 1}]

def test_load_vacancies_empty_response():
    parser = HeadHunterParser()
    with patch("src.hh_parser.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"items": []}
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        result = parser.load_vacancies("Python", page_start=0, page_end=1)
        assert result == []

def test_load_vacancies_raises_for_status():
    parser = HeadHunterParser()
    with patch("src.hh_parser.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.raise_for_status.side_effect = Exception("HTTP error")
        mock_get.return_value = mock_resp

        with pytest.raises(Exception):
            parser.load_vacancies("Python", page_start=0, page_end=1)
