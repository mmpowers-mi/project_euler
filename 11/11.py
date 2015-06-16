# Project Euler
# Problem 11
# Created by Marcus Powers, June 14th, 2015

# main() definition--------------------------------------------------------
def main():
    # Constants
    FILENAME = "11.txt"
    SIZE = 20
    ADJLEN = 4

    # Data Structures
    grid = []

    # Read in numbers one line at a time
    instr = FILENAME
    with open(instr, "r") as fi:
        for line in fi:
            vals = map(int, line.split())
            grid.append(vals)

    # Work our way through, skipping any checks that exceed boundaries
    max = 0
    for x in range(SIZE):
        for y in range(SIZE):
            # Horizontal
            if x < SIZE - ADJLEN:
                s = 1
                for i in range(ADJLEN):
                    s *= grid[y][x + i]
                if s > max:
                    max = s
            # Vertical
            if y < SIZE - ADJLEN:
                s = 1
                for i in range(ADJLEN):
                    s *= grid[y + i][x]
                if s > max:
                    max = s
            # Diagonal Up
            if x < SIZE - ADJLEN and y >= ADJLEN:
                s = 1
                for i in range(ADJLEN):
                    s *= grid[y - i][x + i]
                if s > max:
                    max = s
            # Diagonal Down
            if x < SIZE - ADJLEN and y < SIZE - ADJLEN:
                s = 1
                for i in range(ADJLEN):
                    s *= grid[y + i][x + i]
                if s > max:
                    max = s

    # Print final result
    print max
        
# Run program-----------------------------------------------------------
if __name__ == "__main__":
    main()
