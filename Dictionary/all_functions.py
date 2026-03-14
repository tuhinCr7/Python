#  A dictionary stores data in key-value pairs.

dicts = {
    "name": "Tuhin",
    "department": "cse",
    "Id": 24103096

}
print(dicts)
print(type(dicts))

# for showing keys

print(dicts.keys())

#  for values

print(dicts.values())

#  for every item

print(dicts.items())

#  let's suppose i want to update my id 

dicts.update({'Id':23106063})
print(dicts)


