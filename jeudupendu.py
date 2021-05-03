from random import choice



def saisie () :
    lettre = input ('Entrer une lettre :')
    if len (lettre)  > 1 or ord(lettre) < 65 or ord(lettre) > 122:
        return saisie()
    else : 
        lettre.upper()

motadeviner = ()
lettreproposees = []
print ("Mot à deviner : ")
nb_erreurs =0

while nb_erreurs < 6 : 
    lettre = saisie()
    if lettre not in lettreproposees: 
        lettreproposees += [ lettre ]

    if lettre not in motadeviner: 
        nb_erreurs += 1
    print( '\nMot à deviner : ' , ' '*6 , 'Nombre d\'erreurs maximum :' , 6-nb_erreurs )