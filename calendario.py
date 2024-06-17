


def dataExt():
    listaMeses={1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}
    
    dia=[int(input('Digite a data no formato DDMMAAAA:\nDia: '))]
    mes=[int(input('Mês: '))]
    ano=[int(input('Ano: '))]
    
    print(f"{dia} de {listaMeses[mes]} de {ano}")

dataExt()

