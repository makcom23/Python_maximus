points = [10, 20, 30, 60, 58]
vectors=[]
for i in range(len(points)):
    A = points[i]
    B = points[(i + 1) % len(points)]  # замыкаем кольцо
    vectors.append([A, B])
print(vectors)

