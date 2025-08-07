import allure
import pytest
from praktikum.database import Database


class TestDatabase:

    @allure.title("Получаем ответ от методов класс Database")
    @pytest.mark.parametrize(
        "method_name, expected_len",
        [
            ("available_buns", 3),
            ("available_ingredients", 6),
        ]
    )
    def test_get_datebase_attributes(self, method_name, expected_len):
        database = Database()
        method = getattr(database, method_name)
        assert expected_len == len(method())
