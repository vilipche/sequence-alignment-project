from __future__ import division

def lecture(fic): 
    f = open(fic, 'r')
    l = f.readlines()
    f.close()
    lu = ""
    for line in l[1:]: 
        lu += line[:-1]
    return lu



def CreaTab(text1, text2, gap, M, MM):
	#txt1 est l'abscisse et txt2 est l'ordonnee
	taille1=len(text1)
	taille2=len(text2)
	txt1="0"+text1
	txt2="0"+text2
	matrice = [(0,0)]*(len(txt1)+1)
	for i in xrange((taille1+1)):
		matrice[i]=[(0,0)]*(1+taille2)

	"""Just for info
		0 = Origine
		1 = Gauche
		2 = Diagonal
		3 = Haut
	Info pour la deuxieme valeur du tuple"""

	#Initialisation des premieres lignes et colonnes
	for i in xrange((taille1+1)):
		matrice[i][0]=(-i,1)
	for i in xrange((taille2+1)):
		matrice[0][i]=(-i,3)
	matrice[0][0]=(0,0)
	#M>G>MM pour la suite des calculs
	Val1=0
	Val2=0
	Val3=0
	for x in xrange((taille1)):
		for y in xrange((taille2)):
			if(((len(txt1)+1) <= taille1) and ((len(txt2)+1) <= taille2):
				#Pour 2
				if(txt1[i+1] == txt2[y+1]):
					print("Match")
					Val2=M
				else:
					print("try")
					Val2=MM
				#Pour 1
				if(txt1[i+1] == txt2[y]):
					Val1=gap
					print("Je suis la")
				else:
					Val1=MM
				#Pour 3
				if(txt1[i] == txt2[y+1]):
					Val3=gap
				else:
					Val3=MM
				theval = max(Val3,Val1,Val2)
				print(theval)
				if(theval == Val3):
					matrice[i+1][y+1]=((theval+matrice[i][y+1][0]),3)
				if(theval == Val2):
					matrice[i+1][y+1]=((theval+matrice[i][y][0]),2)
				if(theval == Val1):
					matrice[i+1][y+1]=(theval,1)


	print matrice

CreaTab("cousalut", "coucouc", 1, 2, 0);