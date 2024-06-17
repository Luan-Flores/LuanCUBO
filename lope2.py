# for i in range(1,51):
#     if(i%2==1):
#         print(i)
# for j in range(1,51,2):
#     print(j)

a=int(input('insert '))
b=int(input('insert '))
s=0
for n in range (a,b+1):
    print(n)
    s+=n
print('soma:',s)