import pandas as pd
import csv

# 读取第一个文件
file1 = pd.read_csv('bay_vio_data_03_19.csv')

# 提取所有出现过的 street_marker 和 aim_marker
markers = set(file1['street_marker']).union(set(file1['aim_marker']))

# 打开第二个文件进行逐行读取
with open('dis_CBD_twoPs_03_19.csv', 'r') as infile, open('dis_CBD_twoPs_03_19.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        try:
          start, end = row['twoPs'].split('_')
        except ValueError:
          continue
        if start in markers and end in markers:
            print(start,end,"\n")
            writer.writerow(row)

print("Filtered data has been written to 'dis_CBD_twoPs_03_19.csv'")
