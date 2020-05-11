import smtplib
from email.mime.text import MIMEText

password = input("Password: ")
from_addr = 'hongjian.yuan@edu.escp.eu'
to_addr = 'hongjian.y@yahoo.com'
msg = MIMEText('send by python','plain','utf-8')
smtp_server = 'smtp.gmail.com'

server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
server.login(from_addr, password)

server.sendmail(from_addr, to_addr, msg.as_string())

server.quit()