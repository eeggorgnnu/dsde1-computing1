'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
def inc(a):
    a += 1
    print(a)


# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    result = a + 1
    return result# hint this is incomplete


# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    result = a + b
    return result 


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    ans = sum(a,b)
    result = inc_return(ans)
    return result


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    even_odd = bool((int(a)%2) == 0)

    return even_odd


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    string = phrase
    for i in range (repeat-1):
        string += phrase
    # hint: you can add strings together 
    # in order to concatenate them
    return string

number = sum_inc(3,4)
print(number)
print(is_even(number))

repeat = string_repeat("hello",4)
print(repeat)