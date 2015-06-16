# Project Euler
# Problem 14
# Created by Marcus Powers, June 12th, 2015

# main() definition--------------------------------------------------------
def main():
    # Constants
    SIZE = 1000000

    # Data Structures
    dists = [0 for _ in range(SIZE)]
    max = 0

    # Loop through and calculate results
    for i in range(SIZE):
        if dists[i]:
            continue
        seen = [(i, 0)]
        v = i + 1
        dist = 1
        # Calculate the distance
        while v != 1:
            # Follow Collatz algorithm
            if v % 2 == 0:
                v /= 2
            else:
                v = (3 * v) + 1
            dist += 1
            if v == 1:
                break
            # If we see a value we also need to calculate, cache it
            if v <= SIZE:
                if dists[v - 1]:
                    dist += dists[v - 1]
                    break
                else:
                    seen.append((v - 1, dist))
        # Finally, set the new value(s)
        for (n, d) in seen:
            dists[n] = dist - d

    # Find longest distance from calculated values
    final = 0
    ld = 0
    for x in range(SIZE):
        if dists[x] > ld:
            ld = dists[x]
            final = x + 1

    # Print final result
    print final


# Run program--------------------------------------------------------------
if __name__ == "__main__":
    main()
