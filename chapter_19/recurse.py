def recurse(n):
    if n < 0:
        return

    print(n)
    recurse(n - 1)
