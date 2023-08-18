# Daniel L
# 8/18/23
# Problem 3 Python function to multiply all the numbers in a list(5, 2, 7, -1).

def multiplyList(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

num_list = [5, 2, 7, -1]
product = multiplyList(num_list)
print("Product of numbers in the list:", product)
