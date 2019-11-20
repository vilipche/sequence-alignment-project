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

    print("Nb des mots possibles y gap:", len(mots_de_y_gap))
    

    #eviter les gaps doublant
    #y_aligne = []
    alignement = {}
    
    for motX in mots_de_x_gap:
        alignement[motX] = [] #creation d'une liste pour stocker tous les alignements entre un motX et les motY respectif
        for motY in mots_de_y_gap:
            ajouter = True
            for i in range(len(motX)):
                if(motX[i]=="-" and motY[i]=="-"): #pour eviter l'occurence des gaps dans les memes positions
                    ajouter = False
                    break
            if(motY not in alignement[motX] and ajouter == True):
                alignement[motX].append(motY)
            # if(motY not in y_aligne and ajouter == True):
            #     y_aligne.append(motY)

    total_alignements = 0
    for v in alignement.keys():
        print("{} : {}".format(v,len(alignement[v])))
        total_alignements+=len(alignement[v])
        #print(alignement[v])
    print("Au total il y a {} alignements pour un couple (x,y)".format(total_alignements))
    
    return total_alignements


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
#nb_alignements_possibles("ABCD","AB",2)
