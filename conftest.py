import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


@pytest.fixture()
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = mock_bun.name = "Сладкая булочка"
    mock.get_price.return_value = mock_bun.price = 8
    return mock


@pytest.fixture()
def mock_ingredient_0():
    mock = Mock()
    mock.get_type.return_value = mock.type = "Соус"
    mock.get_name.return_value = mock.name = "Белый соус"
    mock.get_price.return_value = mock.price = 10
    return mock


@pytest.fixture()
def mock_ingredient_1():
    mock = Mock()
    mock.get_type.return_value = mock.type = "Овощ"
    mock.get_name.return_value = mock.name = "Сеньор-помидор"
    mock.get_price.return_value = mock.price = 15
    return mock


@pytest.fixture()
def mock_ingredient_2():
    mock = Mock()
    mock.get_type.return_value = mock.type = "Начинка"
    mock.get_name.return_value = mock.name = "Котлетка"
    mock.get_price.return_value = mock.price = 25
    return mock


@pytest.fixture()
def ingredients(mock_ingredient_0, mock_ingredient_1, mock_ingredient_2):
    return {"ingredient_0": mock_ingredient_0,
            "ingredient_1": mock_ingredient_1,
            "ingredient_2": mock_ingredient_2
            }


@pytest.fixture()
def burger_with_three_ingredients(mock_bun, mock_ingredient_0, mock_ingredient_1, mock_ingredient_2):
    burger = Burger()
    burger.bun = mock_bun
    burger.ingredients = [mock_ingredient_0, mock_ingredient_1, mock_ingredient_2]
    return burger


@pytest.fixture()
def mock_burger(mock_bun, burger_with_three_ingredients):

    price = mock_bun.get_price() * 2
    for ingredient in burger_with_three_ingredients.ingredients:
        price += ingredient.get_price()

    mock = Mock()
    mock.get_price.return_value = price
    mock.get_receipt.return_value = (
        "(==== Сладкая булочка ====)\n"
        "= соус Белый соус =\n"
        "= овощ Сеньор-помидор =\n"
        "= начинка Котлетка =\n"
        "(==== Сладкая булочка ====)\n"
        "\nPrice: 66"
    )
    return mock


@pytest.fixture()
def ingredient():
    return Ingredient(
        ingredient_type="Color",
        name="Black",
        price=123,
    )
