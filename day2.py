# data_source = "data/day2_sample.txt"
data_source = "data/day2.txt"

reports = []
safe = 0
safe_dampened = 0


def safe_dampened_report(report):

    if safe_report(report):
        return True

    for i in range(len(report)):
        rprt = report.copy()
        rprt.pop(i)
        if safe_report(rprt):
            return True

    return False


def safe_report(report):
    rprt = report.copy()
    i = rprt.pop(0)
    while rprt:
        diff = rprt[0] - i
        if diff < 1 or diff > 3:
            return False
        i = rprt.pop(0)
    return True


# Load data into reports list
with open(data_source) as f:
    for line in f:
        levels = [int(level) for level in line.split()]
        reports.append(levels)


for report in reports:
    # Reverse all reports that are descending (make easier testing)
    if report[0] > report[-1]:
        report.reverse()

    if safe_report(report):
        safe += 1

    if safe_dampened_report(report):
        safe_dampened += 1


print("-" * 20)
print("Advent of Code 2024: Day 2")
print(f"Safe reports: {safe}")
print(f"Safe reports *with* dampening: {safe_dampened}")
print("-" * 20)
