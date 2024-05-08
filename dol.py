i = float(input('ajijmer'))
while (i>0): 
    print('Converter real para dólar')
    reas=float(input('Quantos reais? R$:'))
    cot= float(input('Qual cotação do dólar? '))
    conta= reas / cot
    print('O valor é: $%2.2f'%conta)
    i=conta
    