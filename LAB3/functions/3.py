#Write a function called get_max that takes three parameters (a, b, and c) and returns the maximum of the three.
a = int(input())
b = int(input())
c = int(input())
def get_max(a,b,c):
    return max(a,b,c)
maxx = get_max(a,b,c)
print(maxx)