import math

def euclideanDistance(point1, point2):
    """İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon"""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Kullanıcıdan noktaları alma
num_points = int(input("Kaç tane nokta gireceksiniz?: "))
points = []
for _ in range(num_points):
    x, y = map(int, input("Noktayı (x, y) formatında girin: ").split(","))
    points.append((x, y))

distances = []

# Her nokta çifti arasındaki mesafeyi hesaplayıp listeye ekleme
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bulma
min_distance = min(distances)

print("Tüm noktalar arasındaki minimum Öklid mesafesi:", min_distance)
