from macros import *
from tools import *
XA=[]
YA=[]
def SOL_2(x,y):
    n = len(x)
    m = len(y)
    if (n>1) and (m>=1):
        i = abs(n)//2
        j = coupure(x,y)
        print("la coupure pour x={} y={} i:{} j:{}".format(x,y,i,j))
        SOL_2(x[0:i],y[0:j])
        SOL_2(x[i:],y[j:])
    elif(n==1) and (m>1):
        a=align_lettre_mot(x,y)
        for letterX in a[0]:
            XA.append(letterX)
        for letterY in y:
            YA.append(letterY)
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


print(coupure("ATTGTA","ATCTTA"))
SOL_2("ATTGTA","ATCTTA")
print(XA)
print(YA)