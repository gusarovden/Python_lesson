def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "positive: Тесты, которые проверяют корректное поведение функции"
    )
    config.addinivalue_line(
        "markers",
        "negative: Тесты, которые проверяют некорректное поведение функции"
    )