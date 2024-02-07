import sys

#créer une liste comportant plusieurs sous listes déterminée par un scheme spécifique sur fichier 1
def lecture_fichier_1(lien_1, scheme):
    liste_ext = []
    with open(lien_1, 'r') as f:
        sous_liste = []
        for l in f:           
            if l.strip().startswith(scheme):
                if sous_liste:
                    liste_ext.append(sous_liste)
                    sous_liste = []
                sous_liste.append(l.strip())
            else:
                sous_liste.append(l.strip())        
            for i, element in enumerate(sous_liste):
                sous_liste[i] = element.replace("---------------------", "")
        if sous_liste:
            liste_ext.append(sous_liste)     
    return liste_ext

#creer une liste avec les éléments du fichier 2
def lecture_fichier_2(lien_2):
    with open(lien_2, 'r') as f:
        txt = f.readlines() 
        contenu_fichier = [c.strip() for c in txt]
        for i, element in enumerate(contenu_fichier):
            contenu_fichier[i] = element.replace("-", "")
        return contenu_fichier
    
    
#comparer fichier 1 et 2, detecter valeur données présentes
def comparer_listes(fichier_1, fichier_2):
    global elements_fichier_valides 
    global elements_fichier_2
    global elements_fichier_1
    
    elements_fichier_1 = lecture_fichier_1(fichier_1,"--------------------exempledescheme")
    elements_fichier_2 = lecture_fichier_2(fichier_2)
    elements_fichier_2 = [elem.strip() for elem in elements_fichier_2 if elem.strip()]

    elements_fichier_valides = []
    
    for element_2 in elements_fichier_2:          
        for sous_liste in elements_fichier_1 :
            if element_2.lower() in sous_liste and element_2.lower != "":
                elements_fichier_valides.append(element_2)
    

# Vérifier si suffisamment d'arguments ont été passés
if len(sys.argv) != 3:
    print("Erreur: Il faut mettre 2 arguments (ex: python3 /check_err.py fichier1.txt fichier2.txt)")
    sys.exit()

arg_1 = sys.argv[1]
arg_2 = sys.argv[2]

scheme = "--------------------exempledescheme"#Définition du schème pour différencier les noms du fichier 1
comparer_listes(arg_1, arg_2)
           
#Check E_Error
err = False
liste_err = []
for index, s_l in enumerate(elements_fichier_1):
    for i, element in enumerate(s_l):
        if element.startswith("E_ ") :
            err = True
            liste_err.append(s_l[0])

           
if liste_err != []:
    print("[ERROR] dans :") 
    for a in liste_err:
        print(a)

if elements_fichier_2 == elements_fichier_valides and err  == False:
    print("[OK]\nLog Complet")
elif elements_fichier_2 == elements_fichier_valides:
    print("")
    print("[OK]\nToutes les données sont présentes")
    print("")
else:
    for i in elements_fichier_2:
        if i not in elements_fichier_valides:
            print(f"[KO]\nDonnées manquantes : {i}")

    

