

def slow_fib(n):
    if n <= 1:
        return n
    return slow_fib(n-1) + slow_fib(n-2)

cache = {}
def fast_fib(n):
    if n <=1:
        return n
    if n not in cache:
        cache[n] = fast_fib(n-1) + fast_fib(n-2)
    return cache[n]

print(fast_fib(45))
print('done')
print(fast_fib(45))
print('done')
print(cache)