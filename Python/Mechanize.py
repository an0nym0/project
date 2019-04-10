import mechanize

code = '1207'  # type: str
#url = 'https://phonenum.info/en/phone/'
url = 'https://www.kodtelefona.ru/'
r = mechanize.Browser()
r.open(url + code)
print(r.title())
