x = ['A','C','T','G','C','C','T','G']
y = ['C','G','A','T','T','T','G','C','A','T']

def DIST_NAIF(x,y):
    """
        x et y sont deux listes
        retourne la distance des mots x et y
    """
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
            dist = DIST_NAIF_REC(x, y, i+1, j+1, c+c_sub(x[i+1], y[j+1]), dist)
        else:
            if(i<len(x)):
                dist = DIST_NAIF_REC(x, y, i+1, j, c+c_del, dist)
            if(j<len(y)):
                dist = DIST_NAIF_REC(x, y, i, j+1, c+c_ins, dist)
    
    return dist    

def c_sub(x,y):
    pass

def c_del():
    pass

def c_ins():
    pass
