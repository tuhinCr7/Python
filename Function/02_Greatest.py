def great(x, y, z):
    if (x > y and x > z):
        print(f"{x} is greatest")
    elif (y > x and y > z):
        print(f"{y} is greatest")
    else:
        print(f"{z} is greatest")


x, y, z = map(int, input("Enter three number :").split())
great(x, y, z)
