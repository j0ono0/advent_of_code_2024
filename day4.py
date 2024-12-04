import re


def load_data(filepath):
    with open(filepath) as f:
        return f.read()


def out_of_bounds(x, y, data):
    if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):
        return True
    return False


def east(x, y, data):

    if (
        not out_of_bounds(x + 3, y, data)
        and data[y][x] == "X"
        and data[y][x + 1] == "M"
        and data[y][x + 2] == "A"
        and data[y][x + 3] == "S"
    ):
        return True
    return False


def west(x, y, data):

    if (
        not out_of_bounds(x - 3, y, data)
        and data[y][x] == "X"
        and data[y][max(0, x - 1)] == "M"
        and data[y][max(0, x - 2)] == "A"
        and data[y][max(0, x - 3)] == "S"
    ):
        return True

    return False


def north(x, y, data):

    if (
        not out_of_bounds(x, y - 3, data)
        and data[y][x] == "X"
        and data[max(0, y - 1)][x] == "M"
        and data[max(0, y - 2)][x] == "A"
        and data[max(0, y - 3)][x] == "S"
    ):
        return True

    return False


def south(x, y, data):

    if (
        not out_of_bounds(x, y + 3, data)
        and data[y][x] == "X"
        and data[y + 1][x] == "M"
        and data[y + 2][x] == "A"
        and data[y + 3][x] == "S"
    ):
        return True

    return False


def northwest(x, y, data):

    if (
        not out_of_bounds(x - 3, y - 3, data)
        and data[y][x] == "X"
        and data[y - 1][x - 1] == "M"
        and data[y - 2][x - 2] == "A"
        and data[y - 3][x - 3] == "S"
    ):
        return True
    return False


def northeast(x, y, data):

    if (
        not out_of_bounds(x + 3, y - 3, data)
        and data[y][x] == "X"
        and data[y - 1][x + 1] == "M"
        and data[y - 2][x + 2] == "A"
        and data[y - 3][x + 3] == "S"
    ):
        return True

    return False


def southwest(x, y, data):

    if (
        not out_of_bounds(x - 3, y + 3, data)
        and data[y][x] == "X"
        and data[y + 1][x - 1] == "M"
        and data[y + 2][x - 2] == "A"
        and data[y + 3][x - 3] == "S"
    ):
        return True

    return False


def southeast(x, y, data):

    if (
        not out_of_bounds(x + 3, y + 3, data)
        and data[y][x] == "X"
        and data[y + 1][x + 1] == "M"
        and data[y + 2][x + 2] == "A"
        and data[y + 3][x + 3] == "S"
    ):
        return True

    return False


# data = [list(char) for char in load_data("data/day4.txt").split()]
data = [list(char) for char in load_data("data/day4_sample.txt").split()]

count = 0

for y in range(len(data)):
    for x in range(len(data[0])):

        count += (
            east(x, y, data)
            + west(x, y, data)
            + north(x, y, data)
            + south(x, y, data)
            + northwest(x, y, data)
            + northeast(x, y, data)
            + southwest(x, y, data)
            + southeast(x, y, data)
        )

print(count)


# Part 2
x_count = 0


def l_to_r(x, y, data):
    if out_of_bounds(x - 1, y - 1, data) or out_of_bounds(x + 1, y + 1, data):
        return False


x_strs = ["MSAMS", "SSAMM", "MMASS", "SMASM"]

for y in range(len(data)):
    for x in range(len(data[0])):

        if data[y][x] == "A" and not (
            out_of_bounds(x - 1, y - 1, data) or out_of_bounds(x + 1, y + 1, data)
        ):
            # test for X-MAS
            test_str = "".join(
                data[y - 1][x - 1]
                + data[y - 1][x + 1]
                + data[y][x]
                + data[y + 1][x - 1]
                + data[y + 1][x + 1]
            )

            if test_str in x_strs:
                x_count += 1

print(x_count)


print("-" * 20)
print("Advent of Code 2024: Day 4")
print(f"XMAS appearances: {count}")
print(f"X-MAS appearance: {x_count}")
print("-" * 20)
