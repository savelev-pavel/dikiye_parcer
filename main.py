import xlsxwriter
from datetime import date
from getRunnersData import table_headers, getRunnersData

def xls_table(pacer_table):
    today = str(date.today)
    book = xlsxwriter.Workbook('Награждения ред.' + today + '.xlsx')
    page = book.add_worksheet('Награждения')

    page.set_column('A:A', 10)
    page.set_column('B:B', 40)
    page.set_column('C:C', 10)

    page.write(0,0,'№')
    page.write(0,1,'ФИО')
    page.write(0,2,'Кол-во пейсов')
    row = 1
    column = 0
    for i,_ in enumerate(pacer_table):
        no, name, paces = pacer_table[i][0], pacer_table[i][1], pacer_table[i][2]
        page.write(row, column, no)
        page.write(row, column + 1, name)
        page.write(row, column + 2, paces)
        row += 1
    book.close

table = list(getRunnersData())
table_filtered = []
runner = []
margins = ['8','9','28','29','58','59','98','99']
for j, _ in enumerate(table):
    if table[j]['Пейсмейкер или замыкающий'] in margins:
        runner = [table[j]['№'], table[j]['Трейлраннер'], table[j]['Пейсмейкер или замыкающий']]
        table_filtered.append(runner)
        xls_table(table_filtered)
