import pandas as pd
import phonenumbers

#def main():
#    url = 'https://phonenum.info/en/phone/'
#    r = mechanize.Browser()
 #   i = 0
file = 'E_MSK_TEST.xls'
#    writer = pd.ExcelWriter('E_MSK_RESULT.xls', engine='xlsxwriter')
xl = pd.ExcelFile(file)

#    print(xl.sheet_names)

df1 = xl.parse('SQL Results')

for line in df1:
    code = df1.loc[:, 'CODE'].tolist()
#    x = phonenumbers.parse(code, None)
#    print(x)
    print('\n'.join(code))

#print(df1)


#    for l in code.readlines():
#        i = i+1
#        string = l.split(";")
#        r.open(url + l)
#        print(";".join(l)+"\n")



#if __name__ == "__main__":
#    main()

#r = mechanize.Browser()
#r.open(url + code)
#print(r.title())