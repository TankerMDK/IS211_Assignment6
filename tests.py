import conversions
import conversions_refactored
import unittest

    # Part 2
def test_convertCelsiusToKelvin():
    """
    Tests the convertCelsiusTOKelvin function with 5 test cases.
    Outputs the test results for each case.
    """
    print("\nTesting convertCelsiusToKelvin.")

    test_cases = [
        (0, 273.15),    # Freezing point of water
        (100, 373.15),  # Boiling point
        (-273.15, 0),   # Absolute zero
        (25, 298.15),   # Room temp
        (-100, 173.15)  # RNG negative value
    ]

    for i, (input_val, expected) in enumerate(test_cases, 1):
        result = conversions.convertCelsiusToKelvin(input_val)
        if result == expected:
            print(f"Test {i}: Successful — {input_val}C → {result}K")
        else:
            print(f"Test {i}: Failure — {input_val}C → {result}K (Expected: {expected})")

def test_convertCelsiusToFahrenheit():
    """
    Tests the convertCelsiusToFahrenheit function with 5 test cases.
    Outputs the test results for each case.
    """
    print("\nTesting convertCelsiusToFahrenheit.")

    test_cases = [
        (0, 32),       # Freezing point of water
        (100, 212),    # Boiling point
        (-40, -40),    # Where Celsius and Fahrenheit are equal.
        (25, 77),      # Room temp
        (-100, -148)   # RNG negative value
    ]

    for i, (input_val, expected) in enumerate(test_cases, 1):
        result = conversions.convertCelsiusToFahrenheit(input_val)
        if result == expected:
            print(f"Test {i}: Successful — {input_val}C → {result}F")
        else:
            print(f"Test {i}: Failure — {input_val}C → {result}F (Expected: {expected})")

    # Part III
def test_convertFahrenheitToCelsius():
    print("\nTesting convertFahrenheitToCelsius.")
    test_cases = [
        (32, 0),      # Freezing point of water
        (212, 100),   # Boiling point of water
        (-40, -40),   # Fahrenheit and Celsius equal at -40
        (98.6, 37),   # Human body temperature
        (0, -17.78)   # Freezing point in Fahrenheit
    ]
    for i, (input_val, expected) in enumerate(test_cases, 1):
        result = conversions.convertFahrenheitToCelsius(input_val)
        if result == expected:
            print(f"Test {i}: Successful — {input_val}F → {result}C")
        else:
            print(f"Test {i}: Failure — {input_val}F → {result}C (Expected: {expected})")


def test_convertFahrenheitToKelvin():
    print("\nTesting convertFahrenheitToKelvin.")
    test_cases = [
        (32, 273.15),
        (212, 373.15),
        (-40, 233.15),
        (98.6, 310.15),
        (0, 255.37)
    ]
    for i, (input_val, expected) in enumerate(test_cases, 1):
        result = conversions.convertFahrenheitToKelvin(input_val)
        if result == expected:
            print(f"Test {i}: Successful — {input_val}F → {result}K")
        else:
            print(f"Test {i}: Failure — {input_val}F → {result}K (Expected: {expected})")

def test_convertKelvinToCelsius():
    print("\nTesting convertKelvinToCelsius.")
    test_cases = [
        (273.15, 0),
        (373.15, 100),
        (233.15, -40),
        (310.15, 37),
        (255.37, -17.78)
    ]
    for i, (input_val, expected) in enumerate(test_cases, 1):
        result = conversions.convertKelvinToCelsius(input_val)
        if result == expected:
            print(f"Test {i}: Successful — {input_val}K → {result}C")
        else:
            print(f"Test {i}: Failure — {input_val}K → {result}C (Expected: {expected})")


def test_convertKelvinToFahrenheit():
    print("\nTesting convertKelvinToFahrenheit.")
    test_cases = [
        (273.15, 32),
        (373.15, 212),
        (233.15, -40),
        (310.15, 98.6),
        (255.37, 0)
    ]
    for i, (input_val, expected) in enumerate(test_cases, 1):
        result = conversions.convertKelvinToFahrenheit(input_val)
        if result == expected:
            print(f"Test {i}: Successful — {input_val}K → {result}F")
        else:
            print(f"Test {i}: Failure — {input_val}K → {result}F (Expected: {expected})")

    # Part IV
class TestConversionsRefactored(unittest.TestCase):

    def test_temperature_conversions(self):
        self.assertEqual(conversions_refactored.convert('celsius', 'fahrenheit', 100), 212)
        self.assertEqual(conversions_refactored.convert('celsius', 'kelvin', 0), 273.15)
        self.assertEqual(conversions_refactored.convert('fahrenheit', 'celsius', 32), 0)
        self.assertEqual(conversions_refactored.convert('fahrenheit', 'kelvin', -40), 233.15)
        self.assertEqual(conversions_refactored.convert('kelvin', 'celsius', 373.15), 100)
        self.assertEqual(conversions_refactored.convert('kelvin', 'fahrenheit', 310.15), 98.6)

    def test_distance_conversions(self):
        self.assertEqual(conversions_refactored.convert('miles', 'yards', 1), 1760)
        self.assertEqual(conversions_refactored.convert('miles', 'meters', 1), 1609.34)
        self.assertEqual(conversions_refactored.convert('yards', 'miles', 1760), 1)
        self.assertEqual(conversions_refactored.convert('yards', 'meters', 1), 0.91)
        self.assertEqual(conversions_refactored.convert('meters', 'miles', 1609.34), 1)
        self.assertEqual(conversions_refactored.convert('meters', 'yards', 0.9144), 1)

    def test_self_to_self_conversions(self):
        self.assertEqual(conversions_refactored.convert('celsius', 'celsius', 100), 100)
        self.assertEqual(conversions_refactored.convert('fahrenheit', 'fahrenheit', 32), 32)
        self.assertEqual(conversions_refactored.convert('kelvin', 'kelvin', 273.15), 273.15)
        self.assertEqual(conversions_refactored.convert('miles', 'miles', 1), 1)
        self.assertEqual(conversions_refactored.convert('yards', 'yards', 5), 5)
        self.assertEqual(conversions_refactored.convert('meters', 'meters', 42), 42)

    def test_invalid_conversions(self):
        with self.assertRaises(conversions_refactored.ConversionNotPossible):
            conversions_refactored.convert('celsius', 'miles', 100)

        with self.assertRaises(conversions_refactored.ConversionNotPossible):
            conversions_refactored.convert('fahrenheit', 'yards', 32)

        with self.assertRaises(conversions_refactored.ConversionNotPossible):
            conversions_refactored.convert('meters', 'kelvin', 100)


if __name__ == "__main__":
    test_convertCelsiusToKelvin()
    test_convertCelsiusToFahrenheit()
    test_convertFahrenheitToCelsius()
    test_convertFahrenheitToKelvin()
    test_convertKelvinToCelsius()
    test_convertKelvinToFahrenheit()
    unittest.main()