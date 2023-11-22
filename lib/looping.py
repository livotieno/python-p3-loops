#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
      i=10
    while i >= 0:
        if i == 0:
            print("Happy New Year!")
        else:
            print(i)
        i-=1 

def square_integers(int_list):
    # code goes here!
    pass
    squared_integers = [integer ** 2 for integer in int_list]
    return squared_integers

def fizzbuzz():
    # code goes here!
    pass
    num = 1
   while num <= 100:
        if num % 3 == 0 and num % 5 == 0  :
           print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)
        

