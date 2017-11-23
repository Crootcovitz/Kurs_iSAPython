import smtplib
import dzien7.secrets

adresat = dzien7.secrets.login
nadawca = dzien7.secrets.login
haslo = dzien7.secrets.haslo

# tworzę silnik mailera
mailer = smtplib.SMTP('smtp.gmail.com', 587)
# witam się z serwerem/ łączę się
mailer.ehlo()
# szyfruję połączenie
mailer.starttls()
# loguję się
mailer.login(nadawca, haslo)

temat = 'Subject: Hello from Mateusz\n'
wiadomosc = 'To jest moja wiadomosc'
tresc = temat + wiadomosc

# wysyłam
mailer.sendmail(nadawca, adresat, tresc)
print('Wysłano maila!')

mailer.close()