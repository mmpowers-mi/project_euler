# Project Euler
# Problem 10
# Created by Marcus Powers, June 14th, 2015

# main() definition--------------------------------------------------------
def main():
    # Constants
    FILENAME = "10.txt" # List of all primes < 2,000,000
    MAX = 2000000

    # Read in primes
    instr = FILENAME
    with open(instr, "r") as fi:
        primes = fi.read()
        answer = sum(map(int, primes.split()))
        print answer
        
# Run program-----------------------------------------------------------
if __name__ == "__main__":
    main()
