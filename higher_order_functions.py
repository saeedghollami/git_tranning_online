#map(func, iter)
r = list(map(lambda x: x ** 2, list(range(0, 10, 2))))


circle_areas = [3.56773, 5.57668, 4.00912, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, [2]*len(circle_areas)))

def f(x, y, z):
	return x + y + z


r = list(map(lambda x, y, z: x + y - z, [1, 2, 3, 4], [1, 3, 4, 5], [8, 3, 7, 3]))
print(r)