"""
Build a string manipulator with the following requirements:
- converts inputs to lower case for string input
- remove a defined pattern from the string input
"""

class StringManipulator:
    def to_lower_case(self, to_lower):
        if not isinstance(to_lower, str):
            return "Invalid input"
        if not to_lower:
            return "String is empty"
        return to_lower.lower()

