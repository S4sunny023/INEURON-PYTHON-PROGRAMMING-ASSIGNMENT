n = int(input("enter the number :"))
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
print(fact(n))

'''n = int(input("enter the number :"))
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
print(fact(n))
'''