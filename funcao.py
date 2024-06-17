def cadPessoa():
    while True:
        try:
            nome=str(input('Nome: '))
            break
        except ValueError:
            print('Tipo de dado inserido inválido ')
        
    while True:
        try:
            idade=int(input('Idade: '))
            break
        except ValueError:
            print('Tipo de dado inserido inválido ')
    
    while True:
        try: 
            rg=int(input('RG: '))
            break
        except ValueError:
            print('Tipo de dado inserido inválido ')

cadPessoa()