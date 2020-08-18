""" Base de donnée MySQL-Python Pystorage
Application de stockage de donnée personnel """

import mysql.connector

def inserer(pydata, data):
  
  nom = input("Veuillez saisir votre nom : ")
  prenom = input("Veuillez saisir votre prenom : ")
  email = input("Veuillez saisir votre email : ")
  tel = input("Veuillez saisir votre numéro de télephone : ")
  mdp = input("Veuillez saisir votre mot de passe : ")

  sql = "INSERT INTO PyUser (nom, prenom, email, tel, MotDePasse) VALUES (%s, %s, %s, %s, %s)"

  val = (nom, prenom, email, tel, mdp)

  data.execute(sql, val)

  pydata.commit()

  print(data.rowcount, "Les données sont insérées.")


def MiseAjour(pydata, data):

  nom = input("Veuillez saisir votre nom : ")
  prenom = input("Veuillez saisir votre prenom : ")
  email = input("Veuillez saisir votre email : ")
  tel = input("Veuillez saisir votre numéro de télephone : ")
  mdp = input("Veuillez saisir votre mot de passe : ")

  sql = "UPDATE PyUser set nom='"+nom+"', prenom='"+prenom+"', email='"+email+"', tel='"+tel+"', MotDePasse='"+mdp

  data.execute(sql)

  pydata.commit()

  print(data.rowcount, "Les données sont modifiées.")


def visualiser(data):

  data.execute("SELECT * FROM PyUser")

  visu = data.fetchall()

  print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("+   nom   prénom   email   télephone   mot de passe +")
  print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")


  for i in visu:
    
    print(i)


def supprimer(pydata, data):

  nom = input("Saissiez le nom de l'utilisateur a supprimer : ")

  sql = "DELETE FROM PyUser WHERE nom ='"+nom+"' "

  data.execute(sql)

  pydata.commit()

  print(data.rowcount, "Données supprimée.")


def pydb():

  pydata = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="", # Entrer votre mot de passe d'utilisateur
    database="pybase"  # Entrer votre le nom de votre base de donnée
  )

  data = pydata.cursor()

  print("Bienvenue sur Pystorage ! Vous Pouvez inserer, modifier, visualiser et supprimer vos données.")

  print("Les options disponibles :")
  print("inserer")
  print("modifier")
  print("visualiser")
  print("supprimer")


  option = input("entrer l'action de votre choix : ")

  while True:

    if option == "inserer":
      inserer(pydata, data)
      break

    elif option == "modifier":
      MiseAjour(pydata, data)
      break

    elif option == "visualiser":
      visualiser(data)
      break

    elif option == "supprimer":
      supprimer(pydata, data)
      break

    else:
      print("Veuillez enter un action valide !")

pydb()




