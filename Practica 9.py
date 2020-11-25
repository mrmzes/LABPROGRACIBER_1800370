import smtplib
import getpass

smtpObject = smtplib.SMTP('smtp.gmail.com', 587)
smtpObject.ehlo()
smtpObject.starttls()

account = str(input('Ingresa el correo con el cual quieres enviar(GMAIL): '))
password = getpass.getpass()
smtpObject.login(account,password)

to = str(input('Ingresa el correo al cual le quieres enviar: '))
subject = str(input('Ingresa el asunto del correo: '))
cuerpo = str(input('Ingresa el cuerpo del correo: '))
mail = subject + cuerpo

smtpObject.sendmail(account,to,mail)

smtpObject.quit()