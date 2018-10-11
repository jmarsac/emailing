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

$2 est sponsor Or du FOSS4G-FR 2018 qui a lieu la semaine prochaine. A ce titre, un créneau vous est réservé pour une présentation de 15 mn.

Afin de ne pas perdre de temps lors de votre présentation, nous vous proposons de nous transmettre au plus vite votre support pour la rendre disponible sur les ordinateurs des amphithéâtres.
Merci de l'adresser à foss4gfr@osgeo.asso.fr
Pour des raisons de sécurité il n'est pas possible de faire de démo en ligne ; privilégier les vidéos depuis le PDF (format avi)
Afin de nous faciliter la vie, voici les consignes de nommage de votre support  :

(16|17)mai_(Cauchy|Picard|Bienvenue)_NomPConférencier-Structure.extension

A titre d'exemple : 16mai_Cauchy_Bossaert-CENLR.pdf

Nous vous rappelons qu'il n'y aura pas d'accès Internet depuis les ordinateurs mis à disposition pour les présentations.

Pensez également à apporter deux totems à placer dans chacun des grands amphis de la conférence.

Vous pourrez installer votre stand dès lundi 14 de 16h à 18h ou mardi 15 à partir de 9h. Le réseau ne sera opérationnel que mardi 15 au matin.

Un plan d'implantation du site est disponible : <https://github.com/OSGeo-fr/FOSS4G-fr/blob/master/logistique/foss4g-fr-2018.pdf>

En vous remerciant encore de votre soutien, à bientôt.
L'équipe organisatrice du @FOSS4Gfr,
'''

   # corps du mail en HTML
   # ATTENTION: à respecter l'ordre Prénom,Nom ou Nom,Prénom dans le fichier .csv
   params["HtmlBody"] = '''Bonjour $1,
<br /><br />
$2 est sponsor Or du FOSS4G-FR 2018 qui a lieu la semaine prochaine. A ce titre, un créneau vous est réservé pour une présentation de 15 mn.
<br /><br />
Afin de ne pas perdre de temps lors de votre présentation, nous vous proposons de nous transmettre au plus vite votre support pour la rendre disponible sur les ordinateurs des amphithéâtres.
<br /><br />
Merci de l'adresser à <a href="mailto:foss4gfr@osgeo.asso.fr">foss4gfr@osgeo.asso.fr</a>
<br /><br />
Pour des raisons de sécurité il n'est pas possible de faire de démo en ligne ; privilégier les vidéos depuis le PDF (format avi)
<br /><br />
<strong>Afin de nous faciliter la vie, voici les consignes de nommage de votre support </strong> :
<br /><br />
(16|17)mai_(Cauchy|Picard|Bienvenue)_NomPConférencier-Structure.extension
<br /><br />
A titre d'exemple : 16mai_Cauchy_Bossaert-CENLR.pdf
<br /><br />
Nous vous rappelons qu'il n'y aura pas d'accès Internet depuis les ordinateurs mis à disposition pour les présentations.
<br /><br /><br />
Pensez également à apporter deux totems à placer dans chacun des grands amphis de la conférence.
<br /><br />
Vous pourrez installer votre stand dès lundi 14 de 16h à 18h ou mardi 15 à partir de 9h. Le réseau ne sera opérationnel que mardi 15 au matin.
<br /><br />
Un <a href="https://github.com/OSGeo-fr/FOSS4G-fr/blob/master/logistique/foss4g-fr-2018.pdf">plan d'implantation du site est disponible</a>
<br /><br />

En vous remerciant encore de votre soutien, à bientôt.<br /><br />
L'équipe organisatrice du <a href="https://twitter.com/foss4gfr">@FOSS4Gfr</a>'''
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