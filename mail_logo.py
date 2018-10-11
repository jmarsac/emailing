#!c:\\prg\\python36\\python.exe

# use python3


# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

def EnvoyerCarte(smtpServer,smtpPort,loginId,loginPwd,expediteur,destinataire,sujet,logoFile,htmlBody,textBody):

	if htmlBody:
		# Create the root message and fill in the from, to, and subject headers
		msgRoot = MIMEMultipart('related')
	else:
		msgRoot = MIMEText(textBody,'plain','utf-8')
		
	msgRoot['Subject'] = Header(sujet, 'utf-8')
	if expediteur.find(loginId) < 0:
		msgRoot['From'] = Header(expediteur, 'utf-8')
	msgRoot['Reply-to'] = Header(expediteur, 'utf-8')
	msgRoot['To'] = Header(destinataire, 'utf-8')

	if htmlBody:
		msgRoot.preamble = 'This is a multi-part message in MIME format.'
		# Encapsulate the plain and HTML versions of the message body in an
		# 'alternative' part, so message agents can decide which they want to display.
		msgAlternative = MIMEMultipart('alternative')
		msgRoot.attach(msgAlternative)

		# We reference the image in the IMG SRC attribute by the ID we give it below
		if os.path.exists(logoFile):
			htmlText = htmlBody + '</p><p><img src="cid:image1" />'
		else:
			htmlText = htmlBody
		msgText =  MIMEText(htmlText,'html','utf-8')
		msgAlternative.attach(msgText)

		msgText =  MIMEText(textBody,'plain','utf-8')
		msgAlternative.attach(msgText)

		# This example assumes the image is in the current directory
		if os.path.exists(logoFile):
			fp = open(logoFile, 'rb')
			msgImage = MIMEImage(fp.read())
			fp.close()

			# Define the image's ID as referenced above
			msgImage.add_header('Content-ID', '<image1>')
			msgRoot.attach(msgImage)

	# Send the email (this example assumes SMTP authentication is required)
	import smtplib

	# Send the message via local SMTP server.
	try:
		smtp_ie = 0
		smtpObj = smtplib.SMTP(smtpServer, smtpPort)
		#smtpObj.set_debuglevel(True)	
		# identify ourselves, prompting server for supported features
		smtpObj.ehlo()

		# If we can encrypt this session, do it
		if smtpObj.has_extn('STARTTLS'):
			smtpObj.starttls()
			smtpObj.ehlo() # re-identify ourselves over TLS connection
			
		smtpObj.login(loginId, loginPwd)
		smtp_ie = smtpObj.sendmail(expediteur, destinataire, msgRoot.as_string())
		smtpObj.quit()
		print("\t",end="\t")
		info = "Expédié à " + destinataire
		print(info)
		
	except smtplib.SMTPServerDisconnected:
		info = "Impossible d'envoyer le courriel à " + destinataire + " (err " + str(smtplib.SMTPServerDisconnected) + ")"
		print(info)
	except smtplib.SMTPResponseException:
		info = "Impossible d'envoyer le courriel à " + destinataire + " (err " + str(smtplib.SMTPResponseException) + ")"
		print(info)
	except smtplib.SMTPSenderRefused:
		info = "Impossible d'envoyer le courriel à " + destinataire + " (err " + str(smtplib.SMTPSenderRefused) + ")"
		print(info)
	except smtplib.SMTPRecipientsRefused:
		info = "Impossible d'envoyer le courriel à " + destinataire + " (err " + str(smtplib.SMTPRecipientsRefused) + ")"
		print(info)
	except smtplib.SMTPDataError:
		info = "Impossible d'envoyer le courriel à " + destinataire + " (err " + str(smtplib.SMTPDataError) + ")"
		print(info)
	except smtplib.SMTPConnectError:
		info = "Impossible d'envoyer le courriel à " + destinataire + " (err " + str(smtplib.SMTPConnectError) + ")"
		print(info)
	except smtplib.SMTPHeloError:
		info = "Impossible d'envoyer le courriel à " + destinataire + " (err " + str(smtplib.SMTPHeloError) + ")"
		print(info)
	except smtplib.SMTPAuthenticationError:
		info = "Impossible d'envoyer le courriel à " + destinataire + " (err " + str(smtplib.SMTPAuthenticationError) + ")"
		print(info)
	except Exception:
		info = "Impossible d'envoyer le courriel à " + destinataire + " (err " + str(Exception) + ")"
		print(info)
