#coding: utf-8

import sys

# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
	for j in xrange(len(alist)):
		for i in xrange(len(alist)-1):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	return alist

# Esse metodo recebe e valor para ser dado o troco e uma lista com os tipos de moedas possiveis
# e retorna o numero minimo de moedas possiveis em que o troco pode ser dado

# Caso o valor não possa ser alcançado pela combinação de moedas o valor -1 é retornado Ex: valor = 11  moedas = {5, 10, 25}
# Assuma que existe uma quantidade infinita de cada tipo de moeda
def retorna_minimo_moedas(valor, tipos_moedas):
	tipos_moedas.sort(reverse = True)
	
	total_moedas = 0
	i = 0	
	
	while(valor > 0):
		
		if(i == len(tipos_moedas)):
			return -1
		
		while(valor - tipos_moedas[i] >= 0):
			total_moedas = total_moedas + 1
			valor = valor - tipos_moedas[i]
		
		i = i + 1
		
	return total_moedas

