vowels = ['a', 'e', 'i', 'o', 'u']

for vowel in vowels:
	print(vowel)

for index, vowel in enumerate(vowel):
	print(index, " ---> ", vowel)

for vowel in reversed(vowels):
	print(vowel)


names = ['amelie', 'eragorn', 'ivan', 'olaf', 'ulises', 'extra-name']
n = min(len(vowels), len(names))

for i in range(n):
	print(vowels[i], ' ---> ', names[i])