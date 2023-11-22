"""
Iterators are used to fetch one value at a time.
Lets say if you have a list of 100 values and you want values one value at a time then we use iterators.
To use iterators we need to define two functions-
__iter()__   :: Will give you the object of iter
__next()__   :: Will give you the next object

Instead of defining two functions on our own, then python will give us the Generator.
Generator will give you iterators

Yield is a keyword which makes your function into generator...

"""


# mylist = [10, 20, 30, 40]
# var = iter(mylist)
# print(next(var))
# print(next(var))


class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            var = self.num
            self.num = self.num + 1
            return var
        else:
            raise StopIteration


obj = TopTen()
for i in obj:
    print(i)

"""----------------------"""


def topten():
    yield 5
    yield 3


obj = topten()
print(obj)
print(obj.__next__())
print(next(obj))


# Write a program to get squares of the topten numbers using generator

def topten():
    num = 1
    while num <= 10:
        sq = num * num
        yield sq
        num += 1


obj = topten()
for i in obj:
    print(i)


