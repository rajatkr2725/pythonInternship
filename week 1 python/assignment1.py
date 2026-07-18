def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

# Example Usage
c_temp = 37
f_temp = 98.6

print(f"{c_temp}°C is equal to {celsius_to_fahrenheit(c_temp)}°F")
print(f"{f_temp}°F is equal to {fahrenheit_to_celsius(f_temp)}°C")