import csv

#create csv file
#with open("outputNew.csv", "w") as csv_file_wr:
#    writer = csv.writer(csv_file_wr, delimiter=',')
#    writer.writerow (["CODE","CNT","PRICE","CURRENCY"])

with open("gamma.csv", mode='r', encoding='utf-8') as csv_file_1:
#    df1 = csv.DictReader(csv_file_1, delimiter=',')
    df1 = csv.reader(csv_file_1, delimiter=',')

#with open("e_omsk_comma.csv", mode='r', encoding='utf-8') as csv_file_2:
#    df2 = csv.DictReader(csv_file_2, delimiter=',')

    for line in df1:
#        print(line)
#        code = line["CODE"]
#        price = line["PRICE"]
#        currency = line["CURRENCY"]
        print(code)

#        for line in df1:
#            code1 = line["CODE"]
#            cnt = line["CNT"]
#            print (cnt)
#            if code == code1:
#                print(code, cnt, price, currency)
#                with open("outputNew.csv", "a") as csv_file_wr_sec:
#                    writer = csv.writer(csv_file_wr_sec, delimiter=',')
#                    writer.writerow ([code,cnt,price,currency])
#            else:
#                print(code, None, price, currency)
#                with open("outputNew.csv", "a") as csv_file_wr_sec:
#                    writer = csv.writer(csv_file_wr_sec, delimiter=',')
#                    writer.writerow ([code,None,price,currency])


