


def calcular(multiplicador):
	def multiplicar(numero):
		return multiplicador * numero
	return multiplicar


duplicar = calcular(2)
triplicar = calcular(3)
print(
	sum(dict(map(lambda x: (f"{x+1}",x**2),range(duplicar(1000)))))
		)
print(triplicar(5))