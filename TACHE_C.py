from tools import *
from macros import *

def DIST_2(x,y):
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
            # D.pop(0) #remove first row
            # D.append(listeAjouter.copy) #memory complexity???
            D[0], D[1] = D[1], D[0]

    return D[1][-1]

x,y = readFile("./Instances_genome/Inst_0000010_7.adn")

print(DIST_2(x,y))