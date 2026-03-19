

def foo():
    y = 10
    def bar(x):
        return x + y
    return bar

aVar = foo()

print(aVar(7))
