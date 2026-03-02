import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


def test_set_buns(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

def test_add_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    assert mock_ingredient in burger.ingredients

def test_remove_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0

def test_move_ingredient(burger):
    ingredient1 = Mock()
    ingredient2 = Mock()
    ingredient3 = Mock()

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.add_ingredient(ingredient3)

    burger.move_ingredient(0, 2)

    assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

@pytest.mark.parametrize("ingredient_prices, expected_total", [
    ([50], 250),
    ([50, 50], 300),
    ([10, 20, 30], 260),
])
def test_get_price(burger, mock_bun, ingredient_prices, expected_total):
    burger.set_buns(mock_bun)

    for price in ingredient_prices:
        ingredient = Mock()
        ingredient.get_price.return_value = price
        burger.add_ingredient(ingredient)

    assert burger.get_price() == expected_total

def test_get_receipt(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    receipt = burger.get_receipt()

    assert "(==== black bun ====)" in receipt
    assert "= filling cutlet =" in receipt
    assert "Price: 250" in receipt
