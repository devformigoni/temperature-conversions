# Programthat converts degrees Celsius to Kelvin and degrees Fahrenheit
 
# Developed by Paulo Orestes Formigoni profpauloformigoni@gmail.com
# Version 1.0 January 2023

## When running this code, you will be asked to enter the temperature in degrees Celsius,
## and then the result will be displayed in Kelvin and Fahrenheit.

########### Group of functions used in this program ##############

def celsius_to_kelvin(celsius):
  kelvin = celsius + 273.15
  return kelvin

def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

########### Main Body of the Program ########### 
celsius = float(input("Enter the temperature in degrees Celsius: "))
kelvin = celsius_to_kelvin(celsius)
fahrenheit = celsius_to_fahrenheit(celsius)

print("The temperature in Kelvin is: {:.2f} K".format(kelvin))
print("The temperature in Fahrenheit is: {:.2f} °F".format(fahrenheit))
