# tra={}
# tra ['pineapple']='abacaxi'
# tra ['apple']='maçã'
# tra ['orange']='laranja'
# print (type(tra))
# print (tra)
# print(tra['apple'])
# tradutor={'pineapple': 'abacaxi', 'apple': 'maçã', 'orange': 'laranja'}
tom=1
list={1:'C',2:'C#',3:'D'}
acorde={'C':'Dó Maior','C#':'Dó# Maior','D':'Ré Maior'}
a=input('Qual nota? -->')


d=(input('{} \nAumentar 1/2 Tom (+)\nDiminuir 1/2 Tom (-)\nSair (0)\n'.format(acorde[a])))
while d!='0':
    list=[a+=1]    print('Dó Sustenido Maior: {}\nAumentar 1/2 Tom (+)\nDiminuir 1/2 Tom (-)\n'.format(list[a]))
