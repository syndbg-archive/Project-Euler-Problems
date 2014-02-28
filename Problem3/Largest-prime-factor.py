# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# IMPORTS
from math import sqrt

# FUNCTIONS
def largestPrimeFactor(number):
    largestFactor = 0
    factor = 2
    product = 1

    while product != number:
        if number % factor == 0:
            largestFactor = factor
            product *= factor

        factor += 1

    return largestFactor

# main
def main():
    print(largestPrimeFactor(600851475143))

# PROGRAM RUN
main()