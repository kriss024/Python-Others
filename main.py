import sys

def main():
    args = len(sys.argv) - 1

    if args > 0:
        print("The script was called with %i arguments" % (args))

        for pos in range(1, args + 1):
            arg = sys.argv[pos]
            print("Argument %i is %s" % (pos, arg))

    else:
        print("No command line arguments provided")

if __name__ == "__main__":
    main()