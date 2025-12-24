import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),                   # Первая буква заглавная
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("sKyPrO", "SKyPrO")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   04 апреля 2025", "04 апреля 2025"),       # дата с пробелами
    ("   123", "123")                              # числовая строка с пробелами
])
def test_trim_positive_cases(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("text, symbol, expected", [
        ("SkyPro", "S", True),           # символ в начале
        ("12345", "3", True)             # цифра в середине
        
])
def test_contains_positive_cases(text, symbol, expected):
    assert string_utils.contains(text, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("text, symbol, expected", [
        ("SkyPro", "k", "SyPro"),                 # удаление одиночного символа
        ("04 апреля 2023", "апреля ", "04 2023")  # удаление подстроки с пробелом
    ],
    ids=[
        "одиночный_символ",
        "подстрока_с_пробелом"
])
def test_delete_symbol_positive_cases(text, symbol, expected):
    result = string_utils.delete_symbol(text, symbol)
    assert result == expected  


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),              # строка с цифрами и буквами — нет изменений
    ("", ""),                          # пустая строка — остаётся пустой
    ("   ", "   "),                    # строка из пробелов — остаётся без изменений
    ("#test", "#test")                 # строка с спецсимволом — нет изменений
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("invalid_input, expected_exception", [
    ("", None),                   
    ([], AttributeError),         
])
def test_trim_negative_cases(invalid_input, expected_exception):
    if expected_exception is None:
        assert string_utils.trim(invalid_input) == ""
    else:
         with pytest.raises(expected_exception):
            string_utils.trim(invalid_input)  

@pytest.mark.negative
@pytest.mark.parametrize("text, symbol, expected", [
    ("", "a", False),          # пустая строка
    (" ", "a", False)          # строка с пробелом
])
def test_contains_empty_or_space_string(text, symbol, expected):
     assert string_utils.contains(text, symbol) == expected          

@pytest.mark.negative
@pytest.mark.parametrize("text, symbol", [
        ("", "a"),               # пустая строка
        ("   ", " "),            # строка из пробелов
    ],
    ids=[
        "пустая_строка",
        "только_пробелы"
])
def test_delete_symbol_edge_cases(text, symbol):
    result = string_utils.delete_symbol(text, symbol)
    if symbol == " ":
        assert result == ""
    else:
        assert result == text