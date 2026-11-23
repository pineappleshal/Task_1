import pytest


class TestBurger:
    def test_new_burger_is_empty(self, burger):
        assert burger.bun is None and burger.ingredients == []

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun is bun

    def test_add_ingredients_preserves_order(self, burger, ingredients):
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        assert burger.ingredients == ingredients

    @pytest.mark.parametrize('index,remaining', [(0, [1, 2]), (1, [0, 2]), (2, [0, 1])])
    def test_remove_ingredient_by_index(self, burger, ingredients, index, remaining):
        burger.ingredients = ingredients.copy()
        burger.remove_ingredient(index)
        assert burger.ingredients == [ingredients[i] for i in remaining]

    @pytest.mark.parametrize('index,new_index,order', [
        (0, 2, [1, 2, 0]), (2, 0, [2, 0, 1]), (1, 1, [0, 1, 2]),
    ])
    def test_move_ingredient(self, burger, ingredients, index, new_index, order):
        burger.ingredients = ingredients.copy()
        burger.move_ingredient(index, new_index)
        assert burger.ingredients == [ingredients[i] for i in order]

    @pytest.mark.parametrize('count,expected', [(0, 200), (1, 225), (3, 310)])
    def test_price_includes_two_buns_and_all_ingredients(
        self, burger, bun, ingredients, count, expected,
    ):
        burger.bun = bun
        burger.ingredients = ingredients[:count]
        assert burger.get_price() == expected

    def test_receipt_with_ingredients(self, burger, bun, ingredients):
        burger.bun = bun
        burger.ingredients = ingredients[:2]
        expected = ('(==== Краторная булка ====)\n'
                    '= sauce Соус =\n'
                    '= filling Котлета =\n'
                    '(==== Краторная булка ====)\n\n'
                    'Price: 300')
        assert burger.get_receipt() == expected

    def test_receipt_without_ingredients(self, burger, bun):
        burger.bun = bun
        expected = ('(==== Краторная булка ====)\n'
                    '(==== Краторная булка ====)\n\nPrice: 200')
        assert burger.get_receipt() == expected
