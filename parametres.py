#!c:\\prg\\python36\\python.exe

# use python3


def InitParams():
   # connexion serveur mail
   params = dict()
   params["Expediteur"] = "Organisation FOSS4G-fr <foss4gfr@osgeo.asso.fr>"
   #
   # contenu du mail
   #
   params["Sujet"] = "Elections bureau"
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

La clôture des listes électorales aura lieu dimanche 7 octobre à minuit. Tu n'es pour l'instant pas à jour de ta cotisation 2018.
Ce mail n'est pas destiné à faire du forcing mais simplement te permettre de voter pour élire le bureau si tu le désires.

Si tu ne veux pas renouveler ton adhésion, désolé pour le dérangement et bon week-end; si c'est un oubli, la procédure est indiquée ci-après...

Cordialement.

Jean-Marie

*PS: merci de nous indiquer si tu souhaites ne plus recevoir de communication de la part de l'association et résilier ton adhésion*


Pour te connecter sur Dolibarr, ton login est "$2" :

https://www.osgeo.asso.fr > ASSOCIATION > ESPACE ADHERENT

Concernant le règlement de ta cotisation, le lien Paypal n'est pas toujours opérationnel, dans ce cas, tu peux utiliser HelloAsso : <https://www.helloasso.com/associations/osgeo-fr/adhesions/adhesion-renouvellement-osgeo-fr>

Merci d'avance.

Bon week-end.


'''

   # corps du mail en HTML
   # ATTENTION: à respecter l'ordre Prénom,Nom ou Nom,Prénom dans le fichier .csv
   params["HtmlBody"] = '''Bonjour $1,
<br /><br />
La clôture des listes électorales aura lieu dimanche 7 octobre à minuit. Tu n'es pour l'instant pas à jour de ta cotisation 2018.
Ce mail n'est pas destiné à faire du forcing mais simplement te permettre de voter pour élire le bureau si tu le désires.
<br /><br />
Si tu ne veux pas renouveler ton adhésion, désolé pour le dérangement et bon week-end; si c'est un oubli, la procédure est indiquée ci-après...
<br /><br />
Cordialement.
<br /><br />
Jean-Marie
<br /><br />
<strong>PS: merci de nous indiquer si tu souhaites ne plus recevoir de communication de la part de l'association et résilier ton adhésion</strong>
<br /><br />
Pour te connecter sur Dolibarr, ton login est "$2" :
<br /><br />
https://www.osgeo.asso.fr > ASSOCIATION > <a href="http://osgeo.asso.fr/dolibarr/htdocs/">ESPACE ADHERENT</a> 
<br /><br />
Concernant le règlement de ta cotisation, le lien Paypal n'est pas toujours opérationnel, dans ce cas, tu peux utiliser <a href="https://www.helloasso.com/associations/osgeo-fr/adhesions/adhesion-renouvellement-osgeo-fr">HelloAsso</a>
<br /><br />
Merci d'avance.
<br />
Bon week-end.
<br /><br />
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