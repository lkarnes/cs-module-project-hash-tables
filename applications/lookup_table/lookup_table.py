
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v
lookup_table = {}
def slowfun(x, y):
    key = f"{x},{y}"
    if key in lookup_table:
        return lookup_table[key]
    else:
        res = math.pow(x,y)
        res = math.factorial(res)
        res //= (x + y)
        res %= 982451653
        lookup_table[key] = res
        return key



# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
