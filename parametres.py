#!c:\\prg\\python36\\python.exe

# use python3


def InitParams():
   # connexion serveur mail
   params = dict()
   params["Expediteur"] = "Organisation FOSS4G-fr <foss4gfr@osgeo.asso.fr>"
   #
   # contenu du mail
   #
   params["Sujet"] = "Sponsorisation FOSS4G-fr 2018"
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


L'édition 2018 du FOSS4G-fr aura lieu du 15 au 17 mai dans les locaux de l'ENSG (École Nationale des Sciences Géographiques), à Marne-la-Vallée (accès depuis Paris par le RER A).<br />


Organisé par l'OSGeo-fr, cet événement est dédié à la Géomatique Open Source et aux données géographiques libres.<br />
Les précédentes éditions ont rencontré un réel succès, et réuni lors de la dernière édition près de 250 utilisateurs, développeurs et professionnels des SIG (Systèmes d'Information Géographique), pour une journée d'ateliers et deux jours de conférences.


Sur un format similaire, le comité d'organisation se donne, cette année,  comme ambition de réunir un public encore plus large de participants et conférenciers, issus de la communauté Open Source Geospatial francophone.
L'OSGeo-fr, association organisatrice de l'événement, recherche des sponsors pour financer cette rencontre.<br />
C'est "l'Evénement biennal de la Géomatique Open Source" qui permet aux participants d'assurer leur veille technologique.<br />
En tant qu'acteur de la Géomatique Open Source, soutenir l'événement vous permettra d'améliorer votre visibilité.<br />

Les trois niveaux de sponsorisation sont accessibles <a href="http://osgeo.asso.fr/foss4gfr-2018/sponsors.html#appel-sponsors">ici</a><br />


Espérant pouvoir compter sur votre soutien, nous restons à votre disposition pour tout complément d'information et remercions par avance $1 pour sa participation.<br />
Meilleures salutations.


L'équipe organisatrice du @FOSS4Gfr

'''

   # corps du mail en HTML
   # ATTENTION: à respecter l'ordre Prénom,Nom ou Nom,Prénom dans le fichier .csv
   params["HtmlBody"] = '''Bonjour $2,
<br /><br /><br />
L'édition 2018 du FOSS4G-fr aura lieu du 15 au 17 mai dans les locaux de l'ENSG (École Nationale des Sciences Géographiques), à Marne-la-Vallée (accès depuis Paris par le RER A).<br />
<br />
Organisé par l'OSGeo-fr, cet événement est dédié à la Géomatique Open Source et aux données géographiques libres.<br />
Les précédentes éditions ont rencontré un réel succès, et réuni lors de la dernière édition près de 250 utilisateurs, développeurs et professionnels des SIG (Systèmes d'Information Géographique), pour une journée d'ateliers et deux jours de conférences.
<br />
Sur un format similaire, le comité d'organisation se donne, cette année,  comme ambition de réunir un public encore plus large de participants et conférenciers, issus de la communauté Open Source Geospatial francophone.
L'OSGeo-fr, association organisatrice de l'événement, recherche des sponsors pour financer cette rencontre.<br />
C'est "l'Evénement biennal de la Géomatique Open Source" qui permet aux participants d'assurer leur veille technologique.<br />
En tant qu'acteur de la Géomatique Open Source, soutenir l'événement vous permettra d'améliorer votre visibilité.<br />
<br />
Les trois niveaux de sponsorisation sont accessibles <a href="http://osgeo.asso.fr/foss4gfr-2018/sponsors.html#appel-sponsors">ici</a><br />
<br />
Espérant pouvoir compter sur votre soutien, nous restons à votre disposition pour tout complément d'information et remercions par avance $1 pour sa participation.<br />
Meilleures salutations.

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