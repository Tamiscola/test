print("hello, world")

def new_range(start, stop, step):
    current = start

    while True:
        if step > 0 and current >= stop:
            break
        if step < 0 and current <= stop:
            break
        
        yield current

        current += step


iter = new_range(1, 5, 1)
for i in iter:
    print(i)