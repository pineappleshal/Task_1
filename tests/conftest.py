from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = 'Краторная булка'
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def ingredients():
    result = []
    for kind, name, price in [('SAUCE', 'Соус', 25),
                              ('FILLING', 'Котлета', 75),
                              ('FILLING', 'Сыр', 10)]:
        ingredient = Mock(spec=Ingredient)
        ingredient.get_type.return_value = kind
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        result.append(ingredient)
    return result
