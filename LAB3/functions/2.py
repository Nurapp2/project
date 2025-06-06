#Write a function called reverse_string that takes a string as a parameter and returns its reverse.
str = input()
def reverse_string(str):
    return str[::-1]
rev = reverse_string(str)
print(rev)