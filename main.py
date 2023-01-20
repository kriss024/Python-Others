import sys

def hello(a,b):
    print("Hello and that's your sum: {}".format(a + b))

def main():
    arguments = len(sys.argv) - 1
    if arguments==2:
        print("Number of arguments: {} arguments".format(arguments))
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        hello(a, b)
    else:
        raise ValueError('Two arguments required')

if __name__ == "__main__":
    main()