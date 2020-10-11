import csv
import matplotlib.pyplot as plt
import numpy as np
import operator

ppp_file = open('singuspppdata.csv')
ppp_reader = csv.reader(ppp_file)
ppp_data = list(ppp_reader)

for i in range(1, len(ppp_data)-1):
    ppp_data[i][1] = float(ppp_data[i][1])
    ppp_data[i][2] = float(ppp_data[i][2])

sorted_list = sorted(ppp_data[1:len(ppp_data)-1], key=operator.itemgetter(1))

x1 = [] #year
y1 = [] #ppp
x2 = []
y2 = []

for row in sorted_list:
    if row[0] == 'Singapore':
        x1.append(row[1])
        y1.append(row[2])
    else:
        x2.append(row[1])
        y2.append(row[2])

print("x1=", x1, "y1=", y1)
print("x2=", x2, "y2=", y2)

fig, ax = plt.subplots()
plt.plot(x1, y1, label='Singapore')
plt.plot(x1, y2, label = 'US')
ax.set(xlabel='Year')
ax.set(ylabel='GDP per capita, PPP')
plt.tight_layout()
plt.xticks(rotation=90)
plt.ylim(10000,110000)
plt.legend()
plt.show()