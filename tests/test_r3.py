from common.r3 import R3
from pytest import approx


def r3approx(self, other):
    return self.x == approx(other.x) and self.y == approx(other.y) and \
            self.z == approx(other.z)


setattr(R3, 'approx', r3approx)


class TestR3:

    # Выполнено неравенство КБШ
    def test_norm1(self):
        x, y = R3(1.0, 3.0, -2.0), R3(-2.0, 1.0, 0.0)
        assert abs(x.dot(y)) <= x.norm() * y.norm()

    # Норма нулевого элемента равна нулю
    def test_norm2(self):
        assert R3(0.0, 0.0, 0.0).norm() == approx(0.0)

    # Умножение вектора на число увеличивает норму в то же число раз
    def test_norm3(self):
        a, b = R3(5.0, 5.0, -5.0), R3(1.0, 1.0, 1.0)
        assert a.norm() == approx(5.0 * b.norm())

    # Выполнено неравенство треугольника
    def test_norm4(self):
        x, y = R3(1.0, 3.0, -2.0), R3(-2.0, 1.0, 0.0)
        assert (x + y).norm() <= x.norm() + y.norm()

    # Вектор площади ортогонален векторам, образующим треугольник
    def test_area1(self):
        a, b, c = R3(1.0, 1.0, 1.0), R3(0.0, 3.0, 2.0), R3(1.0, 2.0, -2.0)
        assert R3.area(a, b, c).dot(a - c) == approx(0.0)
        assert R3.area(a, b, c).dot(b - c) == approx(0.0)
        assert R3.area(a, b, c).dot(c - a) == approx(0.0)

    # Вычисление вектора площади
    def test_area2(self):
        a, b, c = R3(1.0, 1.0, 1.0), R3(0.0, 3.0, 2.0), R3(1.0, 2.0, -2.0)
        s = R3.area(a, b, c)
        assert s.approx(R3(-3.5, -1.5, -0.5))
