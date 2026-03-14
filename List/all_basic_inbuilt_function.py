# add anything using append
li = [3, 2, 4, 5, 2]
li.append(7)
print(li)

# let's try to add two or more number at a time
li.extend([6, 9])
print(li)

# let's insert something anything specific index

li.insert(2,44)
print(li)

# let's remove anyhting

li.remove(44)
print(li)

# let's remove from the last using pop

li.pop()
print(li)

# 

li.index(3)
print(li)

#  let's sort it

li.sort()
print(li)

# let'r reverse

li.reverse()
print(li)

#  let's sort by ascending order 

li.sort(reverse=True)
print(li)
