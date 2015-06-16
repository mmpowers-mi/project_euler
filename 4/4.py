# Project Euler
# Problem 4
# Created by Marcus Powers, June 14th, 2015

# main() definition-----------------------------------------------------
def main():
    # Loop through all possible combos
    max = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            v = x * y
            if pal(v) and v > max:
                max = v

    # Print final answer
    print max

# pal(n) definition-----------------------------------------------------
def pal(n):
    s = str(n)
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


# Run program-----------------------------------------------------------
if __name__ == "__main__":
    main()
