#mostrar numero de caracteres
a='eDersonnnnn'
print(len(a))
print(a.capitalize())

#todo o texto em CAPS
print(a.lower())
b='aaaa'
print(b.islower())

#.upper para o input se tornar MAIÚSCULO
sexo=input('Digite o sexo (F)Feminino (M)Masculino')
if sexo.upper()=='F':
    print('Feminino')
elif sexo.upper()=='M':
    print('Macho')

#  .islower() ou .isupper() 
#  Mostrar se é todo minúsculo ou se é todo maiúsculo
#  (True or False)

# Confere se a STR é toda número
a='12345'
print(a.isdigit())
#True
b='12345abcde'
print(b.isdigit())
#False

# a.replace('str1',por,'str2')
a = "Ederson roberto"
print(a.replace('Ederson','Arantes'))