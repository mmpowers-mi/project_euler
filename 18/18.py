# Project Euler
# Problem 18/67
# Created by Marcus Powers, June 14th, 2015

# main() definition--------------------------------------------------------
def main():
    # Constants
    FILENAME = "../67/67.txt"
    ROWS = 100

    # Data Structures
    nums = [[0 for _ in range(ROWS)] for _ in range(ROWS)]
    cums = [[0 for _ in range(ROWS)] for _ in range(ROWS)]

    # Read in numbers one line at a time
    instr = FILENAME
    with open(instr, "r") as fi:
        for line in fi:
            vals = map(int, line.split())
            j = len(vals)
            for i in range(j):
                nums[j - 1][i] = vals[i]
                cums[j - 1][i] = vals[i]

    # Work our way through from bottom to top
    for j in range(ROWS - 2, -1, -1):
        for i in range(j + 1):
            if cums[j + 1][i] > cums[j + 1][i + 1]:
                cums[j][i] += cums[j + 1][i]
            else:
                cums[j][i] += cums[j + 1][i + 1]

    # Print final result
    print cums[0][0]
        
# Run program-----------------------------------------------------------
if __name__ == "__main__":
    main()
