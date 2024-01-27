import csv
import datetime
import requests
import wget

url= "https://"

data = wget.download(url,"skosonnerion-9trr.csv")
    
def load_data(filename):
    mylist =[]
    with open(filename, encoding="utf-8") as data:
        numbers_data = csv.reader(data, delimiter=',')
        #next(numbers_data) #skip the header
        for row in numbers_data:
            mylist.append(row)
        return mylist
    


def removeTitles(filename):
    mylist=[]

    for i in range(0,6):
        mylist.append(filename[i])
        mylist[i].pop(0)  
    
    return mylist




# Convertie une liste de timestamp en une liste de date
def convertir_en_date(dates):
    date_formattees=[]
    for i in range(len(dates)):
        # Créer un objet datetime avec la date de référence (1900-01-01)
        date_reference = datetime.datetime(1900, 1, 1)
    

        # Ajouter le nombre de jours spécifié au nombre de jours de la date de référence
        date_convertie = date_reference + datetime.timedelta(days=dates[i])
        
        # Soustraire 2 jours à la date convertie
        date_convertie -= datetime.timedelta(days=2)

        # Formater la date convertie au format Y-m-d
        date_formattee = date_convertie.strftime("%Y-%m-%d")
        date_formattees.append(date_formattee)
    return date_formattees

# Retourne une liste de strings en liste de dates
def convertir_int(nombres):
    liste=[]
    for i in range(len(nombres[0])):
        if nombres[0][i] != '':
            liste.append(
                int(nombres[0][i]))
    return liste

# Range les colonnes dans le bonne ordre et rajoute id et années dans la liste
def ranger_colonnes(data, dates, annees):
    # Ajoutes la liste des dates formatés à la liste des données
    data[0] = dates
    list = []
    # Indique quel sera l'ordre des colonnes
    #list_trier = [0,3,1,5,4,2]
    list_trier = [0,1,3,5,4,2]
    
    list_id = []
    for i in range(len(list_trier)):
        list.append(data[list_trier[i]])
    for i in range(1,len(list)+3): # Ajout de l'id
        list_id.append(i)
    list.insert(0,list_id)
    
    list.append(annees)
    liste = [element for element in list if element != '']
    return list

# Récupère uniquement les années d'une liste de dates
def select_year(dates):
    annees = map(lambda date: datetime.datetime.strptime(date, "%Y-%m-%d").year, dates)

    annees_list = list(annees)

    return annees_list


# Inverse les colonnes et les lignes d'un csv
def retourner_liste_imbriquee(liste):
    liste_imbriquee = []
    for i in range(len(liste[0])):
        element = []
        for j in range(len(liste)):
            element.append(liste[j][i])
        liste_imbriquee.append(element)
    return liste_imbriquee
            
# Edite un fichier CSV à partir d'une liste 
def editer_csv(list):
    with open("liste.csv", "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        doc = writer.writerows(list)
    return doc

# test les sorties des fonctions
def parcourir_liste(list):
    list_test =[]
    for row in list:
        print(row)
        print()

new_list = load_data(data) # Récupère le fichier CSV et le retour en liste
new_list = removeTitles(new_list) # Supprime les éléments vide de la liste
liste_int = convertir_int(new_list) # Convertis la liste de str en entier
liste_dates = convertir_en_date(liste_int) # Convertis la liste des timestamps en date
liste_annees = select_year(liste_dates)
liste_classe = ranger_colonnes(new_list, liste_dates, liste_annees)
inverser_liste = retourner_liste_imbriquee(liste_classe)
editer_csv(inverser_liste)


#test = parcourir_liste(liste_classe)

