def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "test_calculator: Тест проверки заполнения поля с выдержкой времени"
    )
    config.addinivalue_line(
        "markers",
        "test_shop: Тест проверки итоговой суммы"
    )