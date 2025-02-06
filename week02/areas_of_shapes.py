
"""
Author: Santiago Bergerat 
Purpose: W02 Areas of shapes task

Additional Features:

"""

import math 
   
#   Intro
print('-' * 50)
print(f'{" Area Calculator":^50}')
print('-' * 50)

# Area of  square
square = float(input('What is the length of a side of the square?: '))
square_area = square ** 2
print(f'The area of the square is: {square_area:.2f}\n')

# Area of rectangle
rectangle_length = float(input('Enter the length of the rectangle: '))
rectangle_width = float(input('Enter the width of the rectangle: '))
rectangle_area = rectangle_length * rectangle_width
print(f'The area of the rectangle is: {rectangle_area:.2f}\n')



# Area of   circle
circle_radius = float(input('Enter the radius of the circle: '))
circle_area = math.pi * circle_radius ** 2 
print(f'The area of the circle is: {circle_area:.2f}\n')



# Stretch  challenge: Single value  for multiple shapes
value = float(input('Enter a value to calculate areas and volumes: '))



# Calculation 
square_area_unique = value ** 2
circle_area_unique = math.pi * (value ** 2)
cube_volume = value ** 3
sphere_volume = (4 / 3) * math.pi * value ** 3



# Display results 
print(f'Using the value {value}:')
print(f' - Area of square: {square_area_unique:.2f}')
print(f' - Area of circle: {circle_area_unique:.2f}')
print(f' - Volume of cube: {cube_volume:.2f}')
print(f' - Volume of sphere: {sphere_volume:.2f}')



# ---  Third point - areas in cm² and m² ----
print(f'{" Additional Conversion (cm² and m²) ":^50}')

square_cm = float(input('Enter the length of a side of the square (in cm): '))
square_area_cm = square_cm ** 2
square_area_m = square_area_cm * 0.0001
print(f'Square: {square_area_cm:.2f} cm² or {square_area_m:.4f} m² \n')

rectangle_length_cm = float(input('Enter the length of the rectangle (in cm): '))
rectangle_width_cm = float(input('Enter the width of the rectangle (in cm): '))
rectangle_area_cm = rectangle_length_cm * rectangle_width_cm
rectangle_area_m = rectangle_area_cm * 0.0001
print(f'Rectangle: {rectangle_area_cm:.2f} cm² or {rectangle_area_m:.4f} m²\n')


circle_radius_cm = float(input('Enter the radius of the circle (in cm): '))
circle_area_cm = math.pi * circle_radius_cm ** 2
circle_area_m = circle_area_cm * 0.0001
print(f'Circle: {circle_area_cm:.2f} cm² or {circle_area_m:.4f} m²\n')