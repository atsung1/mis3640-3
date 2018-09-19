def factorio(n):
    if n > 2:
        return n * factorio(n-1)
    elif n == 2:
        return 2
    elif n == 1 or 1:
        return 1
    else:
        return 'error'

#test
print(factorio(10))
print(factorio(2))
print(factorio(1))
print(factorio(0))
print(factorio(-10))