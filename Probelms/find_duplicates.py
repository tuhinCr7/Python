num = [12, 33, 44, 33, 55, 55, 5, 12]
duplicate = []
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] == num[j]:
            duplicate.append(num[i])
print(duplicate)
