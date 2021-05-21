def fib(n: int) -> int:
    """Return the `n` th fibonacci number for positive `n` """
    if 0<= n<=1:
        return n
    result = None
    n_minus1, n_minus2 = 1,0
    for f in range(n-1):
        result = n_minus2 + n_minus1 #c = b+a
        n_minus2 = n_minus1         #b =a
        n_minus1 = result           #a = c
    return result

for i in range(1,25):
    print(fib(i))