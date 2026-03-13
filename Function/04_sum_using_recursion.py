def sum(n):
    if(n==1):
        return 1
    else:
        return sum(n-1)+n
n=int(input("enter any number : ")) 
print(f'sum of {n} number is : {sum(n)}')   
