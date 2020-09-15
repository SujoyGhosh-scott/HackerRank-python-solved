a, b, c, n = int(input()), int(input()), int(input()), int(input())
'''
for i in range(0, a+1):
    for j in range(0, b+1):
        for k in range(0, c+1):
            x = []
            if(i+j+k == n):
                continue
            x.append(i)
            x.append(j)
            x.append(k)
            #print(i, j, k)
            # print(x)
            list.append(x)
'''
list = [[i, j, k] for i in range(0, a+1)
        for j in range(0, b+1)
        for k in range(0, c+1) if(i+j+k != n)]

print(list)
