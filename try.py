try:
 a=int(input('digite palavra'))
except ValueError:
   print('apenas números')
except:
  print('erro desconhecido')
finally:
  print('final do algoritmo')