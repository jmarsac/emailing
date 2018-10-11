# À propos d'emailing

**emailing.py** est un script **python3** utilisé pour envoyer des emails sans avoir besoin d'autre chose qu'un compte email et un fichier csv contenant au moins les adresses email de vos destinataires.

Les paramètres de connexion sont définis dans un fichier .yml (à l'exclusion du mot de passe qui doit être passé en argument de la ligne de commande).

Les autres paramètres, notamment le libellé du courriel, sont définis dans le fichier *parameters. py*. 

Il est possible de l'exécuter en lui donnant le chemin du fichier csv et le nom du fichier de connexion (.yml) ainsi que le mot de passe de votre compte de messagerie:

    python emailing.py --csvfile="adresses.csv" --server="smtp.yml" --password="motdepasse".

## Paramètres connexion serveur smtp:

Dans un fichier YAML (ex: smtp.yml)
 - *server*: nom du serveur de messagerie ("smtp.googlemail.com")
 - *port*: numéro de port (587)
 - *user*: identifiant de connexion au compte mail
 - *nbmax*: nombre maximum de mails envoyés avant une pause de *delay* secondes (10)
 - *delay*: délai en secondes entre chaque série de *nbmax* mails (200)

## Paramètres généraux:

 - *Expéditeur*: adresse e-mail de l'expéditeur ("Nom")
 - *Sujet*: objet du mail ("OSGeo-fr")
 - *Logo*: chemin d'accès au fichier du logo ("logo-osgeofr222x63. png")
 - *IndiceEmail*: indice du champ csv contenant l'adresse email.
 *NB: les indices commencent à 0*

## Contenu du courrier:

### Texte en clair (obligatoire)
 - *TextBody*: contenu du mail en texte brut. Ex:
 
`params["TextBody"] = "Bonjour $1,\nConnaissez-vous OSGeo-fr (https://www.osgeo.asso.fr) ?"`
	
### Contenu HTML (obligatoire mais valeur optionnelle)
 - *HtmlBody*: contenu du mail en HTML. Ex: 

`params["HtmlBody"] = '''<p>Bonjour $1,
	<br />
	Connaissez-vous <a href="https://www.osgeo.asso.fr">OSGeo-fr</a></p>'''`

*Ce paramètre doit être défini mais peut être une chaîne vide*

## Paramètres pour variables optionnelles:
Dans le contenu de votre mail, vous pouvez utiliser 9 variables numérotées de 1 à 9 et identifiées par $i ($1, $2,..., $9)

Vous pouvez définir 9 index personnalisés ($i) pour définir la valeur du champ csv à inclure dans le contenu de votre mail.

Le script substituera leurs valeurs aux variables ($1 à $9). Les index commencent à 0, donc la valeur *-1* signifie *inutilisé*.
 - *$1*: indice du champ csv qui se substitue à *$1* (par défaut *-1*)
 - *$2*: indice du champ csv qui se substitue à *$2* (par défaut *-1*)
 - *$3*: indice du champ csv qui se substitue à *$3* (par défaut *-1*)
 - *$4*: indice du champ csv qui se substitue à *$4* (par défaut *-1*)
 - *$5*: indice du champ csv qui se substitue à *5$* (par défaut *-1*)
 - *$6*: indice du champ csv qui se substitue à *$6* (par défaut *-1*)
 - *$7*: indice du champ csv qui se substitue à *$7* (par défaut *-1*)
 - *$8*: indice du champ csv qui se substitue à *$8* (par défaut *-1*)
 - *$9*: indice du champ csv qui se substitue à *9$* (par défaut *-1*)
