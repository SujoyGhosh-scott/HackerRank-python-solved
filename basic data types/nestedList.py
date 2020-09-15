n = int(input())
list1 = []
# list2 is for storing only the scores
list2 = []
# getting the user input in list
for i in range(n):
    x = []
    a, b = input(), float(input())
    x.append(a)
    x.append(b)
    list2.append(b)
    list1.append(x)

# getting the second lowest score
m = min(list2)
sec = 2147483647
secInd = 0
for i in range(n):
    if(list2[i] < sec and list2[i] > m):
        sec = list2[i]
        secInd = i

# getting name of all the students having secongd lowest score in list3
list3 = []
for i in range(n):
    if(list1[i][1] == list2[secInd]):
        list3.append(list1[i][0])

# sorting list3 in alphabetical order
list3.sort()

for i in list3:
    print(i)
