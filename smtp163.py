import smtplib
from email.mime.text import MIMEText


mailto_list = [""]
mail_host = "smtp.163.com"
mail_user = ""
mail_pass = ""

def send_mail(to_list,sub,content):
    me = "小鸟游六花" + "<" + mail_user + ">"
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub  # 邮件主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        # print(server)
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me,to_list,msg.as_string())
        server.close()
        return True
    except:
        print("error")

if __name__ == "__main__":
    sub = "Rikka"
    content = '中二病'
    if send_mail(mailto_list,sub,content):
        print("发送成功")
    else:
        print("发送失败")