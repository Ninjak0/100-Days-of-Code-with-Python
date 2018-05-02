
# ---Manipulating lists---
numlist = [1, 2, 3, 4, 5]
print(numlist)

numlist.reverse()
print(numlist)

numlist.sort()
print(numlist)

for num in numlist:
    print(str(num))

mystring = "julian"
l = list(mystring)
print(l)
print(l[0])
print(l[4])

print(l.pop())
print(l)
l.insert(5, "n")
print(l)

l[0] = "b"
print(l)

del(l[0])
print(l)
l.insert(0, "m")
print(l)

print(l.pop(2))
print(l)

l.append("s")
print(l)



# ---Immutability and Tuples---

mystring = "julian"
l = list(mystring)
t = tuple(mystring)
print(l, t)

l[0] = "t"
print(l)

# t[0] = "b"   # This returns an error
# print(t)

for letter in t:
    print(letter)

# ---Creating and parsing dictionaries---

pybites = {"julian": 30, "bob": 33, "mike": 32}

people = {}

people["julian"] = 30
print(people)
people["bob"] = 103
print(people)

print(people.keys())
print(people.values())
print(people.items())

for x in people.items():
    for y in x:
        print(y)

for key, value in pybites.items():
    print("The key is", key, "and the value is", value)