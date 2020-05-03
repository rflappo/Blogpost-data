colors = ['red', 'green', 'red', 'blue', 'green', 'yellow', 'red']

# Non-idiomatic

d = {}
for color in colors:
	if color not in d:
		d[color] = 0
	d['color'] += 1

# Idiomatic

d = {}
for color in colors:
	d[color] = d.get(color, 0) + 1

d = defaultdict(int)
for color in colors:
	d[color] += 1