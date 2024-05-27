# d=input('Digite uma letra: ')
# if d=='F':
#     print('Feminino')
# elif d=='M':
#     print('Masculino')
# else:
#     print('Sexo inválido')  

# l=input('Digite uma letra: ')
# if l!='a' or l!='e' or l!='i' or l!='o' or l!='u':
#     print('%s é consoante. '%l)
# else: 
#     print('%s é vogal. ')

n1=float(input('Digite a nota: '))
n2= float(input('Digite a nota: '))
media=(n1+n2)/2
if media>=7:
    print('{0:.2} Aprovado'.format(media))
elif media<7:
    print('{0:.2} Reprovado'.format(media))
elif media==10:
    print('Aprovado com distinção')

# a=int(input('Insira um número: '))
# b=int(input('Insira um número: '))
# c=int(input('Insira um número: '))
# if a>b>c or a>c>b:
#     print('Maior: %i'%a)
# elif b>a>c or b>c>a:
#     print('Maior: %i'%b)
# elif c>a>b or c>b>a:
#     print('Maior: %i'%c)