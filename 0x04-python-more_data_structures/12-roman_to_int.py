#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return(0)
    answer = 0
    table = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    roman_string = roman_string.upper()
    size = len(roman_string)
    for idx in range(size):
        tVal = table[roman_string[idx]]
        pos = idx + 1
        nextPos = pos
        if pos != size and table[roman_string[nextPos]] > tVal:
                answer = answer - tVal
        else:
            answer = answer + tVal
    return answer
"""
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))"""
