import unittest

def area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Стороны прямоугольника не могут быть отрицательными")
    return width * height


def perimeter(width, height):
    if width < 0 or height < 0:
        raise ValueError("Стороны прямоугольника не могут быть отрицательными")
    return 2 * (width + height)


class RectangleTestCase(unittest.TestCase):

    def test_zero_area(self):
        self.assertEqual(area(10, 0), 0)

    def test_square_area(self):
        self.assertEqual(area(10, 10), 100)

    def test_float_area(self):
        self.assertAlmostEqual(area(2.5, 4.0), 10.0)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-5, 10)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0, 10), 20)

    def test_square_perimeter(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_float_perimeter(self):
        self.assertAlmostEqual(perimeter(2.5, 4.0), 13.0)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-2, 5)


if __name__ == '__main__':
    unittest.main()