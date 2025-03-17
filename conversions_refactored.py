class ConversionNotPossible(Exception):
    """Raised when two units are not compatible for conversion."""
    pass

def convert(fromUnit, toUnit, value):
    """Converts a value from one unit to another.
    Arguments:
        fromUnit (str): The unit we are converting from.
        toUnit (str): The unit we are converting to.
        value (float): The value to be converted.
    Returns:
        float: The converted value.
    Raises:
        ConversionNotPossible: If the conversion is not possible.
    """
    if fromUnit == toUnit:
        return value

    # Temperature conversions
    temperature_conversions = {
        'celsius': {
            'fahrenheit': lambda c: (c * 9 / 5) + 32,
            'kelvin': lambda c: c + 273.15
        },
        'fahrenheit': {
            'celsius': lambda f: (f - 32) * 5 / 9,
            'kelvin': lambda f: (f - 32) * 5 / 9 + 273.15
        },
        'kelvin': {
            'celsius': lambda k: k - 273.15,
            'fahrenheit': lambda k: (k - 273.15) * 9 / 5 + 32
        }
    }

    # Distance conversions
    distance_conversions = {
        'miles': {
            'yards': lambda m: m * 1760,
            'meters': lambda m: m * 1609.34
        },
        'yards': {
            'miles': lambda y: y / 1760,
            'meters': lambda y: y * 0.9144
        },
        'meters': {
            'miles': lambda m: m / 1609.34,
            'yards': lambda m: m / 0.9144
        }
    }

    if fromUnit in temperature_conversions and toUnit in temperature_conversions[fromUnit]:
        return round(temperature_conversions[fromUnit][toUnit](value), 2)

    if fromUnit in distance_conversions and toUnit in distance_conversions[fromUnit]:
        return round(distance_conversions[fromUnit][toUnit](value), 2)

    # If no valid conversion is found
    raise ConversionNotPossible(f"Cannot convert {fromUnit} to {toUnit}")
