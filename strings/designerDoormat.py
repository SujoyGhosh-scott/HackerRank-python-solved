n, m = map(int, input().split())
list = []
a = (m - 3) // 2
b = 1
c = '.|.'

z = n//2
# create upper half
for i in range(z):
    s = ''
    for j in range(a):
        s += '-'
    for j in range(b):
        s += '.|.'
    for j in range(a):
        s += '-'
    a -= 3
    b += 2
    list.append(s)

s = ''
o = (m-7)//2
for i in range(o):
    s += '-'
s += 'WELCOME'
for i in range(o):
    s += '-'

list.append(s)

a = 3
b = n-2

for i in range(z):
    s = ''
    for j in range(a):
        s += '-'
    for j in range(b):
        s += '.|.'
    for j in range(a):
        s += '-'
    a += 3
    b -= 2
    list.append(s)

for i in range(len(list)):
    print(list[i])
