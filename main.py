from getRunnersData import table_headers, getRunnersData

table = list(getRunnersData())
table_filtered = []
margins = ['8','9','28','29','58','59','98','99']
for j, _ in enumerate(table):
    if table[j]['Пейсмейкер или замыкающий'] in margins:
        table_filtered.append(table[j])

for j, _ in enumerate(table_filtered):
    for i in table_headers:
        print(table_filtered[j][i], end=' ')
    print()
