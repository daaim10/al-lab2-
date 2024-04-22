def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"Temperature in Fahrenheit is: {fahrenheit}°F")

# Convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"Temperature in Celsius is: {celsius}°C")
