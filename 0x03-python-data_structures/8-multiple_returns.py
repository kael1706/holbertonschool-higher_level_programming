#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == None:
        return (0, None)
    return len(sentence), sentence[0]

"""sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
"""
