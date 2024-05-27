# pcerta='Monster'
# p=input('Insert\n')
# if p == pcerta.lower():
#     print('{} nao é {}.'.format(p,pcerta))
# elif p==pcerta:
#     print('perfeito, {}'.format(pcerta))
# z='1'
# x=1
# if x==int(z):
#     print('dumb')
i=1
par=0
impar=0

while i!=0:
    i=float(input('Insert number: \n(0) quit')) 
    if i%2==0:
        print('par')
        par += 1
    else:
        print('impar')
        impar += 1
print('Números Pares: {}\nNúmeros Ímpares: {}'.format(par,impar))