import math

data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"]
]

attributes = ["Outlook", "Temperature", "Humidity", "Wind"]

def entropy(rows):
    yes = 0
    no = 0

    for row in rows:
        if row[4] == "Yes":
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
        weighted_entropy += (len(subset) / len(rows)) * entropy(subset)

    return total_entropy - weighted_entropy

total_entropy = entropy(data)

print("Total Entropy =", round(total_entropy, 4))
print()

for i in range(4):
    gain = information_gain(data, i)
    print(attributes[i], "Information Gain =", round(gain, 4))

print()

gains = []
for i in range(4):
    gains.append(information_gain(data, i))

max_gain = max(gains)
best_attribute = attributes[gains.index(max_gain)]

print("Best Attribute =", best_attribute)
print("Highest Information Gain =", round(max_gain, 4))
