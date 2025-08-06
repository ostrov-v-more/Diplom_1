import allure
from praktikum.bun import Bun


@allure.title("Получение имени булочки")
def test_bun_get_name():
    name = "Сладкая булочка"
    bun = Bun(name, 100)
    assert name == bun.get_name(), "Название не соответствует ожидаемому"


@allure.title("Получение имени булочки")
def test_bun_get_price():
    price = 100
    bun = Bun("Сладкая булочка", price)
    assert price == bun.get_price(), "Цена не соответствует ожидаемой"
