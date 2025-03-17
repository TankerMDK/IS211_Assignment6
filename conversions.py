
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins
    Formula: K = C + 273.15
    Argument: celsius (float): Temperature in Celsius.
    Returns: float: Temperature in Kelvins."""

    # Converts Celsius to Kelvin using the formula
    kelvins = round(celsius + 273.15, 2) # This rounds things to 2 decimal places.
    return kelvins

def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit
    Formula: F = (C * 9/5) + 32
    Argument: celsius (float): Temperature in Celsius.
    Returns: float: Temperature in Fahrenheit.
    """
    # Converts Celsius to Fahrenheit using the formula
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    celsius = round((fahrenheit - 32) * 5 / 9, 2)
    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    """Converts Fahrenheit to Kelvin."""
    kelvin = round((fahrenheit - 32) * 5/9 + 273.15, 2)
    return kelvin

def convertKelvinToCelsius(kelvin):
    """Converts Kelvin to Celsius."""
    celsius = round(kelvin - 273.15, 2)
    return celsius

def convertKelvinToFahrenheit(kelvin):
    """Converts Kelvin to Fahrenheit."""
    fahrenheit = round((kelvin - 273.15) * 9/5 + 32, 2)
    return fahrenheit
