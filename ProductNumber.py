def productNumber(number):
    product = 1
    for num in number:
        product *= num
    return product

list = [1,2,3,4,5,6]
Result = productNumber(list)

print(Result)