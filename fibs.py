def fib(n, holder={}):
    holder[0] = 0
    holder[1] = 1
    if n not in holder:
        holder[n] = fib(n - 1) + fib(n - 2)
    return holder[n]


print([fib(i) for i in range(100)])
