# def far(temp):
#     return ((temp-32)*(5/9))
# temp=float(input('How many °C : __'))
# print('Temp: {0:.1f}'.format(far(temp)),end=' °C\n')
# def soma(x,y):
#     result=x+y
#     return result
# a=int(input('number 1: '))
# b=int(input('number 2: '))
# res=soma(a,b)
# print(res)

# def invert(nome,sobre):
#     inv=sobre+', '+nome
#     return inv
# nome=input('Nome: ')
# sobre=input('Sobrenome: ')
# print (invert(nome,sobre))
def par(x):
    if(x%2)==0:
        return True
while True:
    num=float(input('Digite um número: '))
    if par(num):
        print('é par')
    else:
        print('é ímpar')