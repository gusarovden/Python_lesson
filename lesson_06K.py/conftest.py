import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "form_test: Тест на заполнение формы"
    )
    config.addinivalue_line(
        "markers",
        "сalc_test: Тест проверки заполнения поля с выдержкой времени"
    )
  