def fibonacci(arg):
    if arg == 1:
        return 1
    elif arg == 2:
        return 1
    elif arg > 2:
        value = fibonacci(arg-1) + fibonacci(arg-2)
        return value


print(fibonacci(250))