num = [12, 33, 44, 55, 5]
evencount = 0
oddcount = 0
for i in range(len(num)):
    if num[i] % 2 == 0:
        evencount += 1
    else:
        oddcount += 1

print("total even :", evencount)
print("total odd :", oddcount)
