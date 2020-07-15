import math

lookup_table = {}
def inv_rt(n):
    return 1/math.sqrt(n)

def populate_lookup():
    for i in range(1,1001):
        lookup_table[i] = inv_rt(i)

populate_lookup()

