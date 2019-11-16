import itertools



def nb_alignements_possibles(x,y,k_x):
    """
    str, str, int -> int
    retourne le nombre des facons pour inserer les gaps dans y
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
    print("X_gap: {}".format(x_gap))
    print("Y_gap: {}\n".format(y_gap))

    #creation de tous les mots de x_gap
    mots_de_x_gap = []

    wordlength = len(x) + k_x
    characters = x
    for indices in itertools.combinations(range(wordlength), len(characters)):
        s = ['-']*wordlength
        for index, character in zip(indices, characters):
            s[index] = character
        mots_de_x_gap.append(''.join(s))
    
    print("Tous les mots de X_gap: {}\n{}".format(len(mots_de_x_gap),mots_de_x_gap))

    #creation de tous les mots de y_gap
    mots_de_y_gap = []
    wordlength = len(y) + k_y
    characters = y
    for indices in itertools.combinations(range(wordlength), len(characters)):
        s = ['-']*wordlength
        for index, character in zip(indices, characters):
            s[index] = character
        mots_de_y_gap.append(''.join(s))

    #print("Tous les mots de Y_gap: {}\n{}".format(len(mots_de_y_gap),mots_de_y_gap))

    print("Mots y gap:", len(mots_de_y_gap))
    
    y_aligne = []
    #eviter les gaps doublant
    for motX in mots_de_x_gap:
        for motY in mots_de_y_gap:
            ajouter = True
            for i in range(len(motX)):
                if(motX[i]=="-" and motY[i]=="-"):
                    ajouter = False
                    break
            if(motY not in y_aligne and ajouter == True):
                y_aligne.append(motY)
           
    #print("Total alignements de Y_gap: {}".format(len(y_aligne)))
    print(len(y_aligne))
    #print(y_aligne)     
    
    return len(y_aligne)


def creation_gap(mot, k):
    mot_gap = mot
    for i in range(k):
        mot_gap = mot_gap +"-"
    return mot_gap

x = "ctfctfctfctfctf"
k_x = 1
y = "gtcgtcgtcg"
# k_y = ""
# x_gap = x
# y_gap = ""

nb_alignements_possibles(x,y,k_x)

