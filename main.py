def print_towers(towers):
    num_disks = max(len(tower) for tower in towers)
    for level in range(num_disks - 1, -1, -1):
        for tower in towers:
            if level < len(tower):
                print(f"{'*' * tower[level]:^7}", end='')
            else:
                print(f"{'|':^7}", end='')
        print()


def move_disk(source, target, towers):
    if not towers[source]:
        print("Invalid move! Source tower is empty.")
        return False
    elif towers[target] and towers[source][-1] > towers[target][-1]:
        print("Invalid move! Cannot place a larger disk on top of a smaller one.")
        return False
    else:
        disk = towers[source].pop()
        towers[target].append(disk)
        return True


def tower_of_hanoi(num_disks, num_sticks):
    towers = [[] for _ in range(num_sticks)]
    towers[0] = list(range(num_disks, 0, -1))

    while True:
        print_towers(towers)

        source = int(input("Enter source stick (1, 2, 3): ")) - 1
        target = int(input("Enter target stick (1, 2, 3): ")) - 1

        if source < 0 or source >= num_sticks or target < 0 or target >= num_sticks:
            print("Invalid input! Stick number out of range.")
            continue

        if move_disk(source, target, towers):
            print("Move successful!")
        else:
            print("Move failed. Try again.")

        if towers[-1] == list(range(num_disks, 0, -1)):
            print("Congratulations! You've solved the Tower of Hanoi!")
            break


if __name__ == "__main__":
    num_disks = 5
    num_sticks = 3
    tower_of_hanoi(num_disks, num_sticks)
