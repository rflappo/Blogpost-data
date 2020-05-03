vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(len(vowels)):
	print(vowels[i])

for j in range(len(vowels)-1, -1, -1):
	print(vowels[i])


names = ['amelie', 'eragorn', 'ivan', 'olaf', 'ulises', 'extra-name']

for vowel, name in zip(vowels, names):
	print(vowel, " ---> ", name)