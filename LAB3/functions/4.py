#Write a function called is_even that takes an integer as a parameter and returns True if it's even and False otherwise.
def is_even(a):
    return a % 2 == 0
a = int(input())
if is_even(a):
    print(True)
else:
    print(False)