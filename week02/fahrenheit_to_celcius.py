

"""
Author: Santiago Bergerat 

Purpose: Second week Temperature unit converter

"""

print ('-'* 50 )
print (f'{"Temperature Unit Converter": ^50}')
print ('-'*50)

degrees_fahrenheit = int(input('Enter degrees in Fahrenheit:  '))
convert_to_celsius  = ( degrees_fahrenheit - 32 ) * ( 5/9 )

print(f'To convert {degrees_fahrenheit}°F to Celsius, the result is {convert_to_celsius:.1f}°C')
