# while True:
#     valor=int(input('Digite o valor 1 ou 0 para encerrar'))
#     if valor==1 or valor==0:
#         print('Valor para sair')
#         break
#     else: 
#         print('valor inválido')  

a=(int(input('Insert Number\n')))
b=a
while True:
    a=a-1
    print(a)
    if a==0:
        break
print('\n número de reduções de 1 possíveis até 0: %i'%b)

