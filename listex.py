# a=[[1,2],[3],[4,5,6]]
# b=(sum(a[0]))
# b=b+sum(a[1])
# b=b+sum(a[2])
# print(b)

# i=1
# soma=0
# lista=[]
# mais=[]
# while i!=0:
#     a=int(input('digite um número'))
#     lista.append(a)
#     soma=(sum(lista))
#     mais.append(soma)
#     print(mais)
#     i=int(input('continue () (0) quit'))
    
# lista=[2,3]
# lista.append(4)
# print(lista)
# lista.append(5)
# print(lista)
lista=[]

a=int(input('insert'))
b=int(input('insert'))
c=int(input('insert'))
lista=[a,b,c]
del lista[-1]   
del lista[0]
print(lista)