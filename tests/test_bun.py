import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name', ['black bun', 'Краторная булка'])
    def test_get_name(self, name):
        bun = Bun(name, 100)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [0, 100, 99.5])
    def test_get_price(self, price):
        bun = Bun('bun', price)
        assert bun.get_price() == price
