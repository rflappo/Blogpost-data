words = ['Hello', 'world', 'my', 'name', 'is', 'Ramiro', "and", 'I', 'live', 'in', 'Argentina']

# Non-pythonic
concatenated = ''
for word in words:
	concatenated += word


# Pythonic
concatenated = "".join(words)