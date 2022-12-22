import os

dossier = "scriptura"

fichiers = os.listdir(dossier)
try:
  for fichier in fichiers:
    texte = open(os.path.join(dossier, fichier), encoding='utf-8').read()
    texte = texte.replace(" :", ":")
    texte = texte.replace(" ;", ";")
    texte = texte.replace(" ?", "?")
    texte = texte.replace(" !", "!")
    texte = texte.replace("« ", "«")
    texte = texte.replace(" »", "»")
    f = open(os.path.join(dossier, fichier), 'w', encoding='utf-8')
    f.write(texte)
    f.close()
except Exception as e:
  print(e)

input()
