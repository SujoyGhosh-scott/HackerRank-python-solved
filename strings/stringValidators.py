s = input()

# any function returns true if
# any one of the iteration returns true
# all functions returns true if
# all iterations returns true

print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
