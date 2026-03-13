def F_to_C(f):
    return 5*(f-32)/9


f = float(input("Enter temparature in Farehite : "))
c = F_to_C(f)
print(f'celcius of {f} F is {round(c, 2)}C')
