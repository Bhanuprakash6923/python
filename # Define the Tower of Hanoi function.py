# Define the Tower of Hanoi function
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disc 1 from {source} to {target}")
        return
    # Move top n-1 discs from source to auxiliary
    tower_of_hanoi(n-1, source, target, auxiliary)
    # Move the nth disc from source to target
    print(f"Move disc {n} from {source} to {target}")
    # Move the n-1 discs from auxiliary to target
    tower_of_hanoi(n-1, auxiliary, source, target)

# Input number of disks
n = int(input("Enter the number of disks: "))
print("The moves are:")
tower_of_hanoi(n, 'A', 'B', 'C')