names = ['ramiro', 'jose', 'agustina', 'monica']

def compare_length(c1, c2):
	if len(c1) < len(c2): return -1
	return 1 if len(c1) > len(c2) else 0

print(
	sorted(names, cmp=compare_length)
)