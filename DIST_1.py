
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

def c_sub(x,y):
    if(x==y):
        return 0
    elif((x=="A" and y=="T") or (y=="A" and x=="T") or (x=="G" and y=="C") or (y=="G" and x=="C")):
        return 3
    else:
        return 4

c_del = 2
c_ins = 2
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


        # if(j>0 and T[i][j]==T[i][j-1] + c_ins):
        #     ali_x.insert(0, '-')
        #     ali_y.insert(0, y[j-1])
        #     j=j-1
        # elif(i>0 and T[i][j]==T[i-1][j] + c_del):
        #     ali_x.insert(0, x[i-1])
        #     ali_y.insert(0, '-')
        #     i=i-1
        # else:
        #     ali_x.insert(0, x[i-1])
        #     ali_y.insert(0, y[j-1])
        #     i=i-1
        #     j=j-1
    
    return ali_x, ali_y

def PROG_DYN(x,y):
    #print("x:\n{}\ny:\n{}".format(x,y))
    d = DIST_1(x,y)
    #printMatrice(T,x,y)
    #print("Distance d(x,y) = {}".format(d))
    a_x, a_y = SOL_1(T,x,y)
    #print("Alignement optimal:\n{}\n{}".format(a_x,a_y))


def mot_gaps(k):
    return ['-'] * k

def align_lettre_mot(x,y):
    mot_x = mot_gaps(len(y))
    cout = float("inf")
    indice = 0
    for i in range(len(y)):
        if(x==y[i]): #si a=b
            indice = i
            break
        else:
            if(c_sub(x,y[i])<cout):
                cout=c_sub(x,y[i])
                indice = i

    mot_x[indice] = x
    return mot_x, y
    
XA = []
YA = []



def coupure(x,y):
    n = len(x)
    m = len(y)
    iStar = abs(n) // 2

    D = [ [ 0 for j in range(len(y)+1)] for i in range(2)]
    I = [ [ 0 for j in range(len(y)+1)] for i in range(2)] 

    for j in range(1,m+1):
        D[0][j] = c_ins*j
        I[0][j] = j #initialisation 0 1 2 3 4 5

    for i in range(1,n+1):
        D[1][0] = c_del*i
        I[1][0] = 0
        for j in range(1,m+1):
            D[1][j] = min(D[0][j] + c_ins, D[1][j-1] + c_del, D[0][j-1] + c_sub(x[i-1],y[j-1]))
            if(i>iStar):
                
                if(D[1][j] == D[1][j-1] + c_del):
                    # print("element {} {} {}".format(D[1][j],D[1][j-1],I[0][j-1]))
                    I[1][j] = I[1][j-1]
                elif(D[1][j] == D[0][j] + c_ins):
                    # print("element {} {} {}".format(D[1][j],D[0][j],I[0][j]))
                    I[1][j] = I[0][j]
                elif(D[1][j] == D[0][j-1] + c_sub(x[i-1],y[j-1])):
                    # print("element {} {} {}".format(D[1][j],D[0][j-1],I[0][j-1]))
                    I[1][j] = I[0][j-1]  

                
        if(i>iStar and i!=n):
            I[0], I[1] = I[1], I[0]

        if(i!=n):

            D[0], D[1] = D[1], D[0]
        # print(I[1])    

    return I[1][-1]

def SOL_2(x,y):
    n = len(x)
    m = len(y)
    if (n>1) and (m>=1):
        i = abs(n)//2
        j = coupure(x,y)
        print("la coupure pour x={} y={} i:{} j:{}".format(x,y,i,j))
        SOL_2(x[0:i],y[0:j])
        SOL_2(x[i:],y[j:])


    else:
        print("fina; n:{} m:{} {} {}".format(n,m,x,y))
        if(n==0):
            for letterY in y:
                XA.append('-')
        else:
            for letterX in x:
                XA.append(letterX)
        if(m==0):
            for letterX in x:
                YA.append('-')
        else:
            for letterY in y:
                YA.append(letterY)
            
# print(coupure("ATTGTA","ATCTTA"))
SOL_2("ATTGTA","ATCTTA")
print(XA)
print(YA)
print(coupure("T","C"))
# print(DEST_1(T,x,y))
# printMatrice(T,x,y)

# x,y = readFile("./Inst_0000010_44.adn")
# DEST_1(x,y)

# x,y = readFile("./Inst_0000010_7.adn")

# x,y = readFile("./Inst_0000010_8.adn")
# DEST_1(x,y)

# DIST_1("ATTGTA","ATCTTA")
# print(SOL_1(T,"ATTGTA","ATCTTA"))

# PROG_DYN(x,y)
# DIST_2(x,y)
# print(DIST_2(x,y))