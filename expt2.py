import math
# fa=float(input('Quantos graus Fahrenheit?'))
# pa=float(5*(fa-32)/9)
# print('%f graus Fahrenheit em graus Celsius: %1.0f'%fa,pa)

# a=int(input('Digite o primeiro número:'))
# b=int(input('Digite o segundo número:'))
# c=float(input('Digite o terceiro número:'))

# pe=float(input('Digite um número:'))
# pr=float(input('Digite um número:'))
# cont1=float((2*pe)/(pr/2))
# pt=float(input('Digite um número:'))
# print('O produto do dobro do primeiro dividido metade do segundo: ',cont1)
# print('Soma do triplo do primeiro com o terceiro: ',(3*pe)+pt)
# print('Terceiro ao cubo: ',(pt)**3)

# alt=float(input('Qual a altura em m? '))
# peso=float(72.7*alt)-58
# print('O peso ideal para a altura {0:.2f}m é: {1:.1f}kg'.format(alt,peso))

# i=int(9)
# while i!=0:
#     i=int(input('Cálculo do peso ideal\nHomem(1) Mulher(2) Sair(0)'))
#     if i==1:
#         alt=float(input('Qual a altura em m? '))
#         peso=float(72.7*alt)-58
#         print('O peso masculino ideal para a altura {0:.2f}m é: {1:.1f}kg'.format(alt,peso))
#     elif i==2:
#         alt=float(input('Qual a altura em m? '))
#         peso=float(62.1*alt)-44.7
#         print('O peso feminino ideal para a altura {0:.2f}m é: {1:.1f}kg'.format(alt,peso))
# print('Fim.')

# peso=float(input('Quantos kg de peixe? '))
# if peso>50:
#     exc=peso-50
#     multa=(peso-50)*4
#     print('Você excedeu o limite de pesca em {0:.2f}kg\nDeverá pagar R${1:.2f} de multa'.format(exc,multa))
# else :
#     print('Bela pescada João, volte sempre!')

# pgm=float(input('Quanto ganha por hora? R$'))
# hpm=float(input('Quantas horas trabalha por mês? '))
# tip=(11/100)*pgm
# inss=(8/100)*pgm
# sin=(5/100)*pgm
# print('Salário bruto: R$',pgm*hpm)
# print('Imposto total (Imposto de Renda): R${0:.2f}'.format(pgm-tip))
# print('Imposto total (INSS): R${0:.2f}'.format(pgm-inss))
# print('Imposto total (Sindicato): R${0:.2f}'.format(pgm-sin))
# print('Salário descontado os impostos: R${0:.2f}'.format((pgm*hpm)-tip-inss-sin))

# area=float(input('Quantos m² serão pintados?'))
# litros=area/3
# lata=math.ceil(litros/18)
# # if litros>=18:
    
# print('Serão necessários {0:.2f}L de tinta, totalizando {1:.0f} latas de tinta.'.format(litros,lata))
# valor=lata*80

# print('\nValor total de {0:.0f} latas de tinta é: R${1:.0f}'.format(lata,valor))

# tam=float(input('Tamanho do arquivo (Mb): '))
# vel=float(input('Velocidade de download: (Mbps): '))
# res=(tam/vel)/60
# print('Tempo total de download em minutos: {0:.2f}'.format(res))

# n1=float(input('Digite o número 1: '))
# n2=float(input('Digite o número 2: '))
# if n1>n2:
#     print('Maior = {0:.0f}\nMenor = {1:.0f}'.format(n1,n2))
# elif n1<n2:
#     print('Maior = {0:.0f}\nMenor = {1:.0f}'.format(n2,n1))
# elif n1==n2:
#     print('Os números {0:.0f} e {0:.0f} são iguais. '.format(n1,n2))

# num=float(input('Digite o número: '))
# if num>0:
#     print(num,' = Positivo')
# elif num<0:
#     print(num,' = Negativo')
# else:
#     print('Zero')





area=float(input('Quantos m² serão pintados?'))
litros=area/3
lata=math.ceil(litros/18)
# if litros>=18:
    
print('Serão necessários {0:.2f}L de tinta, totalizando {1:.0f} latas de tinta.'.format(litros,lata))
valor=lata*80

print('\nValor total de {0:.0f} latas de tinta é: R${1:.0f}'.format(lata,valor))

