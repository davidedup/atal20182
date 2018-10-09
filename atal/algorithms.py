# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
	for index in range(1, len(alist)):

		currentvalue = alist[index]
		position = index

		while position > 0 and alist[position-1] <= currentvalue:
			alist[position] = alist[position-1]
			position = position-1

		alist[position] = currentvalue
	return alist
