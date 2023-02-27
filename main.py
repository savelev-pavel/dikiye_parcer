import xlsxwriter, requests
from datetime import date
from bs4 import BeautifulSoup

headers = {'Accept': '*/*', 'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/70.0.3538.67 Safari/537.36 OPR/56.0.3051.104'}

table_headers = ['№', 'Трейлраннер', 'Количество трейлов', 'Количество уникальных локаций',
                 'Общая дистанция','Был наставником', 'Пейсмейкер или замыкающий', 'Бежал с собакой',
                 'Привел друга на трейл', 'Присматривал за детьми на трейле', 'Баллы']
dikiye_url = 'https://app.dikiye.ru/statistics/'

def getRunnersData():
    response = requests.get(dikiye_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    del response
    soup = soup.find('table')
    rows = soup.find_all("tr")
    data = list()
    for row in rows:
        runner = dict()
        cells = row.find_all("td")
        for j in range(len(cells)):
            runner[table_headers[j]] = (str(cells[j]).lstrip('<td>').rstrip('</td>'))
        data.append(runner)
    data.remove({})
    return data

def xls_table(pacer_table):
    today = str(date.today())
    book = xlsxwriter.Workbook(f'Marshals {today}.xlsx')
    page = book.add_worksheet('Marshals')

    page.set_column('A:A', 4)
    page.set_column('B:B', 22)
    page.set_column('C:C', 5)

    page.write(0,0,'№')
    page.write(0,1,'ФИО')
    page.write(0,2,'Пейс')
    row = 1
    column = 0
    for i,_ in enumerate(pacer_table):
        no, name, paces = int(pacer_table[i][0]), pacer_table[i][1], int(pacer_table[i][2])
        page.write(row, column, no)
        page.write(row, column + 1, name)
        page.write(row, column + 2, paces)
        row += 1
    book.close()

try:
    table = list(getRunnersData())
    table_filtered = []
    runner = []
    margins = ['8', '9', '28', '29', '58', '59', '98', '99']
    for j, _ in enumerate(table):
        if table[j]['Пейсмейкер или замыкающий'] in margins:
            runner = [table[j]['№'], table[j]['Трейлраннер'], table[j]['Пейсмейкер или замыкающий']]
            table_filtered.append(runner)
    xls_table(table_filtered)
except Exception:
    input('Возникла ошибка, нажмите любую клавишу')
else:
    input('Успешно, нажмите любую клавишу')