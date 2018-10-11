#!c:\\prg\\python36\\python.exe

# use python3


def InitParams():
   # connexion serveur mail
   params = dict()
   params["Expediteur"] = "Organisation FOSS4G-fr <foss4gfr@osgeo.asso.fr>"
   #
   # contenu du mail
   #
   params["Sujet"] = "FOSS4G-fr 2018"
   # emplacement du fichier logo inséré après la signature
   params["Logo"] = "logo\\osgeo.fr.svg-222x85.png"
   #
   # indice du champ contenant l'adresse email dans le csv (le 1er champ du csv a l'indice 0)
   params["IndiceEmail"] = 0
   #
   # Paramètres facultatifs
   #
   # indices des champs utilisés en tant que paramètres ($1 à $9) dans le corps du mail
   # NB le 1er champ du csv a l'indice 0; si -1 le paramètre n'est pas utilisé
   # ATTENTION: à respecter l'ordre Prénom,Nom ou Nom,Prénom dans le fichier .csv
   #
   # le paramétrage ci-dessous correspond à .csv de la forme:
   # 
   # email@domaine.fr,nom,prenom

   # pour $1 ...
   params["$1"] = 2
   # pour $2 ...
   params["$2"] = -1
   params["$3"] = -1
   params["$4"] = -1
   params["$5"] = -1
   params["$6"] = -1
   params["$7"] = -1
   params["$8"] = -1
   params["$9"] = -1

   # corps du mail en texte
   # ATTENTION: à respecter l'ordre Prénom,Nom ou Nom,Prénom dans le fichier .csv
   params["TextBody"] = '''Bonjour $1,

L'Appel à Présentations du FOSS4G Fr est encore ouvert jusqu'au 15 Mars !


https://www.osgeo.asso.fr/foss4gfr-2018/programme.html


Nous te contactons car, sur l'une des éditions précédentes du FOSS4G Fr,
ta participation via une présentation ou l'animation d'un atelier
avait contribué au succès de l'événement.


Si pour cette nouvelle édition,
tu as de nouvelles thématiques à partager ou à mettre en avant,
n'hésites pas à nous pousser une proposition, ou plusieurs, le cas échéant :)


N'hésites pas, non plus, à relayer ce message dans tes cercles !


Dans les nouveautés saillantes de cette édition,
une volonté d'ouvrir les thématiques (et donc les publics présents).




Contacts:

Site Web: https://www.osgeo.asso.fr/foss4gfr-2018

Twitter:  @foss4gfr

Mail:     programme@osgeo.asso.fr


A bientôt
'''

   # corps du mail en HTML
   # ATTENTION: à respecter l'ordre Prénom,Nom ou Nom,Prénom dans le fichier .csv
   params["HtmlBody"] = '''Bonjour $1,
<br /><br />
L'Appel à Présentations du FOSS4G Fr est encore ouvert jusqu'au 15 Mars !
<br />
<a href="https://www.osgeo.asso.fr/foss4gfr-2018/programme.html">https://www.osgeo.asso.fr/foss4gfr-2018/programme.html</a>
<br />
<br />
Nous te contactons car, sur l'une des éditions précédentes du FOSS4G Fr,
ta participation via une présentation ou l'animation d'un atelier
avait contribué au succès de l'événement.
<br />
<br />

Si pour cette nouvelle édition,
tu as de nouvelles thématiques à partager ou à mettre en avant,
n'hésites pas à nous pousser une proposition, ou plusieurs, le cas échéant :)
<br />
<br />

N'hésites pas, non plus, à relayer ce message dans tes cercles !
<br />
<br />

Dans les nouveautés saillantes de cette édition,
une volonté d'ouvrir les thématiques (et donc les publics présents).

<br />

<br />

Contacts:
<br />
Site Web: <a href="https://www.osgeo.asso.fr/foss4gfr-2018/">https://www.osgeo.asso.fr/foss4gfr-2018</a>
<br />
Twitter:  <a href="https://twitter.com/osgeofr">@foss4gfr</a>
<br />
Mail:     <a href="mailto:programme@osgeo.asso.fr">programme@osgeo.asso.fr</a>
<br />
<br />
A bientôt
'''
   return params

def main():
   row = ["Zenith","Charles"]
   p = InitParams()
   print ("SmtpServer " + p["SmtpServer"])
   hb = p["HtmlBody"]
   if p["$1"] >= 0:
      hb = hb.replace("$1",row[p["$1"]])
   if p["$2"] >= 0:
      hb = hb.replace("$2",row[p["$2"]])
   if p["$3"] >= 0:
      hb = hb.replace("$3",row[p["$3"]])
   if p["$4"] >= 0:
      hb = hb.replace("$4",row[p["$4"]])
   if p["$5"] >= 0:
      hb = hb.replace("$5",row[p["$5"]])
   if p["$6"] >= 0:
      hb = hb.replace("$6",row[p["$6"]])
   if p["$7"] >= 0:
      hb = hb.replace("$7",row[p["$7"]])
   if p["$8"] >= 0:
      hb = hb.replace("$8",row[p["$8"]])
   if p["$9"] >= 0:
      hb = hb.replace("$9",row[p["$9"]])
   print ("HtmlBody:\n" + hb)
   
if __name__ == "__main__":
    main()