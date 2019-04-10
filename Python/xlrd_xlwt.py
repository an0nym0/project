import xlrd, xlwt

rb = xlrd.open_workbook('E_MSK_TEST.xls') #открываем файл
sheet = rb.sheet_by_index(0) #лист номер 0
value = 'CODE' #значение по которому будем искать
row_number = sheet.nrows
col_number = sheet.ncols

for rownum in range(1, row_number):
    CODE = sheet.cell(rownum,6)
#    sys_name = sheet.cell(rownum,8)
    print (CODE)