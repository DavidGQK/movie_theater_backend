def fib(index: int):
    numbers = [0]
    if index < 0:
        return numbers
    prev, current = 0, 1
    for _ in range(index):
        prev, current = current, current + prev
        numbers.append(prev)
    return numbers

# print(fib(5))

class FibMemoryless:
    def __init__(self, index: int):
        self.index = index
        self.prev = 0
        self.current = 1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.index:
            self.counter += 1
            if self.counter != 1:
                self.prev, self.current = self.current, self.current + self.prev
            return self.prev
        raise StopIteration

# fib_it = FibMemoryless(7)
# for _ in fib_it:
#     print(_)

import datetime

def fib_gen(index: int):
    if index < 0:
        return []
    
    prev, current = 0, 1
    yield prev
    for _ in range(index-1):
        prev, current = current, current + prev
        yield prev

# for _ in fib_gen(8):
#     print(_)


# current = datetime.datetime.now()
# sum(fib(1_00_000))
# print(datetime.datetime.now() - current)

# current = datetime.datetime.now()
# sum(FibMemoryless(1_00_000))
# print(datetime.datetime.now() - current)

# current = datetime.datetime.now()
# sum(fib_gen(1_00_000))
# print(datetime.datetime.now() - current)



# def simple_generator():
#     yield 1
#     yield 2
#     return 3

# gen = simple_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))


# numbers = [1, 2, 3]
# def func():
#     for item in numbers:
#         yield item
    
# for item in func():
#     print(item)



numbers = [1, 2, 3]
def func():
    yield from numbers
    
for item in func():
    print(item)
