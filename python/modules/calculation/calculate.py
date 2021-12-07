def add(*args):
    return sum(args)


def sub(x,y):
    return x-y


def mul(*args):
    result = 1
    for i in args:
      result = result*i
    return result


def div(x,y):
    return x/y
