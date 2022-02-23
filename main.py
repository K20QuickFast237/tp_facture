#TODO
import copy

#model de dictionnaire
produit = {
    "quantite" : "<vide>",
    "nom"      : "<vide>",
    "prix"     : "<vide>"
}
productList = []

#recuperer les saisies utilisateur
print('Entrez la liste de vos produits sur chaque ligne.')
print('En suivant le model:  Qtite | Produit | PU . Exemple (03|Biscuit|100)')
print('Terminez par le mot cle "fin".')
userProduct = 'start'
totalcost = 0

while userProduct != 'fin':
    #recuperation de la saisie
    userProduct = input(': ')
    #verification de la valeur
    if userProduct == 'fin':
        continue
    #formatage de la saisie en tableau
    userProduct = userProduct.split('|')
    #Ajouter les donnees a un tableau

    #calcul du prix total
    totalcost += int(userProduct[0])*int(userProduct[2])

    #copie du produit courant dans la liste des produits
    productList.append(userProduct)

print(f'Prix Total: {totalcost} frs.')
#L'objectif de ce mini TP consite en la génération d'une facture. 