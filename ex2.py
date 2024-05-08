print('Cálculo do IMC')
a=0
while a!=2:
    n=float(input("Qual o peso? (kg)"))
    alt=float(input('Qual a altura? (m)'))
    imc= float(n/(alt**2))
    print('O IMC é: ',imc)
    a=int(input('Continuar?' '\n''(1)Sim (2)Não''\n'))
print('Fim')
