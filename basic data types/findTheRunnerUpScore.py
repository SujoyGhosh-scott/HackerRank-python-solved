n = int(input())

inp = list(map(int, input().split()))

m = max(inp)
runner_up = -2147483648

for i in range(n):
    if(inp[i] > runner_up and inp[i] < m):
        runner_up = inp[i]

print(runner_up)
