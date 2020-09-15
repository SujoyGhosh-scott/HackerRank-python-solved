'''
n = int(input())
t = n
j = 1
s = 0
i = 0

while(i < t):
    s += j*n
    j *= 10
    n -= 1
    i += 1

print(s)
'''
N = int(input())
for i in range(1, N+1):
    print(i, end="")
