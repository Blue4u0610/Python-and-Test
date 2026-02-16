"""
Author:Jinfeng Lan
Time:2026/1/25 11:23
Class:SSW 567
Project name:Testing Triangle Classification
"""

from triangle_classification import triangle_classification

def test_nottriangle():
    # when three sides can't form a triangle
    assert triangle_classification(1, 2, 3) == 'Not A Triangle'
    assert triangle_classification(5, 10, 16) == 'Not A Triangle'
    assert triangle_classification(9.4, 1.9, 13.4) == 'Not A Triangle'
    assert triangle_classification(23, 0, 13.4) == 'Not A Triangle'
    assert triangle_classification(-3, 5, 4) == 'Not A Triangle'

def test_equilateral():
    # when three sides are all equal
    assert triangle_classification(0.1, 0.1, 0.1) == 'Equilateral'
    assert triangle_classification(999999999, 999999999, 999999999) == 'Equilateral'

def test_isosceles():
    # when only two sides are equal to each other and not right
    assert triangle_classification(3, 3, 5) == 'Isosceles'
    assert triangle_classification(7.9, 4.45, 4.45) == 'Isosceles'

def test_scalene():
    # not equilateral , isosceles , right
    assert triangle_classification(3, 4, 6) == 'Scalene'
    assert triangle_classification(7.9, 4.46, 4.45) == 'Scalene'

def test_right_scalene():
    assert triangle_classification(3, 4, 5) == 'Right Scalene'
    assert triangle_classification(13, 5, 12) == 'Right Scalene'