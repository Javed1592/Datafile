import time

def time_it(func):

    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + "took " +str((end-start)*1000) + "Min")
        return result
    return inner

@time_it
def square(num):
    r = []
    for i in num:
        r.append(i*i)
    return r

@time_it
def cube(num):
    r = []
    for i in num:
        r.append(i*i*i)
    return r


num = range(1,10000)
lst1 = square(num)
lst2 = cube(num)

print(lst1)
print(lst2)

