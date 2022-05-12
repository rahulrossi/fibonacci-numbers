def fib(num):
    a = 0   # 1st fibonacci number is 0
    b = 1   # 2nd fibonacci number is 1
    for i in range(num):
        yield a   # We stop the program at a and run the below
        temp = a   # We store a in temp
        a = b    # We store b in a to get new a. If we didn't store a in temp, we would have lost a at this operation.
        b = temp + b    # We add temp and b to get new b and continue the loop

for x in fib(21):
    print(x)
