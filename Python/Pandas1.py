import pandas as pd, mechanize, re   #  pip install pandas
url = 'https://phonenum.info/en/phone/'


df = pd.read_excel(r'E_MSK_TEST.xls')

code = df.loc[:, 'CODE']#.tolist()

print(code)

print(df)





#r = mechanize.Browser()
#r.open(url + code)
#print(r.title())