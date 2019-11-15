import itertools

x = "ctg"
k_x = 2
y = "tc"
k_y = ""
x_gap = x
y_gap = ""

def nb_alignements_possibles(x,y,k_x):
    """
    str, str, int -> int
    """
    if(len(x) < len(y)):
        raise Exception("Il faut que n>=m!")

    if(len(y) < k_x):
        raise Exception("Il faut que m soit plus grand!")
    else:
        k_y = len(x) + k_x - len(y) 
    
    #cration de x_gap
    x_gap = creation_gap(x, k_x)
    
    #cration de y_gap
    y_gap = creation_gap(y, k_y)
    print(x_gap)
    print(y_gap)

    #creation de tous les mots de x_gap
    mots_de_x_gap = list(set(["".join(perm) for perm in itertools.permutations(x_gap)]))
    print(mots_de_x_gap)
    
    #creation de tous les mots de y_gap
    mots_de_y_gap = list(set(["".join(perm) for perm in itertools.permutations(y_gap)]))
    print(mots_de_y_gap)

    y_aligne = []
    #eviter les gaps doublant
    for motX in mots_de_x_gap:
        for motY in mots_de_y_gap:
            for i in range(len(motX)):
                if(motX[i]=="-" and motY[i]=="-"):
                    break
            if(motY not in y_aligne):
                y_aligne.append(motY)
    print(y_aligne)            
    print(len(y_aligne))






def creation_gap(mot, k):
    mot_gap = mot
    for i in range(k):
        mot_gap = mot_gap +"-"
    return mot_gap

nb_alignements_possibles(x,y,k_x)