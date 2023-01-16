from fizzbuzz import fizzbuzz
import pytest

@pytest.mark.parametrize(
    "inp, ret",
    [
        (1, 1), (2, 2), (3, 'fizz'),
        (4, 4), (5, 'buzz'), (6, 'fizz'),
        (7, 7), (8, 8), (9, 'fizz'),
        (10, 'buzz'), (11, 11), (12, 'fizz'),
        (13, 13), (14, 14), (15, 'fizzbuzz'),
    ]
)
def test_fizbuzz(inp, ret):
    assert fizzbuzz(inp) == ret

if __name__ == "__main__":
    pass