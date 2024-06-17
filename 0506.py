import os

def cadastro():
    name=input('Qual seu nome? ')
    age=input('Idade: ')
    return name,age
print('Inicializando cadastro: ')
nome,idade=cadastro()
print('Cadastro realizado. ')
os.system('Pause')
os.system('cls')
print('Seu nome é {0}, você tem {1} ano(s) de idade. '.format(nome,idade))