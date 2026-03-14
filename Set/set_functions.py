#  A set is an unordered collection with no duplicate values.

s = {1, 7, 2, 4}
print(type(s))

#  adding in set
s.add(5)
print(s)

#  uning
t = {1, 2, 12, 5}
print(s.union(t))

# intersection means only common data

print(s.intersection(t))
