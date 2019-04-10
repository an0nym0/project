import requests
#import urllib3
url = 'https://www.kodtelefona.ru/1207'
res = requests.get(url, verify=False)
print(res.text)

#print(res.content)


#res = urllib3.get_host(url)
#text = res.read()
#print (text)