from macros import *
from tools import *
import time

T=None

def DIST_1(x,y):
    """
        x et y deux mots, i indice dans x, j indice dans y
        creation de la matrice de distance pour les deux lettres en utilisant la variable globale T
    """
    n=len(x)
    m=len(y)

    global T

    T = [[0 for i in range(m+1)] for j in range(n+1)]

    T[0][0] = 0

    for j in range(1,m+1):
        T[0][j] = c_ins*j

    for i in range(1,n+1):
        T[i][0] = c_del*i

    for i in range(1, n+1):
        for j in range(1, m+1):
            T[i][j] = min(T[i-1][j] + c_del, T[i][j-1] + c_ins, T[i-1][j-1] + c_sub(x[i-1],y[j-1]))

    return T[n][m]


def SOL_1(T,x,y):
    """
        retourne le meilleur alignement pour les deux mots x et y
    """
    ali_x = []
    ali_y = []
    i=len(x)
    j=len(y)
    
    while(i>0 or j>0):
        if(i>0 and j>0 and T[i][j]==T[i-1][j-1]+c_sub(x[i-1],y[j-1])):
            ali_x.insert(0, x[i-1])
            ali_y.insert(0, y[j-1])
            i=i-1
            j=j-1
        elif(i>0 and T[i][j]==T[i-1][j] + c_del):
            ali_x.insert(0, x[i-1])
            ali_y.insert(0, '-')
            i=i-1
        elif(j>0 and T[i][j]==T[i][j-1] + c_ins):
            ali_x.insert(0, '-')
            ali_y.insert(0, y[j-1])
            j=j-1

    return ali_x, ali_y

def PROG_DYN(x,y):
    #print("x:\n{}\ny:\n{}".format(x,y))
    d = DIST_1(x,y)
    # printMatrice(T,x,y)
    #print("Distance d(x,y) = {}".format(d))
    a_x, a_y = SOL_1(T,x,y)
    # print("Alignement optimal:\n{}\n{}".format(a_x,a_y)) 

# Pour essayer l'algorithme:
# x,y = readFile("./Instances_genome/Inst_0000010_7.adn")
# PROG_DYN(x,y) #decommenter l'affichage alignement et printMatrice dans PROG_DYN


#Pour faire des tests sur les instances et les utiliser pour les plots:

# X = []
# Y = []

# testFilesB = [
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
# for ls in testFilesB:
#     x,y = readFile("./Instances_genome/"+ls)
#     n=len(x)
#     m=len(y)
#     start_time = time.time()
#     PROG_DYN(x,y)
#     t=round((time.time() - start_time),4)
#     print("x:{};{}".format(n,t))
#     X.append(n)
#     Y.append(round(t,4))

# print(X)
# print(Y)

#pour les tests de question 29
# for ls in testFilesB:
#     x,y = readFile("./Instances_genome/"+ls)
#     n=len(x)
#     m=len(y)
#     DIST_1(x,y)
#     start_time = time.time()
#     SOL_1(T,x,y)
#     t=round((time.time() - start_time),4)
#     print("x:{};{}".format(n,t))
#     X.append(n)
#     Y.append(round(t,4))


# pour l'instance "Inst_0050000_63.adn" de taille 50 000 avec DIST_1
#   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                                                                                               
# 20371 3874261   20   0 28,338g 0,028t   4888 R 100,0 90,6   4:35.95 python3                                                                