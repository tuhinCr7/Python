number = []
for i in range(3):
    user_input = int(input(f'Enter {1+i}th number'))
    number.append(user_input)
print(number)

if number[0] > number[1] and number[0] > number[2]:
    print(f"Greatest {number[0]}")
elif number[1] > number[0] and number[1] > number[2]:
    print(f"Greatest {number[1]}")
else:
    print(f"Greatest {number[2]}")
