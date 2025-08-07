import allure
import pytest
from praktikum.burger import Burger


class TestBurger:

    @allure.title("Выбираем на какой булочке будет бургер")
    def test_set_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert mock_bun == burger.bun, "У бургера не та булочка которую выбрали"


    @allure.title("Добавляем ингредиенты в бургер")
    @pytest.mark.parametrize(
        "ingredients_list, expected_value",
        [
            ([], 0),
            (["глаз пчелы"], 1),
            (["глаз пчелы", "хвост моржа"], 2),
        ]
    )
    def test_add_ingredient(self, ingredients_list, expected_value):
        burger = Burger()
        for ingredient in ingredients_list:
            burger.add_ingredient(ingredient)
        assert expected_value == len(burger.ingredients), "В бургер не доложили ингредиентов"


    @allure.title("Удаляем ингредиенты из бургер")
    @pytest.mark.parametrize(
        "ingredient_index, ingredient_list",
        [
            (0, ["ingredient_1", "ingredient_2"]),
            (1, ["ingredient_0", "ingredient_2"]),
        ]
    )
    def test_remove_ingredients(
            self, burger_with_three_ingredients, ingredient_index,
            ingredient_list, ingredients
    ):
        expected_ingredients = [ingredients[key] for key in ingredient_list]
        burger_with_three_ingredients.remove_ingredient(ingredient_index)
        assert expected_ingredients == burger_with_three_ingredients.ingredients, \
            "Список оставшихся ингредиентов не соответствует ожидаемому"


    @allure.title("Удаляем все ингредиенты из бургер")
    def test_remove_all_ingredients(self, burger_with_three_ingredients):
        for _ in range(len(burger_with_three_ingredients.ingredients)):
            burger_with_three_ingredients.remove_ingredient(0)
        assert [] == burger_with_three_ingredients.ingredients, "Были удалены не все ингредиенты"


    @allure.title("Меняем ингредиенты местами")
    def test_move_ingredient(self, burger_with_three_ingredients, mock_ingredient_1, mock_ingredient_2):
        burger_with_three_ingredients.move_ingredient(1, 2)
        assert (burger_with_three_ingredients.ingredients[1] == mock_ingredient_2 and
                burger_with_three_ingredients.ingredients[2] == mock_ingredient_1), \
            "Ингредиенты не поменялись местами"


    @allure.title("Получаем цену бургера")
    def test_get_price(self, burger_with_three_ingredients, mock_burger):
        assert mock_burger.get_price() == burger_with_three_ingredients.get_price(), \
            "Цена не соответствует ожидаемой"


    @allure.title("Получаем рецепт бургера")
    def test_get_receipt(self, burger_with_three_ingredients, mock_burger):
        assert mock_burger.get_receipt() == burger_with_three_ingredients.get_receipt()