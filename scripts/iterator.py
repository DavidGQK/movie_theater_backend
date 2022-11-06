


# class CyclicIterator:

#     def __init__(self, stop_value: int):
#         self.current = -1
#         self.stop_value = stop_value - 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current < self.stop_value:
#             self.current += 1
#             return self.current
#         self.current = 0
#         return self.current

# cyclic_iterator = CyclicIterator(3)
# for i in cyclic_iterator:
#     print(i)

# class Range2:
#     def __init__(self, stop_value: int):
#         self.current = -1
#         self.stop_value = stop_value - 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current < self.stop_value:
#             self.current += 1
#             return self.current
#         raise StopIteration

# _range = Range2(5)
# for i in _range:
#     print(i) 


import typing


class CyclicIterator:
    def __init__(self, it: typing.Iterable):
        self.it = iter(it)
        self.copy = []
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            x = next(self.it)
            self.copy.append(x)
        except StopIteration:
            if not self.copy:
                print('StopIteration')
                raise StopIteration

            if len(self.copy) == self.idx:
                print('len')
                self.idx = 0

            x = self.copy[self.idx]
            self.idx += 1
        return x

cyclic_iterator = CyclicIterator(range(2))
for i in cyclic_iterator:
    print(i)