from getRunnersData import table_headers, getRunnersData

table = list(getRunnersData())
for j in range(len(table)):
    for i in table_headers:
        print(table[j][i], end=' ')
    print()