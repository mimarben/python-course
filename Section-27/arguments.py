from car import Car


def add(*args):
    # tupple
    print(args[0])
    sum = 0
    for n in args:
        sum = sum + int(n)
    return sum

print(add(1,2,3,4))

print(add(1,2,3,4,5,6,7,8,9,10))

def calc(n, **kwargs):
    #dictonary
    for key,value in kwargs.items():
        print(key,value)            
    print(kwargs["add"])
    n += kwargs["add"]
    print(f'add: {n}')
    n *= kwargs["mul"]
    print(f'mul: {n}')
    n -= kwargs["sub"]
    print(f'sub: {n}')
    return n
calc(2,add=1,sub=2,mul=3)


my_car = Car(maker="Toyota", model="Camry")
print(my_car.maker)

