#!c:\\prg\\python36\\python.exe

# use python3


# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

import time
import csv
import getopt, sys
import mail_logo
import yaml

from optparse import OptionParser
from parametres import InitParams

def main():
   msgUsage = "usage: %prog --csvfile=<csvfilepath> --server=<smtp_filepath> --password=<motdepasse>"
   parser = OptionParser(usage=msgUsage, version="%prog 1.0")
   parser.add_option("-s", "--server", dest="smtpfile",
                  help="Fichier Yaml de configuration du serveur SMTP")
   parser.add_option("-c", "--csvfile", dest="csvfile",
                  help="Fichier csv des destinataires")
   parser.add_option("-w", "--password", dest="password",
                  help="Mot de passe")
   #parser.add_option("-q", "--quiet",
   #               action="store_false", dest="verbose", default=True,
   #               help="don't print status messages to stdout")

   (options, args) = parser.parse_args()

   try:
   
      print('Emailing depuis le fichier "' + options.csvfile + '"')
      
      print('Configuration serveur dans  "' + options.smtpfile + '"')
      with open(options.smtpfile, 'r') as ymlfile:
         cfg = yaml.load(ymlfile)

      for section in cfg:
         print(section + ':')
         print("  server: " + cfg['smtp']['server'])
         print("  user: " + cfg['smtp']['user'])
         print("  port: " + str(cfg['smtp']['port']))
         print("  nbmax: " + str(cfg['smtp']['nbmax']) + ' mails')
         print("  delay: " + str(cfg['smtp']['delay']) + ' secondes')
      
      p = InitParams()

      cr = csv.reader(open(options.csvfile,"r", encoding='utf-8'),delimiter=',', quotechar='"')
      nbmax = cfg['smtp']['nbmax']
      tempo = cfg['smtp']['delay']

      idx = 0
      for row in cr:
         idx += 1
         if idx % nbmax == 0:
            print("Attente " + str(tempo) + " secondes...")
            time.sleep(tempo)
         
         htmlBody = p["HtmlBody"]
         if p["$1"] >= 0:
            htmlBody = htmlBody.replace("$1",row[p["$1"]])
         if p["$2"] >= 0:
            htmlBody = htmlBody.replace("$2",row[p["$2"]])
         if p["$3"] >= 0:
            htmlBody = htmlBody.replace("$3",row[p["$3"]])
         if p["$4"] >= 0:
            htmlBody = htmlBody.replace("$4",row[p["$4"]])
         if p["$5"] >= 0:
            htmlBody = htmlBody.replace("$5",row[p["$5"]])
         if p["$6"] >= 0:
            htmlBody = htmlBody.replace("$6",row[p["$6"]])
         if p["$7"] >= 0:
            htmlBody = htmlBody.replace("$7",row[p["$7"]])
         if p["$8"] >= 0:
            htmlBody = htmlBody.replace("$8",row[p["$8"]])
         if p["$9"] >= 0:
            htmlBody = htmlBody.replace("$9",row[p["$9"]])

         textBody = p["TextBody"]       
         if p["$1"] >= 0:
            textBody = textBody.replace("$1",row[p["$1"]])
         if p["$2"] >= 0:
            textBody = textBody.replace("$2",row[p["$2"]])
         if p["$3"] >= 0:
            textBody = textBody.replace("$3",row[p["$3"]])
         if p["$4"] >= 0:
            textBody = textBody.replace("$4",row[p["$4"]])
         if p["$5"] >= 0:
            textBody = textBody.replace("$5",row[p["$5"]])
         if p["$6"] >= 0:
            textBody = textBody.replace("$6",row[p["$6"]])
         if p["$7"] >= 0:
            textBody = textBody.replace("$7",row[p["$7"]])
         if p["$8"] >= 0:
            textBody = textBody.replace("$8",row[p["$8"]])
         if p["$9"] >= 0:
            textBody = textBody.replace("$9",row[p["$9"]])

         if options.password:
            mail_logo.EnvoyerCarte(cfg['smtp']["server"],cfg['smtp']["port"],cfg['smtp']["user"],options.password,p["Expediteur"],
               row[p["IndiceEmail"]],
               p["Sujet"],
               p["Logo"],
               htmlBody,
               textBody)
         else:
            print(msgUsage.replace('%prog','emailing.py'))
            break;

   except Exception as e:
      print(msgUsage.replace('%prog','emailing.py'))


if __name__ == "__main__":
    main()