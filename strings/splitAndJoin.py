def split_and_join(line):
    return line.replace(" ", "-")


'''
    line = line.split(" ")
    str = ""
    for i in range(len(line) - 1):
        str += line[i] + "-"
    str += line[-1]
    return str
'''


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
