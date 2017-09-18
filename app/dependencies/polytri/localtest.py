from polytri import *

for triangle in triangulate([[0, 0], [0, 5], [5, 5], [5, 0]]):
    print("Triangle:")
    for point in triangle:
        print("{0}, {1}".format(point[0], point[1]))