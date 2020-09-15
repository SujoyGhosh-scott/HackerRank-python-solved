n = int(input())
dict = {}
for i in range(n):
    inputs = list(map(str, input().split()))
    marks = []
    marks = [float(inputs[j]) for j in range(1, 4)]
    dict[inputs[0]] = marks

name = input()

avg = sum(dict[name])/3

print(round(avg, 2))
