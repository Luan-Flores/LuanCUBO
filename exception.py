while True:
    d=input('(1) Cadastro\n(0) Encerrar\n')
    if d=='1':
        nome=input('Nome: ')
    
        while True:
            try:
                rg=int(input('RG: '))
                break
            except ValueError:
                print('tipos de dados inseridos inválidos')
        
        while True:
            try:
                ida=int(input('Idade: '))
                break
            except ValueError:    
                print('tipos de dados inseridos inválidos')  
        print('\n\n\nNome: {}\nRG: {}\nIdade: {}'.format(nome,rg,ida))
        
    elif d=='0':
        print('Fim')
        break
    else:
        print('volta.')
        continue