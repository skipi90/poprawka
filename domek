import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro:')
# plt.ylabel('liczby z wektora')
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r:')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
#
# plt.axis([0, 6, 0, 20]) # granice osi xmin, xmax, ymin, ymax
# plt.show()

# x = np.arange(0, 5.2, 0.2)
#
# plt.plot(x, x, 'r-', x, x**2, 'b^', x, x**3, 'gs')
# plt.legend(labels=['liniowa', 'kwadratowa', 'sześcienna'], loc='center left')
# plt.show()

# dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasillia', 'Warszawa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}
#
# df = pd.DataFrame(dane)
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosc = list(grupa.agg('Populacja').sum())
#
# plt.pie(x=grupa, labels=etykiety)
# plt.xlabel('Kontynenty')
# plt.ylabel('Populacja na kontynentach')
# plt.show()

# names = ['python','java','javascript','c#','php','c/c++','inne']
# percentages = [29.9, 19.1, 8.2, 7.3, 6.2, 5.9, 76.6]
#
# plt.pie(percentages, labels=names, explode=(0.1,0.1,0.1,0.1,0.1,0.1,0), autopct='%.1f%%', shadow=True)
# plt.title("Najpopularniejsze języki programowania")
# plt.legend(loc='upper left')
# plt.show()
#
# x = [1, 3, 5]
# y = [10, 3, 7]
#
# x2 = [1,6,7]
# y2 = [3,1,4]
#
# x3 = [3, 5 ,8]
# y3 = [1, 2, 3]
#
# plt.bar(x,y, label="Pierwszy",color="blue")
# plt.bar(x2,y2, label="Drugi", color="purple")
# plt.bar(x3, y3, label="Trzeci", color="orange")
# plt.legend()
# plt.show()

# xlsx = pd.read_excel('linieautobusowe10.xlsx')#skiprows = 6
# xlsxheaders = xlsx[['Nazwa','Rok','Wartosc','Jednostka miary','Atrybut']]
# # print(xlsx.head())
# print(xlsxheaders)
# plt.bar(xlsxheaders['Rok'],xlsxheaders['Wartosc'], label=xlsxheaders['Nazwa'])
# plt.legend()
# plt.show()

# import pandas as pd
# df = pd.read_csv('velocity_measurements.csv',header=None)
# print(df.head())
#
# t = df[0]
# v = df[1]
#

# from matplotlib import pyplot as plt
#
# fig, ax = plt.subplots(figsize=(10,7))
# ax.plot(t,v,lw=4)
# ax.set_xlabel('Time [s]',fontsize=14)
# ax.set_ylabel('Velocity [$m/s$]',fontsize=14)
# ax.set_title('Experiment 1',fontsize=14)
