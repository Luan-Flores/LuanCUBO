
somaPresta=0
somaDias=0
somaTotal=0

def valortotal(presta,dias):
    multa=(0.03*presta)
    atraso=(0.001*presta)*dias
    total = multa+atraso+presta
    return total





while True:
    valPrest=float(input('Qual o valor da prestação? \nR$'))
    if valPrest==0:
        print('Relatorio:\nR${}'.format(somaTotal))

    
    dias=float(input('Quantos dias de atraso? '))
    prestaJuros=valortotal(valPrest,dias)
    print('Valor total da dívida: R${}'.format(prestaJuros))
    somaTotal+=prestaJuros
    

# print('fim')



