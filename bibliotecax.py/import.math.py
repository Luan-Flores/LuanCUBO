import math, os
a=float(input('Digite um número: '))






print(math.ceil(a))                  #ceil -> arredonda número ^^^^^
a=math.ceil(a)

print('{:.0f}'.format(math.fabs(a))) # fabs -> Módulo do número
print(math.floor(a))                 # floor -> arredonda número vvvv
print(math.isqrt(a))                 # Isqrt -> Raiz quadrada exata (Inteiro)                  
print(math.sqrt(a))                  # sqrt  -> Raiz quadrada (float)
print(math.factorial(a))             # factorial -> !


os.system('pause')
os.system('cls')


x=float(input('Base: '))             # pow(x,y) -> eleva X ao expoente Y
y=float(input('Expoente: '))
print(math.pow(x,y))