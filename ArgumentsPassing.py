import sys

print("\n")

print(sys.argv)

print("\n")

for argument in sys.argv:
    if sys.argv.index(argument) == 0:
        print("This is the file name: " + argument)
    else:
        print("This is an argument: " + argument)

print("\n")

for index, argument in enumerate(sys.argv[1:]):
    print("Argument " + str(index) + ": " + argument)