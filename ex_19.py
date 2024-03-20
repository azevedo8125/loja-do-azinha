frase = str(input('Introduza uma frase qualquer:'))

#conta os As que tem na frase
conta_a = frase.count('a')
#encontra o primeiro A na frase
pos_pri_a = frase.find('a')
#encontra o ultimo A na frase
pos_ult_a = frase.rfind('a')
#Apresenta os resultados
print('a frase tem',conta_a,  'As')
print('o primeiro a esta na posição:',pos_pri_a)
print('o ultimo a esta na posição:',pos_ult_a)