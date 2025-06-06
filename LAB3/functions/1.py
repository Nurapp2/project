#Write a function called calculate_factorial that takes a positive integer as a parameter and returns its factorial (use recursion)
num = int(input())
def calculate_factorial(num):
    if num == 0:
        return 1
    return num*calculate_factorial(num-1)
result = calculate_factorial(num)
print(result)   