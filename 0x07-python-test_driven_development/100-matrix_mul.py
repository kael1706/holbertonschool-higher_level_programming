#!/usr/bin/python3
"""
this is the module 100-matrix_mul.
this module have the following functions:
matrix_mul(m_a, m_b): multiplies 2 matrices.
"""


def matrix_mul(m_a, m_b):
    if isinstance(m_a, list) is False:
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list) is False:
        raise TypeError("m_b must be a list")
    if len(m_a) is 0 or m_a is None:
        raise ValueError("m_a can't be empty")
    if len(m_b) is 0 or m_b is None:
        raise ValueError("m_b can't be empty")
    m_a_row_size = 0
    only_one_time = False
    m_a_rows_count = 0
    for r in m_a:
        m_a_rows_count = m_a_rows_count + 1
        if isinstance(r, list) is False:
            raise TypeError("m_a must be a list of lists")
        if len(r) is 0 or r is None:
            raise TypeError("m_a can't be empty")
        if only_one_time is False:
            m_a_row_size = len(r)
            only_one_time = True
        tmp = len(r)
        if m_a_row_size != tmp:
            raise TypeError("each row of m_a must be of the same size")
        for c in r:
            if isinstance(c, (int, float)) is False:
                raise TypeError("m_a should contain only integers or floats")
    only_one_time = False
    m_b_row_size = 0
    m_b_rows_count = 0
    for r in m_b:
        m_b_rows_count = m_b_rows_count + 1
        if isinstance(r, list) is False:
            raise TypeError("m_b must be a list of lists")
        if len(r) is 0 or r is None:
            raise TypeError("m_b can't be empty")
        if only_one_time is False:
            m_b_row_size = len(r)
            only_one_time = True
        tmp = len(r)
        if m_b_row_size != tmp:
            raise TypeError("each row of m_a must be of the same size")
        for c in r:
            if isinstance(c, (int, float)) is False:
                raise TypeError("m_b should contain only integers or floats")
    if m_a_row_size is m_b_rows_count:
        new_m = [] 
        for i in range(m_a_rows_count):
            new_m.append([0] * m_b_row_size)
        for ra in range(m_a_rows_count):
            for cb in range(m_b_row_size):
                for rb in range(m_b_rows_count):
                        new_m[ra][cb] += m_a[ra][rb] * m_b[rb][cb]
        return new_m
    else:
        raise ValueError("m_a and m_b can't be multiplied")
