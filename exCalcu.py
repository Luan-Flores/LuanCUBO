def calculadora():
    while True:
        d=(int(input('\nCalculadora\nMultiplicação (1)\nDivisão       (2)\nSoma          (3)\nSubtração     (4)\nSair          (0)\n')))
        if d==0:
            print('Fim')
            break
        a=(float(input('Digite número: ')))
        b=(float(input('Digite número: ')))

        if d==1:
            print('\n{} x {} = {}'.format(a,b,(a*b)))
        elif d==2:
            print('\n{} / {} = {}'.format(a,b,(a/b)))
        elif d==3:
            print('\n{} + {} = {}'.format(a,b,(a+b)))
        elif d==4:
            print('\n{} - {} = {}'.format(a,b,(a-b)))

calculadora()