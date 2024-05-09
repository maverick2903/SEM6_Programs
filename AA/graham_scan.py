import math
import matplotlib.pyplot as plt

def polar_angle(base, p):
    return math.atan2(p[1] - base[1], p[0] - base[0])

def cross_product(a, b, point):
    return (b[0] - a[0])*(point[1] - a[1]) - (b[1] - a[1])*(point[0] - a[0])

def graham_scan(points):
    start = min(points, key=lambda p: (p[1],p[0]))
    sorted_points = sorted(points, key=lambda p: (polar_angle(start, p),p[0],p[1]))
    hull = []

    for point in sorted_points:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
    return hull

points=[
    (0, 3), 
    (1, 1), 
    (2, 2), 
    (4, 4),
    (0, 0), 
    (1, 2), 
    (3, 1), 
    (3, 3)
]

hull = graham_scan(points)
print(hull) 

x,y=zip(*points)
hx,hy=zip(*hull)
plt.scatter(x,y,color='blue',label='Points')
plt.plot(hx+(hx[0],),hy+(hy[0],),color='red',label="Convex hull")
plt.title("Convex Hull using Graham scan")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()