# Project Euler
# Problem 13
# Created by Marcus Powers, June 12th, 2015

# main() definition--------------------------------------------------------
def main():
    # Constants
    FILENAME = "13.txt"

    # Read in numbers
    instr = FILENAME
    fi = open(instr, "r")
    print "file opened"
    contents = fi.read()
    print "file read"
    fi.close()
    print "file closed"
    nums = map(int, contents.split())
    print "file split"

    # Add nums together
    print "calculating..."
    final = sum(nums)

    # Print final result
    print final
        
# Run program-----------------------------------------------------------
if __name__ == "__main__":
    main()
