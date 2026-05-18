# example.py

def compute_average(data):
    return sum(data) / len(data)        # potential division by zero


def find_name_by_id(idx):
    names = ["Alice", "Bob", "Charlie"]
    return names[idx]               # BUG: no bounds check


def main():
    numbers = [10, 20, 30, 40]

    print("Average:", compute_average(numbers))

    idx = int(input("Enter ID (0-2): "))
    name = find_name_by_id(idx)
    print("Name:", name)

    value = 42
    ref = value
    del value
    print("Value after delete:", ref)  # subtle: still works (good discussion point)


if __name__ == "__main__":
    main()
