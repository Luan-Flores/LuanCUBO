import random as rd
def embaralha(word):
    
    word=input('Digite a palavra: ')
    y = len(word)
    x="".join(rd.sample(word,y))
    print(x)
    
embaralha('FutebOl')