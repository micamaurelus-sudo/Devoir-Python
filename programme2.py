annee_naissance = int(input("Antre anne de naissance:"))
anne_courant = 2025
age = annee_courant - annee_naissance

if age >60:
    print("Bon retraite.")
elif age> 18:
    print("Bon travail.")
        
elif age >10:
    print("Amuse toi bien.")

else:
    print("Prepare toi, la vie t'attend.")