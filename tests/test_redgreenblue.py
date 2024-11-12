"""
Build a string manipulator with the following requirements:
- converts inputs to lower case for string input
- remove a defined pattern from the string input
"""  

from string_modules.string_manipulator import StringManipulator


def support():
    pass

def test_convert_lower_case():
    #ARRANGE
    stringmanipulator = StringManipulator()
    #ACT
    result = stringmanipulator.to_lower_case('PYTEST')
    #ASSERT
    assert result == 'pytest'

def test_convert_lower_case_dynamic():
    #ARRANGE
    stringmanipulator = StringManipulator()
    #ACT
    result = stringmanipulator.to_lower_case('USB')
    #ASSERT
    assert result == 'usb'

def test_convert_lower_case_wrong_input():
    #ARRANGE
    stringmanipulator = StringManipulator()
    #ACT
    result = stringmanipulator.to_lower_case(55)
    #ASSERT
    assert result == 'Invalid input'

def test_convert_lower_case_mixed_input():
    #ARRANGE
    stringmanipulator = StringManipulator()
    #ACT
    result = stringmanipulator.to_lower_case("55USB-9%#¤ÖÄÅ")
    #ASSERT
    assert result == '55usb-9%#¤öäå'

def test_convert_lower_case_empty_input():
    #ARRANGE
    stringmanipulator = StringManipulator()
    #ACT
    result = stringmanipulator.to_lower_case("")
    #ASSERT
    assert result == "String is empty"