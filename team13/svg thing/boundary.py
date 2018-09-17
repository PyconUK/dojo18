points = [(568.2,200.2),
		  (560.7,187.2),
		  (392.3,271.1),
		  (348.8,195.8), 
		  (348.8,195.8), 
		  (345.9,190.8), 
		  (303.3,117.1), 
		  (284.1,128.2), 
		  (312.9,184.8), 
		  (232.1,242.5), 
		  (241.1,258.1), 
		  (325.4,209.3), 
		  (367.8,292.4), 
		  (360.2,483.2), 
		  (429.8,483.2), 
		  (415.3,301.1)]

sides = []


import random

def get_sides(points):
	for i in range(len(points)):
		if i != len(points):
			point1 = points[i]
			point2 = points[i + 1]
		else:
			point1 = points[i]
			point2 = points[0]

		m = (point1[1] - point2[1]) / (point1[0] - point2[0])
		c = point1[1] - m * point1[0]

		sides.append({'m': m, "c": c, 1: point1, 2: point2})

def are_intersecting(side, ray):
	if side[0] == ray[0]:
		return False
	x = (ray['c'] - side['c']) / (side['m'] - ray['m'])
	y = side['m'] * x + side['c']

	if is_on_side(x, y, side):
		return True
	else
		return False

def is_on_side(x, y, side):
	if side[1][0] < side[2][0]:
		if x not in range(side[1], side[2]):
			return False
	else
		if x not in range(side[2], side[2]):
			return False

	if side[1][1] < side[2][1]:
		if y not in range(side[1], side[2]):
			return False
	else
		if y not in range(side[2], side[2]):
			return False

def get_ray(x, y):
	ray = {'m': 0, "c": y}
	return ray

x = random.randint(0, 800)
y = random.randint(0, 600)

def check_in_shape(x, y, points):
	




