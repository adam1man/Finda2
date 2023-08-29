from bs4 import BeautifulSoup


def Check_Smtp_Host(host, NUM):
    port = 587
    host = str(host)
       
    if "azure-dns" in host:
        host = "smtp-mail.outlook.com"
        
    elif "protection.outlook.com" in host:
        host = "smtp-mail.outlook.com"

    elif "ultradns" in host:
        host = "smtp.mail.com"
        
    elif "azure-dns.info" in host:
        host = "smtp.office365.com"
    
    elif 'att.net' in host:
        host = "smtp.mail.att.net"
            
    elif "hostgator" in host:
        host = "gator1234.hostgator.com"
    
    elif "yahoo" in host:
        host = "smtp.mail.yahoo.com"
            
    elif "interia" in host:
        host = "poczta.interia.pl"

    elif 'comcast' in host:
        host = "smtp.comcast.net"
    
    elif "1and1" in host:
        host = "smtp.ionos.com"
          
    elif "google.com" in host:
        host = "smtp.gmail.com"
         
    elif "ui-dns.org" in host:
        host = "mail.gmx.net"
            
    elif "gmx.net" in host:
        host = "smtp.gmx.com"
 
    elif "101domain.com" in host:
        host = "mail.mailspot.info"
         
    elif "ovh.net" in host:
        host = "ssl0.ovh.net"
                   
    elif "t-ipnet.de" in host:
        host = "securesmtp.t-online.de"
       
    elif "freenet.de" in host:
        host = "mx.freenet.de"
       
    elif "onet.pl" in host:
        host = "smtp.poczta.onet.pl"
    
    elif "netvision" in host:
        host = "mailgw.netvision.net.il"
       
    elif "movistar" in host:
        host = "smtp.movistar.es"
        port = 25
    
    elif NUM == 0:
        host = "smtp."+host
    elif NUM == 1:
        host = "mail."+host
    elif NUM == 2:
        host = "webmail."+host
    
    else:
        host = "webmail."+host
    return host, port


def Choose_Serva(file_to_open, line_to_check): # Function to choose smtp send
    with open(file_to_open,'r') as S_list:
        S_list = S_list.readlines() #read lines one by one from file 
        SMTP = S_list[line_to_check] #select items from index of the list
        SMTP = SMTP.strip()
        SMTP = str(SMTP)
        Host = SMTP.partition(':')[0]
        SMTP_ = SMTP.partition(':')[2]
        Port = SMTP_.partition(':')[0]
        SMTP_Logs = SMTP_.partition(':')[2]
        Email = SMTP_Logs.partition(':')[0]
        Pwd = SMTP_Logs.partition(':')[2]
    return Host, Port, Email, Pwd
    
    

