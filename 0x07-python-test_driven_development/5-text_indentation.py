#!/usr/bin/python3

"""
this is a module 5-text_indentation.

this module have the following functions:
text_indentation: split the text by "." and "?"
    then print print each item
"""


def text_indentation(text):
    if text is None or not text:
        raise ValueError
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    new_text = text.strip().replace('?', '?***').replace(".", '.***')
    new_text = new_text.replace(':', ':***').split("***")
    size = len(new_text)
    jump = False
    for idx, item in enumerate(new_text):
        jump = False
        new_text[idx] = item.strip()
        for ch in item:
            if ch in "?.:":
                jump = True
        if jump is True:
            print(new_text[idx], end="\n\n")
        else:
            print(new_text[idx], end="")
