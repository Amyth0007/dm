def calculate_mean(data):
    return sum(data) / len(data)

def calculate_slope(x, y, x_mean, y_mean):
    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x)))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(len(x)))
    return numerator / denominator

def calculate_intercept(x_mean, y_mean, slope):
    return y_mean - slope * x_mean

def linear_regression(x, y):
    x_mean = calculate_mean(x)
    y_mean = calculate_mean(y)

    slope = calculate_slope(x, y, x_mean, y_mean)
    intercept = calculate_intercept(x_mean, y_mean, slope)

    return slope, intercept

# Take user inputs for x and y
# Given data
#x = [10, 92, 15, 10, 16, 11, 16]
#y = [95, 80, 10, 50, 45, 98, 38]
x = [float(val) for val in input("Enter values of x (comma-separated): ").split(',')]
y = [float(val) for val in input("Enter values of y (comma-separated): ").split(',')]

slope, intercept = linear_regression(x, y)

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"y = {slope} x + {intercept}")
