import requests
import ipaddress
from tabulate import tabulate


webapi="Your api key"
site="https://ipqualityscore.com/api/json/ip/{}/{}?strictness=0&allow_public_access_points=true&fast=true&lighter_penalties=true&mobile=true"

def valid_ip(address):
    try: 
        ipaddress.ip_address(address)
        return True
    except:
        return False   


while(True):
    ip = input("Enter the IP or nothing to stop the application !")
    if len(ip) == 0:
        print("Thanks for using me :)")
        break

    if not valid_ip(ip):
        print("Enter a vaild ip !")
        continue

    
    site=site.format(webapi,ip)
    response=requests.get(site)
    
    ls = []
    ls.append(['Vpn',response.json()['vpn']])
    ls.append(['Proxy',response.json()['proxy']])
    ls.append(['Tor',response.json()['tor']])
    print(tabulate(ls, headers=['Type', 'T/F']))
    

      
