import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host='smtp.XXX.com'#邮箱服务器
mail_user='xxx'#邮箱用户名
mail_password='xxxxx'#邮箱密码
sender='xx'#发送者
receiver=['XXXX']#接受者
#纯文本
#message=MIMEText('我是高明岗','plain','utf-8')
#Html文件
message = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
subject='测试'
message['Subject'] = Header(subject,'utf-8')
message['From'] = Header('高明岗','utf-8')
message['To'] = Header('测试','utf-8')
stmp=smtplib.SMTP()
stmp.connect(mail_host)
stmp.login(mail_user,mail_password)
stmp.sendmail(sender,receiver,message.as_string())
stmp.close()
print("邮件发送成功")
