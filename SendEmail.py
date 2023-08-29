from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formatdate
#rom ConnectSock5 import *
from Maker import *
import smtplib, ssl
import email.utils as utils
from email import *


def Send_Email(host_, port_, senda_email_, pwd_, recv_email_, msg_file_, senda_name_, subject_):
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject_
    msg['From'] = f"{senda_name_} <{senda_email_}>"
    msg['To'] = recv_email_
    msg['Date'] = formatdate(localtime=True)
    msg['message-id'] = utils.make_msgid(domain='google.com')

    plain_txt_msg = f'''{recv_email_}\n{ pwd_}\n{host_}\n{port_}'''
    
    html_msg = f'''{recv_email_}\n{ pwd_}\n{host_}\n{port_}''' #setting html message by calling string checker function to replace strings.
   
    msg_txt_part = MIMEText(plain_txt_msg, 'plain')
    msg_html_part = MIMEText(html_msg, 'html')
    msg_html_part['Content-Type'] = 'text/html; charset="iso-8859-1'
    
    msg.attach(msg_txt_part)
    msg.attach(msg_html_part)
    
    
    
    try:
        server = smtplib.SMTP(host_, port_, timeout=25) #connect to the smtp server 
        
        server.login(senda_email_,pwd_)
        server.sendmail(senda_email_, recv_email_, msg.as_string())
        return 0 # means success
    except smtplib.SMTPAuthenticationError:
        return 1 # means login Failed
    except smtplib.SMTPServerDisconnected:
        return 2 #means connection error
    except Exception as e:
        return e
 


def Connect_Smtp_serva(host, port):
    host = str(host).strip()
    port = int(port)
    try:
        server = smtplib.SMTP(host, port, timeout=5)
        server.starttls()
        return True
    except smtplib.SMTPConnectError:
        return False
    except Exception as e:
        e = str(e)
        if "No route to host" in e:
            return 'Internet Error'
        else:
            return False
    
   
def Login_(smtp_host, port, email, pwd):
    try:
        #connect_color = Fore.RED
        server = smtplib.SMTP(smtp_host, port, timeout=5)
        server.starttls()
        #connect_color = Fore.MAGENTA
        server.login(email, pwd)
        #print(Fore.GREEN + f"[Login Success] [{smtp_host}:{port}] [{email} : {pwd} ]")
        return True
    except smtplib.SMTPAuthenticationError:
        #print(connect_color + f'[Login Failed] [{smtp_host}:{port}] [{email} : {pwd} ]')
        return False
    except Exception as e:
        #print(connect_color + f'[Connection Error] [{smtp_host}:{port}] Reason: [{e}]')
        return False
    

