"""
Author:Jinfeng Lan
Time:2026/1/25 21:48
Class:SSW 567
Project name:Testing Triangle Classification
"""
def triangle_classification(a, b, c):
    """
    Args:
        a 、b、c(float/int): three sides of a triangle

    Returns:
        str: 'Equilateral', 'Isosceles', 'Scalene', 'Right','NotATriangle'
    """

    if a <= 0 or b <= 0 or c <= 0:
        return 'Not A Triangle'
    # A triangle's three sides are greater than 0

    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return 'Not A Triangle'
    # The sum of any two sides of triangle is greater than the third side

    if a == b == c:
        return 'Equilateral'
    # Equilateral Determination：An equilateral triangle's triangle are all euqal



    short,mid,long = sorted([a,b,c])

    if short == mid or long == mid:
        shape = 'Isosceles'
    else:
        shape = 'Scalene'
    # Iso scalene Determination: An Isosceles triangle has two sides are equal to each other


    if(short * short + mid * mid == long * long):
        shape = 'Right ' + shape

    return shape

def main():# pragma: no cover
    print("Triangle Classification     ")

    while True:
        print("Please enter the three sides of a triangle(enter 'q' to quit)' ):     ")

        user_input = input()

        if user_input == 'q':
            break

        sides = user_input.split()

        if len(sides) != 3:
            print("Please enter a three sides of a triangle")
            continue

        shape = triangle_classification(float(sides[0]), float(sides[1]), float(sides[2]))
        if shape == 'Not A Triangle':
            print(shape)
        else:
            print("The shape of the triangle is " + shape + " triangle")

if __name__ == '__main__':# pragma: no cover
    main()