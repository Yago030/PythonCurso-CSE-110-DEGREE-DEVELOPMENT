"""
Author : Santiago Bergerat
task: windchill calculator 
This code calculates wind chill and ensures the user correctly enters "C" or "F" for temperature input.
"""
def wind_chill(t,v):
    return 35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)

def convert_to_fahrenheit(tc):
    tempConverted = (tc * 9/5) + 32
    return tempConverted

t = float(input('What is the temperature? '))

while True:
        temperature_measurement = input("Fahrenheit or Celsius (F/C) ? ").upper()
        if temperature_measurement[0] == "F" or temperature_measurement[0] == "C":
            if temperature_measurement[0] == "C":
                t = convert_to_fahrenheit(t)
            break
        else:
            print( "You must enter C or F only")
            
             
for v in range(5, 65, 5):
    windChill = wind_chill(t,v)
    print(f'At temperature {t}.0F, and wind speed {v} mph, the wind chill is : {windChill:.2f}F')