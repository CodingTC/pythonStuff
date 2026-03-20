

def foo():
    y = 10
    def bar(x):
        return x + y
    return bar

aVar = foo()

print(aVar(7))


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3

aString = "Hello World"

temp = aString.split()

print(temp)

dog = "".join(temp)

print(dog)
