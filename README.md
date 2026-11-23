# Task_1 — юнит-тесты Stellar Burgers

Тесты классов `Bun`, `Burger`, `Ingredient` и `Database` из заготовки Яндекс Практикума.
Исходные модули перенесены в пакет `praktikum`, который уже указан в их импортах.
Логика приложения сохранена без изменений.

## Запуск

```bash
python -m venv .venv
```

Windows: `.venv\Scripts\activate`. Linux/macOS: `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python -m pytest --cov=praktikum --cov-branch --cov-report=term-missing --cov-report=html:htmlcov --cov-report=xml:coverage.xml --cov-report=markdown:coverage.md
```

## Проверки и результат

28 тестов прошли. Покрытие требуемых классов и их ветвлений — 100%.
Покрытие всего пакета с демонстрационным сценарием — 76,84% (минимум по заданию — 70%).
HTML-отчёт: `htmlcov/index.html`; краткая таблица: `coverage.md`; машиночитаемый отчёт: `coverage.xml`.
В общий отчёт также включён демонстрационный сценарий `praktikum/praktikum.py`:
он не вызывается юнит-тестами четырёх классов и показан как непокрытый код.

- `test_bun.py`: имя и стоимость булки, включая нулевую и дробную цену.
- `test_ingredient.py`: тип, имя и стоимость ингредиента.
- `test_burger.py`: начальное состояние, выбор булки, добавление, удаление и перемещение ингредиентов, стоимость и точный текст чека.
- `test_database.py`: состав каталогов булок и ингредиентов.

В тестах бургера используются `unittest.mock.Mock` с `spec`, чтобы изолировать его от реализаций булки и ингредиента.
Параметризация покрывает разные значения и позиции в списке. Объекты создаются заново для каждого теста.

Рабочая ветка: `develop1`. Для запуска демонстрационного приложения: `python -m praktikum.praktikum`.
