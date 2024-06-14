def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def convert_temperature(value, unit):
    if unit.lower() == 'c':
        celsius = value
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        return fahrenheit, kelvin
    elif unit.lower() == 'f':
        fahrenheit = value
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        return celsius, kelvin
    elif unit.lower() == 'k':
        kelvin = value
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        return celsius, fahrenheit
    else:
        raise ValueError("Unknown temperature unit. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

def main():
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip()
        
        if unit.lower() == 'c':
            fahrenheit, kelvin = convert_temperature(value, unit)
            print(f"{value} degrees Celsius is equivalent to {fahrenheit:.2f} degrees Fahrenheit and {kelvin:.2f} Kelvin.")
        elif unit.lower() == 'f':
            celsius, kelvin = convert_temperature(value, unit)
            print(f"{value} degrees Fahrenheit is equivalent to {celsius:.2f} degrees Celsius and {kelvin:.2f} Kelvin.")
        elif unit.lower() == 'k':
            celsius, fahrenheit = convert_temperature(value, unit)
            print(f"{value} Kelvin is equivalent to {celsius:.2f} degrees Celsius and {fahrenheit:.2f} degrees Fahrenheit.")
        else:
            print("Invalid unit of measurement. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
