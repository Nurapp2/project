#You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an argument and returns only prime numbers from the list.
def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [a for a in numbers if is_prime(a)]

numbers = list(map(int, input().split()))
primes = filter_prime(numbers)
print(primes)