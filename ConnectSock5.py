import socket, socks, requests
import smtplib

#https://ipapi.co/json/  

def connectProxy(proxy_Host, proxy_Port, proxy_in_use):
    proxy_Port = int(proxy_Port)
    proxy_Host = str(proxy_Host)
    
    try:
         connection_type = str(proxy_in_use)
         if connection_type == 'http':
            TYPE = socks.HTTP
         elif connection_type == 'sock4':
            TYPE = socks.SOCKS4
         elif connection_type == 'sock5':
            TYPE = socks.SOCKS5
         
         socks.set_default_proxy(TYPE, proxy_Host, proxy_Port)
         socket.socket = socks.socksocket
         socket.setdefaulttimeout(5)
         r = requests.get('http://icanhazip.com', timeout=5)
         if proxy_Host in str(r.text):
            print(proxy_Host, proxy_Port)
            return True
         
    except Exception as e:
        print(e)
        socks.set_default_proxy(socks.SOCKS5, 'localhost')
        pass
    
    
    #socks4 socks.set_default_proxy(socks.SOCKS, sock_host, sock_port)
    #http socks.set_default_proxy(socks.HTTP, sock_host, sock_port)
    

def Login_(smtp_host, port, email, pwd):
    try:
        server = smtplib.SMTP(smtp_host, port, timeout=10)
        server.starttls()
        server.login(email, pwd)
        return True
    except smtplib.SMTPAuthenticationError:
        return False
    except Exception as e:
        return False
    
