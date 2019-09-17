# David Markham
# 17/09/2019
# This program will perform the Collatz operation.

def collatz(n):
    while n > 1: #Keep looping until we reach 1. 
        print(n, end=' ')
        if (n % 2):
            # n is odd multiply by three and add one.
            n = 3*n + 1
        else:
            # n is even divide by two
            n = n//2
    print(1, end='')
 
# Ask the user to input a positive integer.
n = int(input('Please enter a positive integer: '))
print('Sequence: ', end='') # Print the sequence until 1 is reached.
collatz(n)