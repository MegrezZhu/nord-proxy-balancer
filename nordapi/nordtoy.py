#!/usr/bin/python

'''
A brief example of some of the NordVPN api calls - simply dumps JSON results
'''

import requests 
import json
import hashlib
import argparse


parser = argparse.ArgumentParser(description='nordtoy')
group = parser.add_mutually_exclusive_group()
group.add_argument('-u','--userdata', nargs='*', dest='userdetails', help='my@email  mypassword', default='')
group.add_argument('-l','--serverload', nargs='*', dest='serverload', help='server domain', default='')
group.add_argument('-s','--serverstats', action='store_true')
group.add_argument('-d','--serverdetail',  action='store_true')
group.add_argument('-c','--config', action='store_true')
group.add_argument('-a','--address', action='store_true')
group.add_argument('-n','--nameserver', action='store_true')


ns=parser.parse_args()

# Get the indiviual server load
if ns.serverload:
    response = requests.get(
            url = 'https://api.nordvpn.com/server/stats/'+ns.serverload[0],
            headers = {
            'User-Agent': 'NordVPN_Client_5.56.780.0',
            'Host': 'api.nordvpn.com',  
            'Connection':'Close'
        }
        )
    
    print (response.text)
# Get user account details, using verified token    
elif ns.userdetails:
    response = requests.get(
        url = 'https://api.nordvpn.com/token/token/'+ns.userdetails[0],
        headers = {
        'User-Agent': 'NordVPN_Client_5.56.780.0',
        'Host': 'api.nordvpn.com',  
        'Connection':'Close'
    }
    )
    json_data=json.loads(response.text)
    #Uncomment next line if you want to see the JSON token, salt, key, response
    #print(response.text)
   
    #The response to validate the token is - salt+password, SHA512 hashed - then that hash+key, SHA512 hashed again
    firsthash=hashlib.sha512(json_data['salt'].encode()+ns.userdetails[1].encode())
    secondhash=hashlib.sha512(firsthash.hexdigest()+json_data['key'].encode())
    
    verifyurl='https://api.nordvpn.com/token/verify/'+json_data['token']+'/'+secondhash.hexdigest()
    # Validate token    
    response = requests.get(
        url = verifyurl,
        headers = {
        'User-Agent': 'NordVPN_Client_5.56.780.0',
        'Host': 'api.nordvpn.com',  
        'Connection':'Close'
    }
    )
    # Returns true if validated correctly
    print(response.text)
    # Display account details    
    response = requests.get(
        url = 'https://api.nordvpn.com/user/databytoken',
        headers = {
        'User-Agent': 'NordVPN_Client_5.56.780.0',
        'Host': 'api.nordvpn.com',  
        'nToken': json_data['token'],
        'Connection':'Close'
    }
    )
        
    print (response.text)
# Get current loads for all servers   
elif ns.serverstats:
    response = requests.get(
        url = 'https://api.nordvpn.com/server/stats',
        headers = {
        'User-Agent': 'NordVPN_Client_5.56.780.0',
        'Host': 'api.nordvpn.com',  
        'Connection':'Close'
    }
    )
        
    print (response.text)
# Get detailed information on all servers    
elif ns.serverdetail:
    response = requests.get(
        url = 'https://api.nordvpn.com/server',
        headers = {
        'User-Agent': 'NordVPN_Client_5.56.780.0',
        'Host': 'api.nordvpn.com',  
        'Connection':'Close'
    }
    )
        
    print (response.text)
# Download OpenVPN config files for all servers    
elif ns.config:
    response = requests.get(
        url = 'https://api.nordvpn.com/files/zipv2',
        headers = {
        'User-Agent': 'NordVPN_Client_5.56.780.0',
        'Host': 'api.nordvpn.com',  
        'Connection':'Close'
    }
    )
    
    with open("config.zip", "wb") as code:
        code.write(response.content)
# Get users current IP address   
elif ns.address:
    response = requests.get(
        url = 'https://api.nordvpn.com/user/address',
        headers = {
        'User-Agent': 'NordVPN_Client_5.56.780.0',
        'Host': 'api.nordvpn.com',  
        'Connection':'Close'
    }
    )
        
    print (response.text)
#Display NordVPN nameservers    
elif ns.nameserver:
    response = requests.get(
        url = 'https://api.nordvpn.com/dns/smart',
        headers = {
        'User-Agent': 'NordVPN_Client_5.56.780.0',
        'Host': 'api.nordvpn.com',  
        'Connection':'Close'
    }
    )
        
    print (response.text)
    
    
else:
    print("No options selected, options are -\n")
    print("-u, --userdata     -  -u my@email mypassword  - gives account details")
    print("-l, --serverload   -  -l au1.nordvpn.com      - shows server load as percentage ")
    print("-s, --serverstats  -  -s - lists server load for all servers")
    print("-d, --serverdetail -  -d - lists detailed information about all servers")
    print("-c, --config       -  -c - downloads OpenVPN config files for all servers to config.zip")
    print("-a, --address      -  -a - displays users IP address")
    print("-n, --nameserver   -  -n - displays NordVPN nameservers")
    