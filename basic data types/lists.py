n = int(input())
list1 = []
for i in range(n):
    inputs = list(map(str, input().split()))
    # inputs = raw_input().strip().split(" ")
    if inputs[0] == "insert":
        list1.insert(int(inputs[1]), int(inputs[2]))
    elif inputs[0] == "print":
        print(list1)
    elif inputs[0] == "remove":
        list1.remove(int(inputs[1]))
    elif inputs[0] == "append":
        list1.append(int(inputs[1]))
    elif inputs[0] == "sort":
        list1.sort()
    elif inputs[0] == "pop":
        list1.pop()
    elif inputs[0] == "reverse":
        list1.reverse()
