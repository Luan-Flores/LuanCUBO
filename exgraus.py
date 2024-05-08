#converter temperatura  
'''g= float(input('Digite a temperatura em Fahrenheit: '))
new=(5/9)*(g-32)
#
# print('A temperatura %.2f° Fahrenheit é igual a %.2f° Celsius. '%(g,new))
print('temperaturwa',g,'em raus é igual a ',round(new,2))'''

n=input('Nome do produto: ')
v=float(input('Valor do produto: '))
q=int(input('Quantidade: '))
d=float(input('Quantos % de desconto? '))
des=(q*v)-((d/100)*(q*v))
print(q,'produto(s) %s, valor total: R$%2.f '%(n,des))
