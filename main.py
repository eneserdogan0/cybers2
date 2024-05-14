import math

def get_point():
    try:
        x, y = map(float, input("Noktanın değerlerini (x y) giriniz: ").split())
        return x, y
    except ValueError:
        print("Geçersiz giriş lütfen geçerli bir sayı giriniz.")
        return get_point()


points = []
while True:
    point = get_point()
    points.append(point)
    another_point = input("Başka bir nokta değerleri eklemek ister misiniz? (E/H): ")
    if another_point.lower() != "e":
        break


def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


distances = []
for i, p1 in enumerate(points):
    for p2 in points[i+1:]:
        distance = euclidean_distance(p1, p2)
        distances.append(distance)


min_distance = min(distances)
print(f"Min mesafe: {min_distance:.2f}")
