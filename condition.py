# age = 18
# if (age>17):
#     print('Você é maior, já pode dirigir.')
# print('Fim;')
# idade=int(input('insert your age'))
# if (idade>=16 and idade<18):
#     print('allowed to vote')
# elif idade<16:
#     print('just study')
# else:
#     print('allowed to drive')
# a=float(input('insert number 1\n'))
# b=float(input('insert number 2\n'))
# if a>b:
#     print('n1 (%.1f) é maior que n2 (%.1f)' %(a,b))
# elif b>a:
#     print('n2 (%.1f) é maior que n1 (%.1f)' %(b,a))
# else:
#     print('são iguais.')
# b=int(input('insert number'))
# if b>0:
#     print('{} é positivo.'.format(b))
# elif b<0:
#     print('{} é negativo.'.format(b))
# else:
#     print('{} é neutro.'.format(b))
# s=float(input('Qual o salário? R$'))
# q=(s+((15/100)*s))
# d=(s+((10/100)*s))
# c=(s+((5/100)*s))
# if s<500:
#     print('Salário de R${0} com reajuste de 15%: R${1}'.format(s,q))
# elif s==500 or s<1000:
#     print('Salário de R${0} com reajuste de 10%: R${1}'.format(s,d))
# else:
#     print('Salário de R${0} com reajuste de 5%: R${1}'.format(s,c))

# b=input('DIGA: ')
# print(b.upper())
# vog=['a','e','i','o','u']
# letra=input('insert letter')
# letra=letra.lower()
# if letra in vog:
#     print('vogal')
# else:
#     print('consoante')



# n1=float(input('Nota: '))
# n2=float(input('Nota: '))
# md=(n1+n2)/2
# if md==10:
#     print('Aprovado com distinção.')
# elif md<7:
#     print('Reprovado')
# else:
#     print('Aprovado')

# n1=float(input('Insert number: '))
# n2=float(input('Insert number: '))
# n3=float(input('Insert number: '))
# if n1>n2 and n2>n3:
#     print('Maior: {}\nMenor: {}'.format(n1,n3))
# elif n2>n1 and n3>n1:
#     print('Maior {}\nMenor: {}'.format(n2,n1))
# elif n3>n1 and n1>n2:
#     print('Maior {}\nMenor: {}'.format(n3,n2))

n1=int(input('Insert number: '))
n2=int(input('Insert number: '))
n3=int(input('Insert number: '))
if n1>n2 and n2>n3:
    print('{},{},{}'.format(n1,n2,n3))
elif n1>n3 and n3>n2:
    print('{},{},{}'.format(n1,n3,n2))
elif n2>n1 and n1>n3:
    print('{},{},{}'.format(n2,n1,n3))
elif n2>n3 and n3>n1:
    print('{},{},{}'.format(n2,n3,n1))
elif n3>n1 and n1>n2:
    print('{},{},{}'.format(n3,n1,n2))
elif n3>n2 and n2>n1:
    print('{},{},{}'.format(n3,n2,n1))