import random
import itertools

# 1. Convert grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams

# 2. Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

# 3. Solve chickens and rabbits puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None

# 4. Filter prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# 5. All permutations of a string
def string_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]

# 6. Reverse words in a sentence
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

# 7. Check for 3 next to 3
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# 8. Check for 007 in order
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# 9. Volume of a sphere
def volume_of_sphere(radius):
    return (4/3) * 3.141592653589793 * (radius ** 3)

# 10. Unique elements in a list
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# 11. Check palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# 12. Histogram
def histogram(lst):
    for num in lst:
        print('*' * num)

# 13. Guess the number game
def guess_the_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

# 14. Importing and using functions
if __name__ == "__main__":
    print(grams_to_ounces(100))
    print(fahrenheit_to_celsius(212))
    print(solve(35, 94))
    print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
