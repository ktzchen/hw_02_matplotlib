import csv
import matplotlib.pyplot as plt
import operator

open_days_file = open('open_business_days_undata_export_20201006_054612387.csv')
open_days_reader = csv.reader(open_days_file)
open_days_data = list(open_days_reader)

for i in range(1,7):
    open_days_data[i][2] = float(open_days_data[i][2])

sorted_list = sorted(open_days_data[1:7], key=operator.itemgetter(2))
#print(sorted_list)

x = [] #country
y = [] #days

for row in sorted_list:
    x.append(row[0])
    y.append(row[2])
    
print('x=', x, 'y=', y)

fig, ax = plt.subplots()
plt.bar(x,y)
ax.set(xlabel='Country')
ax.set(ylabel='# of Days')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()