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

Nous vous avons sollicité(e) il y a une dizaine de jours afin d'avoir vos retours sur la dernière édition du FOSS4G-fr.

Vous avez été nombreux à participer mais quelques uns manquent à l'appel !

*Vous avez jusqu'au 12 juin pour y répondre <https://goo.gl/forms/Jn4inQHfdnSoL8853> !*
			
Votre avis est important pour les prochaines éditions et cela ne vous prendra que quelques minutes.

Nous partagerons avec vous les résultats rapidement.

Merci par avance de votre participation !

L'équipe organisatrice du @FOSS4Gfr

/Si vous avez déjà répondu à notre sondage, ne tenez pas
            compte de cet email./
'''

   # corps du mail en HTML
   # ATTENTION: à respecter l'ordre Prénom,Nom ou Nom,Prénom dans le fichier .csv
   params["HtmlBody"] = '''Bonjour $1,
<br /><br />
Nous vous avons sollicité(e) il y a une dizaine de jours afin d'avoir vos retours sur la dernière édition du FOSS4G-fr.
<br />
Vous avez été nombreux à participer mais quelques uns manquent à l'appel !
<br /><br />
<strong>Vous avez jusqu'au 12 juin pour y répondre grâce à ce <a href="https://goo.gl/forms/7puTKhZaFthZZ9u93">formulaire</a> !</strong>
<br />
Votre avis est important pour les prochaines éditions et cela ne vous prendra que quelques minutes.
<br /><br />
Nous partagerons avec vous les résultats rapidement.
<br /><br />
Merci par avance de votre participation !
<br /><br />
L'équipe organisatrice du <a href="https://twitter.com/foss4gfr">@FOSS4Gfr</a>
<br /><br />
/Si vous avez déjà répondu à notre sondage, ne tenez pas compte de cet email./

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