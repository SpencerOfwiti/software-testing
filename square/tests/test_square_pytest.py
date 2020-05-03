import pytest
from ..square import Square


# marking tests
@pytest.mark.area
def test_square_area():
	sq = Square(2)
	assert sq.area() == 4, f'Area for side {sq.side} units is {sq.area()}'


def test_square_perimeter():
	sq = Square(-1)
	assert sq.perimeter() == -1, f'Perimeter is shown {sq.perimeter()} rather than -1'
