#!/usr/bin/python3
def remove_char_at(str, n):
    word = list(str)
    if n >= 0 and len(word) > n:
        del word[n]
    return("".join(word))
