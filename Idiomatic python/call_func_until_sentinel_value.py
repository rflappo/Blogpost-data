# idiomatic way
blocks = []
while True:
	block = f.read(32)
	if not block:
		break
	blocks.append(block)


# idiomatic way
blocks = []
for block in iter(partial(f.read, 32). ''):
	blocks.append(block)