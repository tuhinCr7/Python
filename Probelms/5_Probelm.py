# Find the year is leapyear or not

year = int(input("Enter any year : "))
if year % 4 == 0:
    print(f"{year} is leapyear !")
else :
    print(f"{year} is not leapyear !")