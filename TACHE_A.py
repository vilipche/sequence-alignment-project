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

# Pour voir si l'algo marche:

# x,y = readFile("./Instances_genome/Inst_0000010_44.adn")
# print(DIST_NAIF(x,y)) #10
# x,y = readFile("./Instances_genome/Inst_0000010_7.adn")
# print(DIST_NAIF(x,y)) #8
# x,y = readFile("./Instances_genome/Inst_0000010_8.adn")
# print(DIST_NAIF(x,y)) #2


listFiles = ["Inst_0000010_7","Inst_0000010_8","Inst_0000010_44",\
            "Inst_0000012_13","Inst_0000012_32","Inst_0000012_56",\
            "Inst_0000013_45","Inst_0000013_56","Inst_0000013_89",\
            "Inst_0000014_7","Inst_0000014_23","Inst_0000014_83",\
            "Inst_0000015_2","Inst_0000015_4","Inst_0000015_76",\
            "Inst_0000020_8","Inst_0000020_17","Inst_0000020_32"]

# listFiles = ["Inst_0000010_8", "Inst_0000012_56","Inst_0000013_45","Inst_0000014_7","Inst_0000015_2","Inst_0000020_8","Inst_0000050_3","Inst_0000100_3","Inst_0000500_3"]
#Test en moins d'une minute



# print("instance:tailleX:tailleY:seconds")
# for ls in listFiles:
#     x,y = readFile("./Instances_genome/"+ls+".adn")
#     n=len(x)
#     m=len(y)
#     start_time = time.time()
#     DIST_NAIF(x,y)
#     print("{}:\tx:{} y:{}\t{}".format(ls,n,m, (time.time() - start_time)))

# Resultats:

# instance:           tailleX:tailleY:seconds
# Inst_0000010_7:         x:10 y:10       5.566756010055542
# Inst_0000010_8:         x:10 y:9        2.2577273845672607
# Inst_0000010_44:        x:10 y:5        0.030281782150268555
# Inst_0000012_13:        x:12 y:9        10.14145803451538
# Inst_0000012_32:        x:12 y:9        10.197986602783203
# Inst_0000012_56:        x:12 y:11       74.36218762397766
# Inst_0000013_45:        x:13 y:12       409.54640221595764
# Inst_0000013_56:        x:13 y:12       413.4217278957367
# Inst_0000013_89:        x:13 y:12       414.7486081123352
# Inst_0000014_7:         x:14 y:12       911.9344797134399
# Inst_0000014_23:        x:14 y:10       118.05104804039001
# Inst_0000014_83:        x:14 y:10       116.8823618888855