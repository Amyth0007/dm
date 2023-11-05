# Euclidean Distance
def euclidean_distance(point1, point2):
    return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

# Manhattan Distance
def manhattan_distance(point1, point2):
    return sum(abs(x - y) for x, y in zip(point1, point2))

# Minkowski Distance
def minkowski_distance(point1, point2, p):
    return sum(abs(x - y) ** p for x, y in zip(point1, point2)) ** (1/p)

# Example usage
#point1 = [1, 2, 3]
#point2 = [4, 5, 6]
point1 = [float(val) for val in input("Enter point1 (comma-separated): ").split(',')]
point2 = [float(val) for val in input("Enter point1 (comma-separated): ").split(',')]
# Calculate distances
euclidean_dist = euclidean_distance(point1, point2)
manhattan_dist = manhattan_distance(point1, point2)
minkowski_dist = minkowski_distance(point1, point2, p=3)

print(f"Euclidean Distance: {euclidean_dist}")
print(f"Manhattan Distance: {manhattan_dist}")
print(f"Minkowski Distance (p=3): {minkowski_dist}")
