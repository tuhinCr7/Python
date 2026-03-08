num = [12, 34, 53, 65, 77, 5]

for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] + num[j] == 17:
            print(i, j)
