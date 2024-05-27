# while True:
#     d=(int(input('\nCalculadora\nMultiplicação (1)\nDivisão       (2)\nSoma          (3)\nSubtração     (4)\nSair          (0)\n')))
#     if d==0:
#         print('Fim')
#         break
#     n1=(float(input('Digite número: ')))
#     n2=(float(input('Digite número: ')))

#     if d==1:
#         print('\n{} x {} = {}'.format(n1,n2,(n1*n2)))
#     elif d==2:
#         print('\n{} / {} = {}'.format(n1,n2,(n1/n2)))
#     elif d==3:
#         print('\n{} + {} = {}'.format(n1,n2,(n1+n2)))
#     elif d==4:
#         print('\n{} - {} = {}'.format(n1,n2,(n1-n2)))
while True:
    nome=input('Nome: ')
    senha=input('Senha: ')
    if nome==senha:
        print('Senha inválida ')
    else:
        break
        