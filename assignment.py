#Smart Temperature converter 
#Take input in Celsius and print its equivalent in Pahrenheit an Kalvin.

celsius = float(input("Enter Temperature in celcius : "))

fahrenheit = (celsius*9/5)+32

kelvin = celsius + 273.15

print(f"Temperature in Celsius is : {celsius}")
print(f"Temperature in Fahrenheit is : {fahrenheit}")
print(f"Temperature in Kelvin is : {kelvin}")
