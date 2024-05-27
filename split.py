# # Splita a str em diferentes objetos
nota='Dó Ré Mi Fá Sol Lá Si'
print(nota.split())
dupla='Mato-Grosso-e-Mathias'
print(dupla.split("-"))

# # Find acha qual posição a letra ocupa na string
c='Guilherme e Santiago'
print(c.find("u"))


# in confere se está dentro da variável
a=input('name: ')
if 'a' in a or 'o' in a:
    print('okay')
else:
    print('not okay')
'''okdokd'''
#count mostra a ocorrencia de determinada str
co='bololo da silva'
print(co.count('o'))

#printa índice escolhido de acordo com a posição na str
s='Olá mundo'
print(s[4])
print(s[2:10]) 
print(s[:13])# se omite, começa no 0
