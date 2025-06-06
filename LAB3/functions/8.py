#Write a recursive function fibonacci that returns the nth Fibonacci number.
def formula(n):
    if n <= 1:
        return n
    return formula(n - 1) + formula(n - 2)

n = int(input())
cnt = formula(n)
print(cnt)