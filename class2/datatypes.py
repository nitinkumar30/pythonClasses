# Text - str

name = "Nitin"
print(name)

# Numeric - int, float, complex

a = 23
print(a)

a = 23.56
print(a)

a = 4j
print(a)
b = 4 + 3j
print(b)

c = 4 + 3j
print(c)

# Sequence - list, tuple, range

l = ['Nitin', 'Yash', 'Anji']
print(l)

t = (1, 2, 3)
print(t)

r = range(6)
# range(starting_index, ending_index, increment)
print(r)
# for i in r:
#     print(i)

# Mapping - dictionary

d = {'name': 'Nitin', 'age': 23, 'clg': 'AJU'}
print(d)

# Set - set, frozenset

s = {1, 2, 3, 4}
print(s)

f = ({1, 2, 3, 4}, {5, 6, 7, 8})
print(f)

# Boolean - bool

print(1 == 2)  # False
print(1 == 1)  # True

# Binary - bytes, bytearray, memoryview
h = "Hello"
print(type(h))
b = b"Hello"
print(type(b))
print(b)

b_ = bytearray(4)
print(type(b_), b_)
b__ = bytearray(b)
print(b__, type(b__))

m = memoryview(bytes(4))
print(m, type(m))

# Nonetype - None

nitin = None
print(nitin, type(nitin))
