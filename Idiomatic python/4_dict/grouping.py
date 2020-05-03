colors = ['red', 'green', 'red', 'blue', 'green', 'yellow', 'red']

# Non-idiomatic
d = {}
for color in colors:
	key = len(color)
	if key not in d:
		d[key] = []
	d[key].append(color)

# Idiomatic
d = dafaultdict(list)
for color in colors:
	key = len(color)
	d[key].append(color)