# Project Euler
# Problem 8
# Created by Marcus Powers, June 13th, 2015

# main() definition--------------------------------------------------------
def main():
    # Constants
    DIGLEN = 1000
    ADJLEN = 13
    FILENAME = "8.txt"

    # Data Structures
    # Note: prods[j] represents the product of the following ADJLEN integers starting at (and including) j
    prods = [1 for _ in range(DIGLEN)]
    
    # Read in digits
    instr = FILENAME
    fi = open(instr, "r")
    contents = list(str(fi.read()))
    contents.pop()
    fi.close()
    digits = map(int, contents)

    # Loop through the digits
    prod = 1
    recalc = True
    for i in range(DIGLEN - ADJLEN):
        if i >= DIGLEN - ADJLEN:
            break
        if recalc:
            recalc = False
            prod = 1
            for k in range(ADJLEN):
                prod *= digits[i + k]
                if not digits[i + k]:
                    recalc = True
                    i += k + 1
                    break
        if recalc:
            continue
        prods[i] = prod
        if not digits[i + ADJLEN]:
            recalc = True
            i += ADJLEN + 1
        else:
            prod /= digits[i]
            prod *= digits[i + ADJLEN]

    # Find the largest result
    max = 0
    for i in range(DIGLEN):
        if prods[i] > max:
            max = prods[i]

    # Output final result
    print max


# Run program--------------------------------------------------------------
if __name__ == "__main__":
    main()
