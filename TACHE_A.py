import time
from tools import *
from macros import *

def DIST_NAIF(x,y):
    """
        x et y sont deux listes
        retourne la distance des mots x et y
    """
    # print(x)
    # print(y)
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
            dist = DIST_NAIF_REC(x, y, i+1, j+1, c+c_sub(x[i], y[j]), dist) 
        if(i<len(x)):
            dist = DIST_NAIF_REC(x, y, i+1, j, c+c_del, dist)
        if(j<len(y)):
            dist = DIST_NAIF_REC(x, y, i, j+1, c+c_ins, dist)

    return dist    

# x,y = readFile("./Instances_genome/Inst_0000010_44.adn")
# print(DIST_NAIF(x,y)) #10
# x,y = readFile("./Instances_genome/Inst_0000010_7.adn")
# print(DIST_NAIF(x,y)) #8
# x,y = readFile("./Instances_genome/Inst_0000010_8.adn")
# print(DIST_NAIF(x,y)) #2



listFiles = ["Inst_0000010_8", "Inst_0000012_56","Inst_0000013_45","Inst_0000014_7","Inst_0000015_2","Inst_0000020_8","Inst_0000050_3"]

for ls in listFiles:
    x,y = readFile("./Instances_genome/"+ls+".adn")
    n=len(x)
    m=len(y)
    start_time = time.time()
    DIST_NAIF(x,y)
    print("{}:{}".format(n, (time.time() - start_time)))


