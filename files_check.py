import os

def custom_open(filepath):
  """filepath should point to a TSV file with one line of headers
  featuring the following fields: code, incipit, rubric, file (done or not) and source.
  so far, this script will only use the fields code and file."""
  l = open(filepath, encoding="utf8").readlines()
  del l[0]
  if (len(l) > 0 and len(l[-1]) < 4):
    del l[-1]
  l = [x.split('\t') for x in l]
  # ignore lines that correspond to a reading marked as a duplicate and that therefore should have no file
  l = [ [x.strip() for x in line] for line in l if len(line[5].strip())==0 ]
  l = [( x[0].strip() , (len(x[3].strip())>0) ) for x in l]
  return l

def folder_list(folderpath):
  """folderpath should point to an existing folder with tex files inside.
  this function return a list of pairs (filename, size) where size is True when >0 and False when <0."""
  fl = os.listdir(folderpath)
  # ignore files that are not .tex
  fl = [x[0:-4] for x in fl if x[-4:]=='.tex']
  l = []
  for x in fl:
    file_is_populated = (os.path.getsize(os.path.join(folderpath, x+".tex")) > 0)
    l.append((x,file_is_populated))
  return l

# Opening of all descriptor files
hom_evang = custom_open("homiliae.tsv")
hom_script = custom_open("sermones_legendae.tsv")
lectionnaire = custom_open("scriptura.tsv")

# Getting the list of all folders
hom_evang_files = folder_list("homiliae")
hom_script_files = folder_list("sermones_legendae")
lectionnaire_files = folder_list("scriptura")

# Check for duplicates in the descriptor files
codes = [x[0] for x in hom_evang+hom_script+lectionnaire]
for c in set(codes):
  if codes.count(c) > 1:
    print("Doublon : "+c)

# Check for files that are in the descriptors but not in the folders, or the opposite,
# or described as done but are empty, or not described as done but are populated.
for (l1,l2) in [(hom_evang, hom_evang_files),
                (hom_script, hom_script_files),
                (lectionnaire, lectionnaire_files)]:
  # x is a pair (filename, file_is_done)
  for x in l1:
    if x not in l2:
      print("Fichier manquant ou inattendu :"+x[0])
  for x in l2:
    if x not in l1:
      print("Fichier non décrit ou inattendu :"+x[0])

input()