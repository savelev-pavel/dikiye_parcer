import requests, gc
from bs4 import BeautifulSoup

headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36 OPR/56.0.3051.104'}

def getRunnersData(dikiye_url = 'https://app.dikiye.ru/statistics/',
                  number_of_lines=2000):
    """Сбор информации о действующих экспертах"""
    global experts_quantity
    runners_quantity = number_of_lines
    response = requests.get(dikiye_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    del response
    gc.collect()
    soup = soup.find('table')

    t_headers = {'Трейлраннер', 'Количество трейлов', 'Количество уникальных локаций', 'Общая дистанция',
                 'Пейсмейкер или замыкающий', 'Бежал с собакой', 'Привел друга на трейл',
                 'Присматривал за детьми на трейле'}
    rows = soup.find_all("tr")

    data = []

    for row in rows:
        cells = row.find_all("td")
        print(cells)
    # item = {}
    #
    # for index in t_headers:
    #     item[headers[index]] = cells[index].text
    #     data.append(item)

    # search_lines = ['tr-'+str(i) for i in range(1, number_of_lines + 1)]
    # line1 = soup.find('tbody')
    # del soup
    # gc.collect()
    #
    # for _ in search_lines:
    #     line2 = line1.find(class_=_)
    #     if line2 == None:
    #         experts_quantity = search_lines.index(_)
    #         break
    #     name = line2.find(class_='td-0').text
    #     date_since = line2.find(class_='td-1').text
    #     date_until = line2.find(class_='td-2').text
    #     sphere = line2.find(class_='td-3').text
    #     okpd_codes = line2.find(class_='td-4').text
    #     department = line2.find(class_='td-5').text
    #     extra = line2.find(class_='td-6').text
    #     yield name,date_since, date_until, sphere, okpd_codes, department, extra
    #
    # del line2, search_lines, name, date_since, date_until, sphere, okpd_codes, department, extra
    # gc.collect()
    return data
if __name__ == '__main__':
    print(getRunnersData())