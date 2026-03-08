num = [12, 33, 44, 33, 55, 5, 12]
largest = num[0]
second_largest = num[1]
for i in range(len(num)):
    if num[i] > largest:
        second_largest = largest
        largest = num[i]
print("second largest :", second_largest)
