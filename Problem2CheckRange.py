# Daniel L
# 8/18/23
# Problem 2 Python function to check whether a number is in a given range(1-10).

def check_number_in_range(number):
    if 1 <= number < 10:
        print(f"{number} is in the range (1, 10)")
    else:
        print(f"{number} is not in the range (1, 10)")

def main():
    number = int(input("Enter a number: "))
    check_number_in_range(number)

if __name__ == "__main__":
    main()
