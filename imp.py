#SOBRA + C INDICE ATUAL - INDICE FINAL = SOBRA, 
# type: ignore #1,1,2,3,5,8,13,21,34...
tons = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
tomenor = ['Cm','C#m','Dm','D#m','Em','Fm','F#m','Gm','G#m','Am','A#m','Bm']
i=1
d=0
c=0
fla=0
f=0
while i!=0:
    d=(int(input('\nEscala de {0} \n(1)         (2)         (3)\n+1/2 Tom    -1/2 Tom    Imprimir\n'.format(tons[fla]) ) ) )
    if d==1:
        c=c+1
        fla=c
    if c==fla==12:
        c=c-c
        fla=fla-fla
    if d==3:
        if c<3:
            print('Escala de {0}'.format(tons[fla]))
            print('\n',tons[fla],tomenor[fla+2],tomenor[fla+4],tons[fla+5],tons[fla+7],tomenor[fla+9])
            
        elif c>3 and c<5: 
            print('Escala de {0}'.format(tons[fla]))
            print('\n',tons[fla],tomenor[fla+2],tomenor[fla+4],tons[fla+5],tons[fla+7],tomenor[fla-3])
        
        if c==5:
            print('Escala de {0}'.format(tons[fla]))
            print('\n',tons[fla],tomenor[fla+2],tomenor[fla+4],tons[fla+5],tons[fla-5],tomenor[fla-3])
        
        if c>5:
            print('Escala de {0}'.format(tons[fla]))
            print('\n',tons[fla],tomenor[fla+-10],tomenor[fla-8],tons[fla-7],tons[fla-5],tomenor[fla-3])
        
        
        
        
        
        
        
        
        
        
        
        
        # elif c>4:
        #     print('Escala de {0}'.format(tons[fla]))
        #     print('\n',tons[fla],tomenor[fla+2],tomenor[fla+4],tons[fla+5],tons[fla+7],tomenor[fla+9])
            
        # else: 
        #     print('Escala de {0}'.format(tons[fla]))
        #     print('\n',tons[fla],tomenor[fla+2],tomenor[fla+4],tons[fla+5],tons[fla-5],tomenor[fla-3])
        
        
        
        
        #T T ST T T T ST
        #2 3 6 MENORES