from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        buns = Database().available_buns()
        actual = [(bun.get_name(), bun.get_price()) for bun in buns]
        assert actual == [('black bun', 100), ('white bun', 200), ('red bun', 300)]

    def test_available_ingredients(self):
        ingredients = Database().available_ingredients()
        actual = [(item.get_type(), item.get_name(), item.get_price()) for item in ingredients]
        assert actual == [
            ('SAUCE', 'hot sauce', 100), ('SAUCE', 'sour cream', 200),
            ('SAUCE', 'chili sauce', 300), ('FILLING', 'cutlet', 100),
            ('FILLING', 'dinosaur', 200), ('FILLING', 'sausage', 300),
        ]
