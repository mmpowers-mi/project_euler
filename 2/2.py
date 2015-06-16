# Project Euler
# Problem 2
# Created by Marcus Powers, June 12th, 2015

# main() definition--------------------------------------------------------
def main():
    # Constants
    FIBMAX = 34

    # Data Structures
    fiblist = [0 for x in range(FIBMAX)]
    fiblist[0] = 0
    fiblist[1] = 1
    for i in range(2, FIBMAX):
        fiblist[i] = fiblist[i - 1] + fiblist[i - 2]

    final = 0
    # Add up all even fib numbers
    for i in range(0, FIBMAX, 3):
        print fiblist[i]
        final += fiblist[i]

    # Output final result
    print final


# Run program--------------------------------------------------------------
if __name__ == "__main__":
    main()
