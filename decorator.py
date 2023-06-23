def decor(func):
    def wrapper(*args, **kwargs):
        print("The execution of argument function is statred here....")
        result = func(*args, **kwargs)
        print("The execution of argument function is completed")
    return wrapper


@decor
def summation(*args):
    sum = 0
    for i in args:
        sum = +i
    print(sum)


summation(1, 2, 3, 4)
