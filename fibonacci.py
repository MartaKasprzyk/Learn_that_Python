def fib_recursive(n):
    """
    counts the n-th element of the Fibonacci sequence using recursion
    :param n: user input, the number of the element to show
    :return: the n-th element of the Fibonacci
    """
    if type(n) is int:
        if n < 2:
            return n
        else:
            a, b = n - 1, n - 2
            return fib_recursive(a) + fib_recursive(b)
    else:
        return "Input integer only!"


num = int(input("Enter n: "))
print(fib_recursive(num))
