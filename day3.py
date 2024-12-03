import re


def load_data(filepath):
    with open(filepath) as f:
        return f.read()


def extract_muls(data):
    muls = re.findall(r"(?<=mul\()[0-9]+,[0-9]+(?=\))", data)
    muls = [[int(n) for n in m.split(",")] for m in muls]
    return muls


def filter_data(data):
    return re.sub(r"don't\(\).*?do\(\)", "--filtered--", data, flags=re.DOTALL)


# raw_data = load_data("data/day3_sample_b.txt")
raw_data = load_data("data/day3.txt")
muls = extract_muls(raw_data)

total = sum([a * b for a, b in muls])

fil_data = filter_data(raw_data)
print(fil_data)
fil_muls = extract_muls(fil_data)
fil_total = sum([a * b for a, b in fil_muls])

print(total)
print(fil_total)

print("-" * 20)
print("Advent of Code 2024: Day 3")
print(f"Sum of Mul: {total}")
print(f"Filtered sum of Mul: {fil_total}")
print("-" * 20)
