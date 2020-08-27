# ordem de procedência:
# 1. ()
# 2. ** - potência
# 3. * / // % (// = divisão inteira, sem vírgula, % = resto da divisão) - A resolução é de quem aa

n1 = int(input('Manda um número: '))
n2 = int(input('Manda outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# end = '' faz com que não quebre a linha no próximo print 
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ') # :.3f formata o float para 3 casas decimais
print('Divisão inteira {} e potência {}'.format(di, e))
