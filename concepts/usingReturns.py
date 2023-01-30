def add(a, b):
    result = a + b
    return result

result = add(3, 4)
print(result) # Output: 7


def is_even(number):
    if number % 2 == 0: # If the number is even
        return True
    else:
        return False

result = is_even(5)
print(result) # Output: False

result = is_even(6)
print(result) # Output: True
