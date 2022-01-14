def inspect(func):
    def wrapper(*args):
        print(f"Running {func.__name__}")
        val = func(*args)
        return val
    return wrapper

@inspect
def combine(*numbs):
    sum = 0
    for n in numbs:
        sum += n
    return sum

#print(str(combine(1,2,3,4)))

print(combine(1,2,3))