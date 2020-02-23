def plus(val1, val2):
    return val1 + val2


def minus(val1, val2):
    return val1 - val2


def multiple(val1, val2):
    return val1 * val2


def divide(val1, val2):
    return val1 / val2

print('return_plus:', plus(10, 20))
print('return_minus:', minus(10, 20))
print('return_multiple:', multiple(10, 20))
print('return_divide:', divide(10, 20))

result = divide(minus(10,20), multiple(50,10))
print(result)