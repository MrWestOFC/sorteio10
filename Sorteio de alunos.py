#Scrit Em Python criado para algum sorteio
#Script 
#Cruiado por: 
import random

a = ('===============')
print(a)
al1 = str(input ('1° Pessoa: '))
al2 = str(input ('2° Pessoa: '))
al3 = str(input ('3° Pessoa: '))
al4 = str(input ('4° Pessoa: '))
al5 = str(input ('5° Pessoa: '))
al6 = str(input ('6° Pessoa: '))
al7 = str(input ('7° Pessoa: '))
al8 = str(input ('8° Pessoa: '))
al9 = str(input ('9° Pessoa: '))
al10 = str(input ('10° Pessoa: '))
a2 = ('==============')
print(a2)

confirm = str(input ('Confirmar: ?'))
confirm2 = str(input ('Repete a confirmação: '))
	
resp = (al1, al2, al3, al4, al5, al6, al7, al8, al9, al10)
print('O Sorteado é: {}'.format(random.choice(resp)))