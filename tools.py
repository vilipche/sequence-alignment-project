#fichier contenant les outils pour lire et afficher un alignment


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


def printMatrice(T,x,y):
    print("   ",end=' ')
    for i in range(len(y)):
        if(i!=len(y)-1):
            print("%3s" %(y[i]),end="")
        else:
            print("%3s" %(y[i]))

    for i in range(len(T)):
        if(i==0):
            print(" ", end=" ")
        else:
            print(x[i-1], end=" ")

        for j in range(len(T[0])):
            print("%2s" %(T[i][j]),end=' ')
        print(end='\n')
