
def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)

Result = Factorial(6)
print(Result)


# def factorial(n):
#     if n < 0:
#         return "error."
#     elif n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
#
#
# print(factorial(5))