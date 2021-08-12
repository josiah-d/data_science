import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):

    def setUp(self):
        self.p0 = Polynomial([-1, 3, 10])
        self.p1 = Polynomial([5, 2, 3])
        self.p2 = Polynomial([6, -4, 0, 2])
        self.p3 = Polynomial([0, 0, 0])
        self.p4 = Polynomial([1, 0, 0, 0])
        self.p5 = Polynomial([])
        self.p6 = Polynomial([1, -3, -10])
        self.p7 = Polynomial([-5, 13, 53, 29, 30])
        self.p8 = Polynomial([3, 20])

    def test_add(self):
        self.assertEquals(self.p5 + self.p0, self.p0)
        self.assertEquals(self.p0 + self.p6, self.p3)

    def test_multiply(self):
        self.assertEquals(self.p5 * self.p0, self.p3)
        self.assertEquals(self.p0 * self.p1, self.p7)

    def test_order(self):
        self.assertEquals(self.p5.degree(), 0)
        self.assertEquals(self.p3.degree(), 0)
        self.assertEquals(self.p0.degree(), 2)
        self.assertEquals(self.p2.degree(), 3)

    def test_str(self):
        self.assertEquals(str(self.p0), "10x^2 + 3x - 1")
        self.assertEquals(str(self.p6), "-10x^2 - 3x + 1")
        self.assertEquals(str(self.p3), "0")

    def test_differentiate(self):
        self.assertEquals(self.p3.differentiate(), self.p3)
        self.assertEquals(self.p0.differentiate().differentiate().differentiate(), self.p3)
        self.assertEquals(self.p0.differentiate(), self.p8)

