"""
Problem statement:
Given a list of rational numbers,find their product.

Concept
The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.

>>> reduce(lambda x, y : x + y,[1,2,3])
6

Sample Input 

3
1 2
3 4
10 6

Sample Output 

5 8 (1/2 * 3/4 *10/6)
"""

from fractions import Fraction
from functools import reduce

def product(fracs):
    
    t = reduce(lambda a,b: a*b, fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)