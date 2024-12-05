def load_data(filepath):
    with open(filepath) as f:
        return f.read()


def parse_rules(data):
    rules = {}
    for row in data.splitlines():

        try:
            (key, val) = row.split("|")
            key = int(key)
            val = int(val)
            if key not in rules:
                rules[key] = set([val])
            else:
                rules[key].add(val)

        except ValueError:
            break

    return rules


def parse_page_list(data):
    pagelist = []
    start = False
    for row in data.splitlines():
        # scan for break between rules and data
        if row == "":
            start = True
            continue
        elif start == False:
            continue
        # collect data
        pagelist.append([int(n) for n in row.split(",")])
    return pagelist


# data = load_data("data/day5_sample.txt")
data = load_data("data/day5.txt")


pagelists = parse_page_list(data)
rules = parse_rules(data)

print(rules)
print(pagelists)

goodlists = []
badlists = []
goodlist_middle_num_total = 0
badlist_middle_num_total = 0

#######################################################
for lst in pagelists:

    goodlist = True

    for i, pg in enumerate(lst):
        if pg in rules:
            if len(rules[pg].intersection(lst[:i])) > 0:
                goodlist = False

    if goodlist:
        goodlists.append(lst)
    else:
        badlists.append(lst)

# Count the middle numbers of good lists
for gl in goodlists:
    index = len(gl) // 2
    goodlist_middle_num_total += gl[index]

print(f"total middle nums from good lists: {goodlist_middle_num_total}")


##################################################### part 2


def good_list(lst):
    for i, pg in enumerate(lst):
        if pg in rules:
            if len(rules[pg].intersection(lst[:i])) > 0:
                return False
    return True


print(badlists)

for badlist in badlists:
    while not good_list(badlist):
        for i, pg in enumerate(badlist):
            if pg in rules:
                if len(rules[pg].intersection(badlist[:i])) > 0:
                    badlist.insert(0, badlist.pop(i))

# Count the middle numbers of good lists
for gl in badlists:
    index = len(gl) // 2
    badlist_middle_num_total += gl[index]

print(f"total middle nums from BAD lists: {badlist_middle_num_total}")
