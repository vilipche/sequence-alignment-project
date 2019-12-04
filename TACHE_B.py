from macros import *
from tools import *
import time

T=None

def DIST_1(x,y):
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

    #printMatrice(T,x,y)
    return T[n][m]


def SOL_1(T,x,y):
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
    # global T
    d = DIST_1(x,y)
    printMatrice(T,x,y)
    #print("Distance d(x,y) = {}".format(d))
    a_x, a_y = SOL_1(T,x,y)
    print("Alignement optimal:\n{}\n{}".format(a_x,a_y))


x,y = readFile("./Instances_genome/Inst_0000010_7.adn")
PROG_DYN(x,y) #2



# start_time = time.time()
# DIST_NAIF(x,y)
# print((time.time() - start_time))

# listFiles = ["Inst_0000010_8", "Inst_0000012_56","Inst_0000013_45","Inst_0000014_7","Inst_0000015_2","Inst_0000020_8","Inst_0000050_3"]

# for ls in listFiles:
#     x,y = readFile("./Instances_genome/"+ls+".adn")
#     n=len(x)
#     m=len(y)
#     start_time = time.time()
#     PROG_DYN(x,y)
#     print("{}:{}".format(n, (time.time() - start_time)))