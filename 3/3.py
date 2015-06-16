# Project Euler
# Problem 3
# Created by Marcus Powers, June 14th, 2015

# main() definition-------------------------------------------------------
def main():
    # Constants
    VALUE = 600851475143

    # Get factors
    factors = factor(VALUE)
    print "factored"

    # Determine largest prime factor
    max = 0
    for fac in factors:
        if prime(fac) and fac > max:
            max = fac
    
    # Print result
    print max
    

# factor(n) definition----------------------------------------------------
def factor(n):
    # Return a list of all factors of n
    factors = []
    i = 1
    while True:
        if i > n / i:
            break
        if not n % i:
            factors.append(i)
            factors.append(n / i)
        i += 1
    return factors

# prime(n) definition-----------------------------------------------------
def prime(n):
    # Determines primality of a number
    return len(factor(n)) == 2


# Run program-------------------------------------------------------------
if __name__ == "__main__":
    main()
