
# Non-idiomatic way of doing it
def find(seq, target):
	found = False
	for i, value in enumerate(seq):
		if value == target:
			found = True
			break
	if found:
		return i
	return -1

# Idiomatic
def find(seq, target):
	for i, value in enumerate(seq):
		if value == target:
			break
	else:
		return -1
	return i
