#! /usr/bin/env python3

def fizzBuzz(n):
    for i in range(0,n):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0 and i%5!=0:
            print('Fizz')
        elif i%3!=0 and i%5==0:
            print('Buzz')
        else:
            print(i)

a = input('hello: ')
fizzBuzz(a)
