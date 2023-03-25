#function for fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

#function for celsuis
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

#function for wind chill
def wind_chill(temperature, wind_speed):
    return 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16

#asking user for information
temperature = float(input("What is the temperature? "))
temp_unit = input("Fahrenheit or Celsius (F/C)? ")

#calculating the temperature
if temp_unit == 'C':
    temperature = celsius_to_fahrenheit(temperature)

#calculating the temperature with windchill
for wind_speed in range(5, 65, 5):
    windchill = wind_chill(temperature, wind_speed)
    print("At temperature {:.1f}F, and wind speed {:d} mph, the windchill is: {:.2f}F".format(temperature, wind_speed, windchill))