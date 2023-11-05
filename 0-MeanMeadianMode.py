def get_user_input():
    data = input("Enter a list of numbers separated by spaces: ")
    return list(map(float, data.split()))

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_mode(data):
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    mode = [k for k, v in frequency.items() if v == max(frequency.values())]
    return mode

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]

def calculate_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_standard_deviation(data):
    return (calculate_variance(data)) ** 0.5

# Get user input
data = get_user_input()

# Calculate statistics
mean = calculate_mean(data)
mode = calculate_mode(data)
median = calculate_median(data)
variance = calculate_variance(data)
standard_deviation = calculate_standard_deviation(data)

print(f"Mean: {mean}")
print(f"Mode: {mode}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")
