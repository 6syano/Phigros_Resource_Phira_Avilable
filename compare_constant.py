import csv
file1 = input('Path of original infos.csv:')
file2 = input('Path of info_new.csv generated by Phigros_Resource:')
dic1 = {}
dic2 = {}
with open(file2, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            try:
                float(row[5])
            except:
                dic2[row[1]] = row[2:5]
            else:
                dic2[row[1]] = row[2:6]
with open(file1, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[1]:
            if row[0] in dic2:
                dic1[row[0]] = row[1:1 + len(dic2[row[0]])]
            else:
                pass
                #print(f'{row[0]} not found in info_new.csv')
diff = {}
for key in dic1:
    if key in dic2:
        for i in range(len(dic1[key])):
            if dic1[key][i] != dic2[key][i]:
                print(f'{key} {["EZ","HD","IN","AT"][i]}: {dic1[key][i]} -> {dic2[key][i]}')
                diff[key + str(i)] = dic2[key][i]
print('write into infos_new.csv')
with open('infos_new.csv', 'w', encoding='utf-8', newline='') as f:
    with open(file1, 'r', encoding='utf-8') as f1:
        reader = csv.reader(f1)
        writer = csv.writer(f)
        for row in reader:
            x = row
            if row[1]:
                for i in '0123':
                    if row[0] + i in diff:
                        x[1 + int(i)] = diff[row[0] + i]
            writer.writerow(x)