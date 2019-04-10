import xlrd, xlwt, mechanize

#ПЕРЕМЕННЫЕ

#открываем файл
rb = xlrd.open_workbook('E_MSK_TEST.xls',formatting_info=True)
#выбираем активный лист
sheet = rb.sheet_by_index(0)
#получаем значение первой ячейки A1
val = sheet.row_values(0)[0]
#получаем список значений из всех записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#создаем новый файл
wb = xlwt.Workbook()
#создаем новую книгу
ws = wb.add_sheet('Test')
#страница запроса региона по тел коду
url = 'https://phonenum.info/en/phone/'
#запрос информации
res = mechanize.Browser()
res.open(url)
