from shadow.polyedr import Polyedr
from pytest import approx


class TestPolyedr:

    def test_oxyarea1(self):
        pol = Polyedr("data/tri_hor.geom")
        pol._shader()
        pol.ihwfunc()
        assert pol.oxyarea == approx(6.0)

    def test_oxyarea2(self):
        pol = Polyedr("data/box.geom")
        pol._shader()
        pol.ihwfunc()
        assert pol.oxyarea == approx(0.0)

    def test_oxyarea3(self):
        pol = Polyedr("data/threefacets.geom")
        pol._shader()
        pol.ihwfunc()
        assert pol.oxyarea == approx(0.0)

    def test_oxyarea4(self):
        pol = Polyedr("data/triangle.geom")
        pol._shader()
        pol.ihwfunc()
        assert pol.oxyarea == approx(32.0)

    def test_numedge1(self):
        pol = Polyedr("data/tri_hor.geom")
        assert pol.numedge == [0, 4, 7]

    def test_numedge2(self):
        pol = Polyedr("data/box.geom")
        assert pol.numedge == [0, 4, 8, 12, 16, 20]

    def test_gomc1(self):
        pol = Polyedr("data/tri_hor.geom")
        with open("data/tri_hor.geom") as f:
            strn = f.readline().split()
            c = float(strn[0])
        assert pol.gomc == approx(c)

    def test_gomc2(self):
        pol = Polyedr("data/box.geom")
        with open("data/box.geom") as f:
            strn = f.readline().split()
            c = float(strn[0])
        assert pol.gomc == approx(c)
