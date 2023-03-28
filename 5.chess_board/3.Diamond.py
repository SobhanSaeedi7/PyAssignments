#Make a Diamond
size = int(input("Enter size of Diamond : "))

for i in range(size):
        print(" " * (size - i), "♦" * (2 * i + 1))

for i in range(size-2, -1,-1):
        print(" " * (size - i), "♦" * (2 * i + 1))
