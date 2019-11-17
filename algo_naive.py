# x = ['A','C','T','G','C','C','T','G']
# y = ['C','G','A','T','T','T','G','C','A','T']
# x = ['A','C','A','A']
# y = ['A','C','T','G','T']
def c_sub(x,y):
    if(x==y):
        return 0
    elif((x=="A" and y=="T") or (y=="A" and x=="T") or (x=="G" and y=="C") or (y=="G" and x=="C")):
        return 3
    else:
        return 4

c_del = 2
c_ins = 2

def DIST_NAIF(x,y):
    """
        x et y sont deux listes
        retourne la distance des mots x et y
    """
    print(x)
    print(y)
    return DIST_NAIF_REC(x,y,0,0,0,float("inf"))

    
def DIST_NAIF_REC(x,y,i,j,c,dist):
    """
        x et y deux mots, i indice dans x, j indice dans y
        c le cout d'alignement de (xi,yj)
        dist le cout de meilleur alignement connu
    """
    
    if(i==len(x) and j==len(y)):
        if(c<dist):
            dist = c
    else:
        if(i<len(x) and j<len(y)):
            dist = DIST_NAIF_REC(x, y, i+1, j+1, c+c_sub(x[i], y[j]), dist) #i+1 j+1 e vo zadacata, ama dava exception taka
        else:
            if(i<len(x)):
                dist = DIST_NAIF_REC(x, y, i+1, j, c+c_del, dist)
            if(j<len(y)):
                dist = DIST_NAIF_REC(x, y, i, j+1, c+c_ins, dist)
    
    return dist    

def readFile(p):
    f = open(p, "r")
    
    X=f.readlines()[-2]
    x=[]
    for e in X:
        if(e!=" "):
            x.append(e)
    
    #problem, ne raboti so eden f
    f.close() 
    f = open(p, "r")
    Y=f.readlines()[-1]
    y=[]
    for e in Y:
        if(e!=" "):
            y.append(e)
     
    return x[:-1], y[:-1]


    f.close()


x,y = readFile("./Inst_0000010_44.adn")
print(DIST_NAIF(x,y)) #treba 10 da vrati
x,y = readFile("./Inst_0000010_7.adn")
print(DIST_NAIF(x,y)) #treba 8 da vrati
x,y = readFile("./Inst_0000010_8.adn")
print(DIST_NAIF(x,y)) #treba 2 da vrati

