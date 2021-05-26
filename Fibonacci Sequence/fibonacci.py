def fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect Input")
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci sequence:")
for i in range(20):
    print(fibonacci(i))
