import time
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://hmanager.cm-alenquer.pt/acct-webapp/'
extension = open('/opt/wordlists/common.txt', 'r')

#print(extension.read())

for i in extension:
    response = requests.get(url + i.strip(), verify=False)
    r = response.url
    if(r != url+'login'):
        print(f'{response.status_code} => {i.strip()}')

    #time.sleep(0.1)

extension.close()




