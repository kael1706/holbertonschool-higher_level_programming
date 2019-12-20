#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        c = 0
        w = ''
        for k, v in a_dictionary.items():
            if v > c:
                c = v
                w = k
        return w
    return None
"""
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
"""
