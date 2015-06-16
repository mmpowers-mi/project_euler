# Project Euler
# Problem 15
# Created by Marcus Powers, June 12th, 2015

# main() definition--------------------------------------------------------
def main():
    # Constants
    SIZE = 20

    # Data Structures
    paths = [[0 for _ in range(SIZE + 1)] for _ in range(SIZE + 1)]

    # Run DP pathfinder
    for i in range(SIZE, -1, -1):
        # First calculate the row
        x = i
        y = i
        while x >= 0:
            if y == SIZE:
                paths[x][y] = 1
            else:
                paths[x][y] = paths[x + 1][y] + paths[x][y + 1]
            x -= 1
        # Then the column
        x = i
        y = i - 1
        while y >= 0:
            if x == SIZE:
                paths[x][y] = 1
            else:
                paths[x][y] = paths[x + 1][y] + paths[x][y + 1]
            y -= 1

    # Final result is value stored at initial point (number of paths)
    final = paths[0][0]

    # Print final result
    print final


# Run program--------------------------------------------------------------
if __name__ == "__main__":
    main()
