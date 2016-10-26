#!/usr/bin/env python
# Author : Fouad Teniou
# Date : 27/07/09
# version :2.6
# http://code.activestate.com/recipes/576857-nth-root/

"""
nth-Root program uses generators to compute values' approximations
of a sequence and displays the nth root of a number, once two equal
values are generated consecutively.
"""
from __future__ import generators
from decimal import *


def nthRoot(n, x):
    """ Returns the nth root of a number """

    seq_start = 1.0  # sequence starting value
    counter = 0  # initialize the generator counter to zero

    if x < 0:
        raise ValueError, \
            " Cannot compute a Square root on a negative number"
    elif n == 0:
        raise ValueError, \
            " Cannot compute 0 root of a number"

    while counter < 700:
        yield seq_start  # return nthRoot(x)

        # compute the next sequence term (Xn+1)
        seq_start = 1 / float(n) * (
            (n - 1) * float(seq_start) + x / (float(seq_start) ** (n - 1)))

        counter += 1


while True:

    try:
        # get the nth root number from user
        nth = int(raw_input("Please Enter a nth root (n) : "))
        # get a number from user
        number = int(raw_input("Please Enter a number (x): "))

    except ValueError:
        print "This value is not an integer"

    else:
        break

    print

seq_list = []  # start with an empty list

for i in nthRoot(nth, number):
    seq_list.append(i)  # append the list

    if seq_list.count(i) > 1:
        seq_list.remove(i)

if number == 0:
    # Display nth root(0)
    print "The %s root of %s is : %s" \
          % (nth, number, int(Decimal(repr(i)).normalize()))
else:
    # Display the nth root (x)
    print "The (%s)root of %s is : %s" \
          % (nth, number, Decimal(repr(i)).normalize())



    ###############################################################################

    # >>>
    # >>> The (22552222)root of 22 is : 1.000000137061557
    # >>>
    # >>> The (5) root of 0 is : 0
    # >>> The (2)root of 25 is : 5
    ######################################################################################
