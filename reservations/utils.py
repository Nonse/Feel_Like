import itertools
import math

# Basic reference data (e.g. client or invoice No.) 1 2 3 4 5 6
# Weights from right to left 1 3 7 1 3 7
# The sums arrived at are added together 1+6+21+4+15+42 = 89
# The following number ending in zero 90
# from which the added sum is subtracted -89
# Difference = check digit 1
# http://goo.gl/hBEASf <<- check ref number (nordea)

def make_referencenumber(number):
    sum = 0.0;
    weigths = itertools.cycle([7, 3, 1])

    for n in reversed(number):
        sum += int(n) * weigths.next()

    difference = int((math.ceil(sum / 10) * 10) - sum)

    return number + str(difference)
