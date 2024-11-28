# Problem 6
# Sang Park

points = []

# Reading points from file
point = open('points.txt', 'r')
lines = point.readlines()
for line in lines:
    points.append(line.strip().split(","))

point.close()

# Calculate squared distance from origin and sort by that
distances = []
for coordinate in points:
    name = coordinate[0]
    x = float(coordinate[1])
    y = float(coordinate[2])
    z = float(coordinate[3])
    
    squared_distance = x**2 + y**2 + z**2
    distances.append((name, squared_distance))

# Function to return squared distance for sorting
def get_squared_distance(point_distance):
    return point_distance[1]

# Sort points by distance from origin
distances.sort(key=get_squared_distance)

print("Points sorted by squared distance from origin (closest first):")
for point_name, squared_dist in distances:
    print(f"{point_name}: Squared Distance = {squared_dist}")

# Find the closest point to the origin
closest_squared_distance = distances[0][1]
closest_points = []
for name, dist in distances:
    if dist == closest_squared_distance:
        closest_points.append(name)

print("\nClosest point(s) to the origin:")
for name in closest_points:
    print(name)

# Part 2: Finding the two closest points to each other

# Function to approximate square root using the Babylonian method
def approximate_sqrt(value, tolerance=1e-7):
    if value == 0:
        return 0
    guess = value / 2
    while abs(guess * guess - value) > tolerance:
        guess = (guess + value / guess) / 2
    return guess

# Function to calculate the Euclidean distance between two points without math.sqrt()
def calculate_distance(point1, point2):
    x1, y1, z1 = float(point1[1]), float(point1[2]), float(point1[3])
    x2, y2, z2 = float(point2[1]), float(point2[2]), float(point2[3])
    
    squared_distance = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    return approximate_sqrt(squared_distance)

min_distance = float('inf')
closest_pair = ()

# Compare every pair of points
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = calculate_distance(points[i], points[j])
        if dist < min_distance:
            min_distance = dist
            closest_pair = (points[i][0], points[j][0])

print(f"\nThe two closest points to each other are: {closest_pair[0]} and {closest_pair[1]}")
print(f"Distance between them: {min_distance}")
