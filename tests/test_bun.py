import allure
from praktikum.bun import Bun


class TestBun:

    @allure.title("Получение имени булочки")
    def test_bun_get_name(self):
        name = "Сладкая булочка"
        bun = Bun(name, 100)
        assert name == bun.get_name(), "Название не соответствует ожидаемому"


    @allure.title("Получение имени булочки")
    def test_bun_get_price(self):
        price = 100
        bun = Bun("Сладкая булочка", price)
        assert price == bun.get_price(), "Цена не соответствует ожидаемой"
