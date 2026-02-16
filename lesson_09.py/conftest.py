def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "students: Тест на проверку БД"
    )