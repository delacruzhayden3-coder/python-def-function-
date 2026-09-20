# Temperature Converter

# This def function is used to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Get temperature from the user
celsius = float(input("Enter temperature in Celsius: "))

# Call/invoke the function
result = celsius_to_fahrenheit(celsius)

# Display the result
print("Temperature in Fahrenheit:", result)
