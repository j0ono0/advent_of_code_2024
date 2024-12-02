data_source = "data/day1.txt"
# data_source = "data/day1_sample.txt"

list_a = []
list_b = []
total_distance = 0
total_similarity = 0

# read data into lists
with open(data_source) as f:
    for line in f:
        a, b = [int(n) for n in line.split()]
        list_a.append(a)
        list_b.append(b)

# Sort lists to compare correct values
list_a.sort()
list_b.sort()

# sum total distance between lists
for a, b in zip(list_a, list_b):
    total_distance += abs(b - a)

# Similarity score
for a in list_a:
    # same = [b for b in list_b if b == a]
    # total_similarity += a * len(same)
    total_similarity += a * list_b.count(a)

print("-" * 20)
print("Advent of Code 2024: Day 1")
print(f"Total distance: {total_distance}")
print(f"Similarity score: {total_similarity}")
print("-" * 20)
