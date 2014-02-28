# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# FUNCTIONS
def sumMultiplesBelow1000():
    outputSum = 0

    # don't include 1000!
    for number in range(2, 1000):
        if number % 3 == 0 or number % 5 == 0:
            outputSum += number

    return outputSum

# main
def main():
    print("Sum of multiples of 3 and 5 below 1000")
    print(sumMultiplesBelow1000())


# PROGRAM RUN
main()