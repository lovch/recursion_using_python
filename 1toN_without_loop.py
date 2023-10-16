import sys

// set this limit according to your requirements
sys.setrecursionlimit(2000)

n = 0

def print_f(n):
    print(n)
    print_f(n+1)

print_f(n)
