import random

prix=random.randint (0,100)

prix1 = int(input("Deviner le prix :"))

while prix != prix1 :

    if prix < prix1 :
        print("prix plus petit")
        prix1 = int(input("Deviner le prix :"))

    elif prix > prix1 : 
        print("prix plus grand")
        prix1 = int(input("Deviner le prix :"))


else : 
    print ("Bravo!Vous avez trouvé le nombre !")