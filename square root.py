
def square_root(number, precision=0.00001):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number")

    guess = number / 2 if number >= 1 else 1

    while abs(guess * guess - number) > precision:
        guess = (guess + number / guess) / 2

    return guess
num = 64
result = square_root(num)
print(f"The square root of {num} is approximately {result}")
