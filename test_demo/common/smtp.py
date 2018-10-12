import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# -----------1、发件相关的参数---------------
smtpserver = "smtp.163.com"  # 发件服务器
port = 0  # 端口
sender = "m18581893850@163.com"  # 发件人
psw = "wp635889832"  # 密码
receiver = "635889832@qq.com"  # 收件人
# receiver = ["639889836@qq.com", "635889845@qq.com"] # 群发用列表

# -----------2、编辑邮件内容---------------
# -----------2、1只发送邮件---------------
subject1 = "测试报告"
body = '<p>发送测试报告</p>'  # 邮件正文用html格式
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = receiver
msg['subject'] = subject1
# -----------2、2发送附件-------------------
# 读文件
subject2 = "发送测试报告html"
file_path = os.path.join("..\\report\\report.html")
with open(file_path, "rb") as fp:
    mail_body = fp.read()
msg = MIMEMultipart()
msg["from"] = sender  # 发件人
msg["to"] = receiver  # 收件人
# msg["to"] = ";".join(receiver)         # 群发收件人
msg["subject"] = subject2  # 主题
# 正文
body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)
# 附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)

# ----------3、发送邮件---------------------
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)  # 连服务器
    smtp.login(sender, psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)  # 登录
smtp.sendmail(sender, receiver, msg.as_string())  # 发送
smtp.quit()  # 关闭
