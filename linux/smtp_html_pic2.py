__author__ = 'jefby'
# coding=utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr
import smtplib

#格式化邮件地址
def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr(( \
        Header(name,'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr,unicode) else addr \
    ))
from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = raw_input('SMTP server: ')
#邮件对象
msg = MIMEMultipart()
#msg = MIMEText('<html><body><h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>..</p>' + '</body></html>','html','utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' %from_addr)
msg['To']=_format_addr(u'管理员 <%s>'% to_addr)
msg['Subject'] = Header(u'来自SMTP的问候...','utf-8').encode()

#邮件正文是MIMEText
msg.attach(MIMEText('<html><body><h1>Hello</h1>'+\
                    '<p><img src="cid:0"></p>'+\
                    '</body></html>','html','utf-8'))

#添加附件就是加上一个MIMEBase,从本地读取一个图片
with open('c:\Yuri-SNSD-2.png','rb') as f:
    #设置附件的MIME和文件名，
    mime = MIMEBase('image','png',filename='Yuri-SNSD-2.png')
    #加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='Yuri-SNSD-2.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')

    #把附件的内容读进来
    mime.set_payload(f.read())
    #用Base64编码
    encoders.encode_base64(mime)
    #添加到MIMEMultipart
    msg.attach(mime)

server = smtplib.SMTP(smtp_server,25)#SMTP的默认端口号是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())#MIMEText对象变成str
server.quit()


