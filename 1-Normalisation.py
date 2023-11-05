def min_max_scaling(data):
    min_val = min(data)
    max_val = max(data)
    scaled_data = [(x - min_val) / (max_val - min_val) for x in data]
    return scaled_data

def z_score_normalization(data):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean)**2 for x in data) / len(data)) ** 0.5
    normalized_data = [(x - mean) / std_dev for x in data]
    return normalized_data

def decimal_scaling(data):
    max_value = max(abs(x) for x in data)
    num_digits = len(str(max_value))
    scaled_data = [x / (10 ** num_digits) for x in data]
    return scaled_data

# Example usage
#data = [5, 10, 15, 20, 25]
data= [float(val) for val in input("Enter the data (comma-separated): ").split(',')]
min_max_scaled = min_max_scaling(data)
z_score_normalized = z_score_normalization(data)
decimal_scaled = decimal_scaling(data)

print(f"Min-Max Scaled Data: {min_max_scaled}")
print(f"Z-Score Normalized Data: {z_score_normalized}")
print(f"Decimal Scaled Data: {decimal_scaled}")
