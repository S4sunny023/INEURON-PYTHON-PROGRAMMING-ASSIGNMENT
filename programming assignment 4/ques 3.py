n = int(input("enter how many numbers you want in this series : "))
a = 0
b = 1
if n == 1:
    print(a)
else:
    print(a)
    print(b)

for i in range(2,n):
    c = a+b
    a = b
    b = c
    print(c)