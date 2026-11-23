import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:
    @pytest.mark.parametrize('kind', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type(self, kind):
        ingredient = Ingredient(kind, 'ingredient', 10)
        assert ingredient.get_type() == kind

    @pytest.mark.parametrize('name', ['hot sauce', 'Соус'])
    def test_get_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 10)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('price', [0, 100, 25.5])
    def test_get_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Котлета', price)
        assert ingredient.get_price() == price
