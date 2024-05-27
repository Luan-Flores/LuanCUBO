# while True:
#     valor=int(input('Digite o valor 1 ou 0 para encerrar'))
#     if valor==1 or valor==0:
#         print('Valor para sair')
#         break
#     else: 
#         print('valor inválido')  

# a=(int(input('Insert Number\n')))
# b=a
# while True:
#     a -= 1
#     print(a)
#     if a==0:
#         break
# print('\nnúmero de reduções de 1: %i'%b)

v1=2.60
v2=6.0
v3=4.0
ba=0
to=0
me=0
while True:
    a=int(input('O que deseja comprar?\n(1) Banana   R${}\n(2) Tomate   R${}\n(3) Melancia R${}\n(4) Caixa\n(0) Sair\n'.format(v1,v2,v3)))   
    if a==0:
        break
    if a==1:
        ba+=1
    elif a==2:
        to+=1
    elif a==3:
        me+=1
    while a==4:
        tot=(ba*v1)+(to*v2)+(me*v3)
        print('Bananas: {}\nTomates: {}\nMelancias: {}\nTotal: R${}'.format(ba,to,me,tot))
        t=float(input('Troco para quanto? R$'))
        print('Troco: R$%.2f'%(t-tot))
        a=int(input('(1) Voltar ao menu\n'))
        if a==1:
            ba=0
            to=0
            me=0
            
print('Fim')


    