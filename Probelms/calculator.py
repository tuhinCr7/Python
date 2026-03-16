def calculator(x, y):

    expression = input("Enter expression * / + - ")

    if (expression == "+"):
        print(f"Output is : {x+y}")
    elif (expression == "-"):
        print(f"Output is : {x-y}")
    elif (expression == "*"):
        print(f"Output is : {x*y}")
    
    elif (expression == "/"):
        print(f"Output is : {x/y}")

    else:
        print("Invalid Input !")


x = float(input("Enter first values : "))
y = float(input("Enter second values : "))


calculator(x, y)
