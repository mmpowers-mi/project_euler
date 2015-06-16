# Project Euler
# Problem 1
# Created by Marcus Powers, June 12th, 2015

# main() definition--------------------------------------------------------
def main():
    # Constants
    MAX = 1000
    MAX3 = 333
    MAX5 = 199
    MAX15 = 66

    # Find all multiples of 3 and 5
    threes = [3 * x for x in range(1, MAX3 + 1)]
    fives = [5 * x for x in range(1, MAX5 + 1)]
    fifteens = [15 * x for x in range(1, MAX15 + 1)]

    # Add them together and remove overlap
    final = sum(threes) + sum(fives) - sum(fifteens)

    # Output final result
    print final


# Run program--------------------------------------------------------------
if __name__ == "__main__":
    main()
