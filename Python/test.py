'''Скрипт создает новый файл,
читает построчно приготовленный файл с кодами,
делает интернет запрос каждой строки,
из полученной информации парсит строку title и записывает в новый файл два столбца CODE COUNTRY'''

import mechanize
import csv

#create csv file
with open("outputNew.csv", "w") as csv_file_wr:
    writer = csv.writer(csv_file_wr, delimiter=',')
    writer.writerow (["CODE","COUNTRY","ZONE","PRICE","CURRENCY"])

with open("Equant_MSK.csv", mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for line in csv_reader:
        code = line["CODE"]
        zone = line["SERVICE_NAME"]
        price = line["PRICE"]
        currency = line["CURRENCY"]
        url = 'https://phonenum.info/en/phone/'
        r = mechanize.Browser()
        r.open(url + code)
        title = r.title()
  #     print(r.title())
        with open("outputNew.csv", "a") as csv_file_wr_sec:
            writer = csv.writer(csv_file_wr_sec, delimiter=',')
            writer.writerow ([code,title,zone,price,currency])