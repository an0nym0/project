import csv
import phonenumbers
'''
def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj, delimiter=',')
    for row in reader:
        print(";".join(row))

if __name__ == "__main__":
    csv_path = "Equant_MSK.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)
'''

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["CODE"])
        #code = line["CODE"]
        #x = phonenumbers.parse(code, None)
#        print(line["SERVICE_NAME"]),
#        print(line["PRICE"]),
#        print(line["CURRENCY"])
        #print(x)

if __name__ == "__main__":
    with open("Equant_MSK.csv") as f_obj:
        csv_dict_reader(f_obj)