"""
Author:Jinfeng Lan
Time:2026/1/25 11:23
Class:SSW 567
Project name:Testing Triangle Classification
"""
import unittest

from triangle_classification import triangle_classification

class TestTriangles(unittest.TestCase):

    def test_nottriangle(self):
        # when three sides can't form a triangle
        self.assertEqual(triangle_classification(1, 2, 3), 'Not A Triangle')
        self.assertEqual(triangle_classification(5, 10, 16), 'Not A Triangle')
        self.assertEqual(triangle_classification(9.4, 1.9, 13.4), 'Not A Triangle')
        self.assertEqual(triangle_classification(23, 0, 13.4), 'Not A Triangle')
        self.assertEqual(triangle_classification(-3, 5, 4), 'Not A Triangle')

    def test_equilateral(self):
        # when three sides are all equal
        self.assertEqual(triangle_classification(0.1, 0.1, 0.1), 'Equilateral')
        self.assertEqual(triangle_classification(999999999, 999999999, 999999999), 'Equilateral')

    def test_isosceles(self):
        # when only two sides are equal to each other and not right
        self.assertEqual(triangle_classification(3, 3, 5), 'Isosceles')
        self.assertEqual(triangle_classification(7.9, 4.45, 4.45), 'Isosceles')

    def test_scalene(self):
        # not equilateral , isosceles , right
        self.assertEqual(triangle_classification(3, 4, 6), 'Scalene')
        self.assertEqual(triangle_classification(7.9, 4.46, 4.45), 'Scalene')

    def test_right_scalene(self):
        self.assertEqual(triangle_classification(3, 4, 5), 'Right Scalene')
        self.assertEqual(triangle_classification(13, 5, 12), 'Right Scalene')

if __name__ == '__main__':
    unittest.main()