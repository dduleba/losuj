import smtplib, ssl
import random
from getpass import getpass
import yagmail
 
do_losowania = {
'x':'x@l.a.s.y.d',
'y':'y@l.a.s.y.d',
}
a = list(do_losowania.keys())
x = a[:]
 
while [i for i in x if x.index(i) == a.index(i)]:
        print(x)
        print(a)
        random.shuffle(x)
	
b= dict(zip(a, x))


context = ssl.create_default_context()

#with smtplib.SMTP(smtp_server, port) as server:
#server = smtplib.SMTP('smtp.gmail.com', 587)
#server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
#server = smtplib.SMTP('localhost')

email = input("Type your mail and press enter: ")

#password = getpass(prompt="Password: ", stream=None)
#server.starttls(context=context)
#server.login(email, password)

yag = yagmail.SMTP(email) 
for i,j in b.items():
        drogie = "Droga" if i.endswith('a') else 'Drogi'
        sub='Wylosowalismy Tobie osobe dla ktorej prosimy zebys zakupil prezent na swieta'
        msg = "%s %s prosze kup prezent dla %s" %(drogie, i, j)
        print(msg)
        #server.sendmail("test@my-domain.ort.pl", do_losowania[i].lower(), msg)
        #server.send_message(email, do_losowania[i].lower(), msg)
        # pamietaj wylaczyc zabezpieczenie na gmailu
        yag.send(subject=sub, to=do_losowania[i].lower(), contents=msg)
	
#server.quit()
