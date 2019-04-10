import csv
import phonenumbers

#create csv file
with open("outputPN.csv", "w") as csv_file_wr:
    writer = csv.writer(csv_file_wr, delimiter=',')
    writer.writerow(["CODE","COUNTRY","ZONE","PRICE","CURRENCY"])

with open("Equant_MSK.csv", mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for line in csv_reader:
        code = str(line["CODE"])  # type: str
        x = phonenumbers.parse(code, None)
        print(x)

        with open("outputPN.csv", "a") as csv_file_wr_sec:
            writer = csv.writer(csv_file_wr_sec, delimiter=',')
            writer.writerow([code, x])