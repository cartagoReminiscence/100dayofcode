from guess import get_random_number, Game
import random
from unittest.mock import patch
import pytest

@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 10
    assert get_random_number() == 10

side_effect = [9, '14', 'ana', 14, 5, -10, 24, None]
@patch("builtins.input", side_effect=side_effect)
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
    #out of range
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    #input value: empty 
    with pytest.raises(ValueError):
        game.guess()

def test_validate_guess(capfd):
    game = Game()
    game._answer = 7

    #too high or low
    assert not game._validate_guess(6)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '6 is too low'
    assert not game._validate_guess(8)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '8 is too high'
    #good
    assert game._validate_guess(7)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '7 is correct!'

side_effect=[1, 20, 14, 7, 10]
@patch('builtins.input', side_effect=side_effect)
def test_game_win(inp, capfd):
    game = Game()
    game._answer = 10

    game()
    assert game._win is True

    out, _ = capfd.readouterr()
    expected = ['1 is too low', '20 is too high',
                '14 is too high', '7 is too low',
                '10 is correct!','It took you 5 guesses'
                ]

    output = [line for line in out.split('\n') if line.rstrip()]
    for line, exp in zip(expected, output):
        assert line == exp

side_effect=[None, 4, 5, 11, 9, 1]
@patch('builtins.input', side_effect=side_effect)
def test_game_lose(inp, capfd):
    game = Game()
    game._answer = 10

    game()
    assert game._win is False

    out = capfd.readouterr()[0]
    print("\n")
    print(out.rstrip())