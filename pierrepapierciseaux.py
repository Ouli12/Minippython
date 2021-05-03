import random

resultO = random.randint(1,3)

resultJ = int (input("choisissez  pierre = 1, papier = 2 ou ciseau = 3 :"))

if resultO == resultJ : 
    print ("egalité")

if resultO == 1 and resultJ ==2 : 
    print ("Joueur a gagné")
    
if resultO == 1 and resultJ ==3 : 
    print ("L'ordinateur a gagné")
    

if resultO == 2 and resultJ ==1 : 
    print ("l'ordinateur a gagné")
    
if resultO == 2 and resultJ ==3 : 
    print ("Joueur a gagné")
    

if resultO == 3 and resultJ ==1 : 
    print ("joueur a gagné")
    
if resultO == 3 and resultJ ==2 : 
    print ("ordinateur a gagné")
    
if resultO == 1:
    resultO = "pierre"  
if resultO == 2:
    resultO = "papier"  
if resultO == 3:
    resultO = "ciseaux"  

if resultJ == 1:
    resultJ = "pierre"  
if resultJ == 2:
    resultJ = "papier"  
if resultJ == 3:
    resultJ = "ciseaux"  

print (resultO, resultJ )
