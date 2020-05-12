import smtplib
from email.mime.text import MIMEText
from email.header import Header
import csv



from_addr = input('your email adress:')
password = input("Password: ")

# server
smtp_server = 'smtp.gmail.com'


# 邮件内容
text='''nnmnnlk
fffllll
kml;m;mml;m;
'''


data = [['yhj ', 'hongjian.y@yahoo.com'],['YHJ', '273140844@qq.com']]

# write the receiver
with open('to_addrs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

# read the receiver
with open('to_addrs.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        to_addrs = row[1]
        msg = MIMEText(text,'plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addrs)
        msg['Subject'] = Header('python test')
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server, 465)
        server.login(from_addr, password)
        try:
            server.sendmail(from_addr, to_addrs, msg.as_string())
            print("You've sent an email! ")
        except:
            print("error! try it again! ")
# 关闭服务器
server.quit()