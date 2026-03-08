num = [12, 33, 44, 55, 5]
maximum = num[0]
for i in range(len(num)):
    if num[i] > maximum:
        maximum = num[i]
print(f'Maximum is : {maximum}')
