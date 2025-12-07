montant =float(input("entre le montant acheter en gourdes:"))
if montant>=50000:
    retour=montant*0.20
elif montant>=25000:
    retour=montant*0.10
elif montant>=10000:
    retour=montant*0.05
else:
    retour=0
                
                
print("le retour est:",retour,"gdes")