def countUp(n):
    i = 0
    while i <= n:
        yield i
        i += 1


g = countUp(5)


for x in countUp(5):
    print(x)

while True:
    try:
        print(next(g))
    except StopIteration:
        break
