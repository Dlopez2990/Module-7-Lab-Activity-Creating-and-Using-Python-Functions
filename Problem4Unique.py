# Daniel L
# 8/18/23
# Problem 4 takes a list of numbers and returns a new list with unique elements of the first list.

def uniqueElements(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

original_list = [1, 3, 3, 3, 6, 2, 3, 5]
unique_list = uniqueElements(original_list)
print("Original list:", original_list)
print("List with unique elements:", unique_list)
