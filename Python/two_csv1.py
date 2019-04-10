import csv

#create csv file
with open("outputSuc.csv", "w") as csv_file_wr1:
    writer = csv.writer(csv_file_wr1, delimiter=',')
    writer.writerow(["CODE","CNT","PRICE","CURRENCY"])

with open("outputUnSuc.csv", "w") as csv_file_wr2:
    writer = csv.writer(csv_file_wr2, delimiter=',')
    writer.writerow(["CODE","CNT","PRICE","CURRENCY"])

#f1 = open('file1.csv', 'r')
#f1_reader = csv.reader(f1, delimiter=';')

with open("e_omsk_comma.csv", mode='r', encoding='utf-8') as f1:
#    f1_reader = csv.DictReader(f1, delimiter=',')
    f1_reader = csv.reader(f1, delimiter=',')

    for row in f1_reader:
        with open('gamma.csv', 'r') as f2:
#            f2_reader = csv.DictReader(f2, delimiter=',')
            f2_reader = csv.reader(f2, delimiter=',')
            for line in f2_reader:
                try:
                    if str(row[0]) == str(line[0]):
#                        code = row["CODE"]
#                        cnt = line["CNT"]
#                        price = row["PRICE"]
#                        currency = row["CURRENCY"]
                        print('Success', str(row[0]), str(line[1]), str(row[1]), str(row[2]))
                        with open("outputSuc.csv", "a") as csv_file_wr_sec:
                            writer = csv.writer(csv_file_wr_sec, delimiter=',')
                            writer.writerow ([str(row[0]), str(line[1]), str(row[1]), str(row[2])])
#                    elif str(row[0]) !== str(line[0]):
#                        print('UnSuccess', str(row[0]), str(line[1]), str(row[1]))
                except IndexError:
                    continue