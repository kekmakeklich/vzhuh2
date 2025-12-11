def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    return 1 if n == 0 else n * factorial(n - 1)
