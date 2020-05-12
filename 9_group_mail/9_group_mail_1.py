# Using list to sent group mail

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# from address
password = input("Password: ")
from_addr = 'hongjian.yuan@edu.escp.eu'

# to address
to_addr = ['hongjian.y@yahoo.com', '273140844@qq.com']

# server
smtp_server = 'smtp.gmail.com'

# content
text = '''jifjqljfljqljldq
fqjldjflqjdl
nfqndfklnqlks
fqldlqj
'''
msg = MIMEText(text,'plain','utf-8')

# information
msg['From'] = Header(from_addr)
msg['To'] = Header(','.join(to_addr))
msg['Subject'] = Header('Python test')

# connect
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)

# log in
server.login(from_addr, password)

# send email
server.sendmail(from_addr, to_addr, msg.as_string())

# close the server
server.quit()