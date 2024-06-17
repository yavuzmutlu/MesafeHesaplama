import math

points = [(30, 40), (70, 90), (1,1), (5,5)]
distances = []

def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

for i in range(len(points)-1):
    distance = euclideanDistance(points[i], points[i+1])
    distances.append(distance)
    
min_distance = min(distances)
print("En kısa mesafe:", min_distance)