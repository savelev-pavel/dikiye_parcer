# https://qna.habr.com/q/480867

import requests, gc
from bs4 import BeautifulSoup

headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36 OPR/56.0.3051.104'}

def getRunnersData(dikiye_url = 'https://app.dikiye.ru/statistics/',
                  number_of_lines=2000):
    global experts_quantity
    runners_quantity = number_of_lines
    response = requests.get(dikiye_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    del response
    gc.collect()
    soup = soup.find('table')

    rows = soup.find_all("tr")

    table_headers = []
    data = list()

    for row in rows:
        runner = list()
        cells = row.find_all("td")
        for i in range(len(cells)):
            runner.append(str(cells[i]).lstrip('<td>').rstrip('</td>'))
        data.append(runner)
    data.remove([])

    return data
if __name__ == '__main__':
    for i in range(len(getRunnersData())):
        print(getRunnersData())