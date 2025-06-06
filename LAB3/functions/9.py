#Write a function calculate_running_average that takes a series of numbers as input and returns a list containing the running average at each position.
def average(n):
    running = []
    a = 0
    for i, num in enumerate(n, start=1):
        a += num
        av_a = a / i
        running.append(av_a)
    return running

n = list(map(int, input().split()))

res_list = average(n)
print(res_list)