# Sample dataset
data = [
    {'outlook': 'sunny', 'temp': 'hot', 'humidity': 'high', 'windy': False, 'play': 'no'},
    {'outlook': 'sunny', 'temp': 'hot', 'humidity': 'high', 'windy': True, 'play': 'no'},
    {'outlook': 'overcast', 'temp': 'hot', 'humidity': 'high', 'windy': False, 'play': 'yes'},
    {'outlook': 'rainy', 'temp': 'mild', 'humidity': 'high', 'windy': False, 'play': 'yes'},
    {'outlook': 'rainy', 'temp': 'cool', 'humidity': 'normal', 'windy': False, 'play': 'yes'},
    {'outlook': 'rainy', 'temp': 'cool', 'humidity': 'normal', 'windy': True, 'play': 'no'},
    {'outlook': 'overcast', 'temp': 'cool', 'humidity': 'normal', 'windy': True, 'play': 'yes'},
    {'outlook': 'sunny', 'temp': 'mild', 'humidity': 'high', 'windy': False, 'play': 'no'},
    {'outlook': 'sunny', 'temp': 'cool', 'humidity': 'normal', 'windy': False, 'play': 'yes'},
    {'outlook': 'rainy', 'temp': 'mild', 'humidity': 'normal', 'windy': False, 'play': 'yes'},
    {'outlook': 'sunny', 'temp': 'mild', 'humidity': 'normal', 'windy': True, 'play': 'yes'},
    {'outlook': 'overcast', 'temp': 'mild', 'humidity': 'high', 'windy': True, 'play': 'yes'},
    {'outlook': 'overcast', 'temp': 'hot', 'humidity': 'normal', 'windy': False, 'play': 'yes'},
    {'outlook': 'rainy', 'temp': 'mild', 'humidity': 'high', 'windy': True, 'play': 'no'}
]

def calculate_entropy(data):
    total = len(data)
    if total == 0:
        return 0

    # Count the occurrences of each class
    class_counts = {}
    for entry in data:
        label = entry['play']
        if label in class_counts:
            class_counts[label] += 1
        else:
            class_counts[label] = 1

    # Calculate entropy
    entropy = 0
    for count in class_counts.values():
        probability = count / total
        if probability > 0:  # Avoid log(0)
            entropy -= probability * (probability**0.5)  # Using square root as base for logarithm
    return entropy

def calculate_information_gain(data, attribute):
    total = len(data)
    if total == 0:
        return 0

    # Calculate the weighted entropy for the given attribute
    weighted_entropy = 0
    attribute_values = set(entry[attribute] for entry in data)
    for value in attribute_values:
        subset = [entry for entry in data if entry[attribute] == value]
        subset_entropy = calculate_entropy(subset)
        subset_weight = len(subset) / total
        weighted_entropy += subset_weight * subset_entropy

    # Calculate information gain
    return calculate_entropy(data) - weighted_entropy

# Example usage
information_gains = {}
for attribute in ['outlook', 'temp', 'humidity', 'windy']:
    information_gain = calculate_information_gain(data, attribute)
    information_gains[attribute] = information_gain

print("Information Gains:")
for attribute, gain in information_gains.items():
    print(f"{attribute}: {gain}")
