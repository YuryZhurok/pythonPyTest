import pytest
from triangle.triangle import Triangle


@pytest.fixture()
def right_triangle():
    right_tr = Triangle(6, 6, 6)
    yield right_tr
    del right_tr


@pytest.fixture()
def simple_triangle():
    simple_tr = Triangle(3, 4, 5)
    yield simple_tr
    del simple_tr


@pytest.fixture(params=[(3, 3, 5), (8, 8, 11), (5, 8, 5)])
def rb_triangle(request):
    rb_tr = Triangle(request.param[0], request.param[1], request.param[2])
    yield rb_tr
    del rb_tr

