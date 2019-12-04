from tools import *
from macros import *
import time

def DIST_2(x,y):
    """
        Distance de deux mots x et y en memoire lineaire
    """
    n=len(x)
    m=len(y)
    #listeAjouter = [0 for i in range(m+1)]
    D = [ [ 0 for j in range(len(y)+1)] for i in range(2)]
    for j in range(1,m+1):
        D[0][j] = c_ins*j

    for i in range(1,n+1):
        D[1][0] = c_del*i
        for j in range(1,m+1):
            D[1][j] = min(D[0][j] + c_ins, D[1][j-1] + c_del, D[0][j-1] + c_sub(x[i-1],y[j-1]))
        if(i!=n):
            D[0], D[1] = D[1], D[0]

    return D[1][-1]

# Pour essayer l'algorithme:
# x,y = readFile("./Instances_genome/Inst_0000010_7.adn")
# print(DIST_2(x,y)) 


#Pour faire des tests sur les instances et les utiliser pour les plots:

# X = []
# Y = []

# testFilesC = [
# "Inst_0000010_44.adn", \
# "Inst_0000012_13.adn", \
# "Inst_0000013_45.adn", \
# "Inst_0000014_23.adn", \
# "Inst_0000015_2.adn", \
# "Inst_0000020_17.adn", \
# "Inst_0000050_3.adn", \
# "Inst_0000100_3.adn", \
# "Inst_0000500_3.adn", \
# "Inst_0001000_23.adn", \
# "Inst_0002000_3.adn", \
# "Inst_0003000_45.adn", \
# "Inst_0005000_4.adn", \
# "Inst_0008000_32.adn", \
# "Inst_0010000_50.adn", \
# "Inst_0015000_20.adn", \
# "Inst_0020000_5.adn", ]


# print("instance:tailleX:tailleY:seconds")

# for ls in testFilesC:
#     x,y = readFile("./Instances_genome/"+ls)
#     n=len(x)
#     m=len(y)
#     start_time = time.time()
#     DIST_2(x,y)
#     t=round((time.time() - start_time),4)
#     print("x:{};{}".format(n,t))
#     X.append(n)
#     Y.append(round(t,4))

# pour l'instance "Inst_0050000_63.adn" de taille 50 000 avec DIST_2
#   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND   
# 21399 3874261   20   0   29428  13512   4892 R 100,0  0,0   4:58.23 python3   