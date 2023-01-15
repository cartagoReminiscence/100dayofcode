from guess import get_random_number, Game
import random
from unittest.mock import patch
import pytest

@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 10
    assert get_random_number() == 10

@patch("builtins.input", side_effect=[9, '14', 'ana', 14, 5, -10, 24, None])
def test_guess(inp):
    game = Game()
    #good
    assert game.guess() == 9
    assert game.guess() == 14
    #not a number
    with pytest.raises(ValueError):
        game.guess()
    #already guessed 14
    with pytest.raises(ValueError):
        game.guess()
    #good
    assert game.guess() == 5
    #out of the range
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    #input value: empty 
    with pytest.raises(ValueError):
        game.guess()