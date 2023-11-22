"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.


try:
       # Some Code....
except:
       # optional block
       # Handling of exception (if required)
else:
       # execute if no  exception
finally:
      # Some code .....(always executed)

"""


def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero, please check once ")
    else:
        print("Your answer is :", result)
    finally:
        # this block is always executed
        # regardless of exception generation.
        print('This is always executed')

    # Look at parameters and note the working of Program


divide(3, 2)
divide(10, 9)
divide(3, 0)
