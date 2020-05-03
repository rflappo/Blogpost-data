names = ['Ramiro', 'Lucas', 'Emanuel', 'Alexis']
colores = ['rojo', 'azul', 'amarillo', 'verde', 'rosa']

# Non-idiomatic
n = min(len(names), len(colores))
d = {}
for i in range(n):
	d[names[i]] = colores[i]


# Idiomatic
d = dict(zip(names, colores))