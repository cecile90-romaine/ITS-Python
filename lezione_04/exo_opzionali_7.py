# Esercizio_7:

"""
Roman Numeral Conversion:

    Create a function that converts a given integer to its Roman numeral representation.
    Handle numbers from 1 to 3999.
    Use a combination of string manipulation and conditional statements to build the Roman numeral.

"""
# Function to convert an integer to a Roman numeral
def int_to_roman(num: int) -> str:
    # List of Roman numeral values in descending order
    val: list[int] = [
        1000, 900, 500, 400,
        100, 90,  50,  40,
        10, 9,    5,   4, 1
    ]
    
    # Corresponding Roman numeral symbols for the values
    syms: list[str] = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    
    # Resulting Roman numeral string to be built
    roman: str = ""

    # Iterate through the values and symbols
    for i in range(len(val)):
        # While the current value can be subtracted from num
        while num >= val[i]:
            roman += syms[i]     # Append the corresponding symbol
            num -= val[i]        # Subtract the value from num

    # Return the constructed Roman numeral
    return roman

# Example usage of the function
print(int_to_roman(1994))  # Output: MCMXCIV