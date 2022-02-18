#write a python program for fibonacci numbers.

def fib(n):
    x = 0
    y = 1
    z = 0
    count = 1
    while(count<=n):
        print(z)
        count += 1
        x = y
        y = z
        z = x+y
while True :
    n = int(input("Enter the number :"))
    fib(n)
