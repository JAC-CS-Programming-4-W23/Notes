import sys

# reading from a file instead of stdin
with open("inputs.txt", "r") as file:
    sys.stdin = file
    while True:
        try:
            x = input("Enter something ")
            print(x)
        except EOFError:
            break
sys.stdin = sys.__stdin__

input("press enter to continue")

# writing to a file instead of console
with open("outputs.txt", "w") as file:
    sys.stdout = file
    print("Hello There")
sys.stdout = sys.__stdout__

print("All done")
