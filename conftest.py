import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = 100
    bun.get_name.return_value = "black bun"
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_price.return_value = 50
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_type.return_value = "FILLING"
    return ingredient
