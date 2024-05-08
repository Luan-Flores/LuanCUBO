n1=99999999
while(n1!=0 or n2!=0):
    nome=str(input('Qual seu nome? '))
    ida=int(input('Qual a idade? '))
    sex=int(input('Qual seu sexo? \nMasculino(1) Feminino(2)'))
    n1=float(input('Qual nota 1?'))
    n2=float(input('Qual nota 2? '))
    n3=(n1+n2)/2
    if(sex==1):
        print('Sr.',nome,', sexo masculino, idade',ida, ', a média das notas é: %2.f'%n3)
    elif(sex==2):
        print('Sra.',nome,', sexo feminino, idade',ida, ', a média das notas é: %2.f'%n3)
