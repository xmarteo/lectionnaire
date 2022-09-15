import os

liste_dossiers = ["homeliaire_evangelique", "homeliaire_scripturaire", "lectionnaire"]
liste_chaines_interdites = ["« ", " »", " ;", " :", " ?", " !", "'", "oe", "A ", "/", "Evangile", "Eglise"]
longueur_max_lignes = 80
largeur_tab = 4

def erreur(dossier, fichier, err, ligne):
  print(dossier+"/"+fichier+"    "+err+" "+str(ligne+1))

for dossier in liste_dossiers :
  for fichier in os.listdir(dossier) :
    try:
      lignes = open(os.path.join(dossier, fichier), encoding='utf-8').readlines()
      for (i,l) in enumerate(lignes):
        for x in liste_chaines_interdites:
          if x in l:
            erreur(dossier, fichier, x, i)
        if l[0]=='«':
          y=1
        else:
          y=0 # y est la position du premier caractère alphabétique attendu
        if (i==0 and not l[y].isupper()): # le texte ne commence pas par une majuscule
          erreur(dossier, fichier, "incipit", i)
        if len(l) == 1: # ligne vide, == "\n"
          erreur(dossier, fichier, "vide", i)
        if l[-1] != '\n': # manque un retour en fin de dernière ligne
          erreur(dossier, fichier, "sans retour chariot", i)
        # on regarde maintenant la ligne sans son caractère de fin
        l = l.removesuffix('\n')
        # on compte les tabs au début de la ligne, puis on les enlève
        n_tabs = len(l)-len(l.lstrip('\t'))
        l = l.lstrip('\t')
        if n_tabs > 2: # trop de tabs en début de ligne
          erreur(dossier, fichier, "tabs", i)
        if (len(l) + largeur_tab * n_tabs) > longueur_max_lignes:
          erreur(dossier, fichier, "longueur", i)
        if l.strip() != l :
          erreur(dossier, fichier, "espaces", i)
    except Exception as e:
      print(e)
      print(dossier+"/"+fichier)
input()