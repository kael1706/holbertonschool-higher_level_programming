#!/usr/bin/python3
def remove_char_at(str, n):
    word = list(str)
    if n >= 0 and len(word) > n:
        del word[n]
    return("".join(word))

print(remove_char_at("Holberton School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
