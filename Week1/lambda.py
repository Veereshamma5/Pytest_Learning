"""
def square(a):
    return a * a


result = square(5)
print(result)

"""
from functools import reduce

var = lambda a: a * a
result = var(3)
print(result)
res = var(8)
print(res)

# Filter, map and reduce

"""def is_even(n):
    return n % 2 == 0


nums = [1, 2, 3, 4, 5, 6, 7]

evens = list(filter(is_even, nums))

print(evens)"""

list_num = [10, 2, 3, 4, 5, 6, 7, 8, 9, 0]
even_num = list(filter(lambda a: a % 2 == 0, list_num))
print("List of even numbers are", even_num)

#doubles the even_numbers
doubles = list(map(lambda n: n*n, even_num))
print(doubles)

# Print squares of odd numbers
odd_num = list(filter(lambda a: a % 2 != 0, list_num))
print("odd numbers are", odd_num)
#Add all values in the list
square_odd = reduce(lambda x, y: x + y, odd_num)
print("Addition of all values:", square_odd)
