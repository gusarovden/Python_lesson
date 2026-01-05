def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "form_test: Тест проверки заполнения формы."
    )