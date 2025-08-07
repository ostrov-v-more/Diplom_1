import allure
import pytest


class TestIngredient:

    @allure.title("Получаем ответ от методов класса Ingredient")
    @pytest.mark.parametrize(
        "method_name, expected_value",
        [
            ("get_name", "Black"),
            ("get_price", 123),
            ("get_type", "Color")
        ]
    )
    def test_ingredient_methods(self, ingredient, method_name, expected_value):
        method = getattr(ingredient, method_name)
        assert expected_value == method()
