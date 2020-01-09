#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_l = []
    for pos in range(list_length):
        answer = 0
        try:
            answer = my_list_1[pos] / my_list_2[pos]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            n_l.append(answer)
    return n_l
