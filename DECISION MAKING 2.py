import math

data = [
    [True, "Hot", "High", "No"],
    [True, "Hot", "High", "No"],
    [False, "Hot", "High", "Yes"],
    [False, "Cool", "Normal", "Yes"],
    [False, "Cool", "Normal", "Yes"],
    [True, "Cool", "High", "No"],
    [True, "Hot", "High", "No"],
    [True, "Hot", "Normal", "Yes"],
    [False, "Cool", "Normal", "Yes"],
    [False, "Cool", "High", "Yes"]
]

attributes = ["Q1", "Q2", "Q3"]

def entropy(rows):
    yes = 0
    no = 0

    for row in rows:
        if row[3] == "Yes":
            yes += 1
        else:
            no += 1

    total = len(rows)
    result = 0

    if yes > 0:
        p = yes / total
        result -= p * math.log2(p)

    if no > 0:
        p = no / total
        result -= p * math.log2(p)

    return result

def information_gain(rows, column):
    total_entropy = entropy(rows)
    values = set(row[column] for row in rows)

    weighted_entropy = 0

    for value in values:
        subset = [row for row in rows if row[column] == value]

        weighted_entropy += (
            len(subset) / len(rows)
        ) * entropy(subset)

    return total_entropy - weighted_entropy

total_entropy = entropy(data)

print("Total Entropy =", round(total_entropy, 4))
print()

gains = []

for i in range(3):
    gain = information_gain(data, i)
    gains.append(gain)

    print(attributes[i], "Information Gain =", round(gain, 4))

print()

max_gain = max(gains)
best_attribute = attributes[gains.index(max_gain)]

print("Best Attribute =", best_attribute)
print("Highest Information Gain =", round(max_gain, 4))
