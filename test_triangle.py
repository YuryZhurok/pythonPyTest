import pytest
from triangle.triangle import Triangle


class TestTrianglePtest:

    def test_triangle_exist(self):
        assert Triangle.check_if_exist(7, 8, 9)

    def test_triangle_right(self, right_triangle):
        assert right_triangle.is_right_triangle()

    def test_triangle_right_angled(self, simple_triangle):
        assert simple_triangle.is_right_angled()

    def test_triangle_perimetr(self, simple_triangle):
        assert simple_triangle.perimetr() == 12

    @pytest.mark.parametrize("a, b, c", [(7, 8, 9), (8, 9, 7)])
    def test_triangle_eq(self, a, b, c):
        first = Triangle(a, b, c)
        second = Triangle(9, 8, 7)
        assert first == second

    def test_triangle_lt(self, simple_triangle, right_triangle):
        assert simple_triangle.perimetr() < right_triangle.perimetr()

    def test_triangle_two_sides_eq(self):
        first = Triangle(3, 3, 5)
        assert first.two_sides_eq()

    def test_triangle_rb(self, rb_triangle):
        assert rb_triangle.two_sides_eq()

    @pytest.mark.parametrize("a, b, c", [(6, 8, 10), (9, 12, 15)])
    def test_triangle_equal(self, a, b, c, simple_triangle):
        first = Triangle(a, b, c)
        assert simple_triangle.equal(first)
