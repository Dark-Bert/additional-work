import math
import xlwt as xw
import numpy as np
import matplotlib.pyplot as plt

wb = xw.Workbook()
this_sheet = wb.add_sheet('EV Battery life span')


k = float(input('Enter the value of alpha: '))  # 6.32499
m = float(input('Enter the value of beta: '))   # 14.3826
life_span = int(input('Enter life span: '))     # 60


def weibull(t, a):
    if t > a:
        return k*math.pow(m, -k)*math.pow(t - a, k - 1)*math.exp(-1*math.pow((t - a)/m, k))

    else:
        return 0


arr_x = np.zeros(life_span, dtype=float)
arr_y = np.zeros(life_span, dtype=int)

this_sheet.write(0, 0, 'Life Span')
this_sheet.write(0, 1, 'Distribution')

for i in range(life_span):
    arr_x[i] = weibull(i + 1, 1)
    arr_y[i] = i + 1
    this_sheet.write(i+1, 0, float(arr_y[i]))
    this_sheet.write(i+1, 1, float(arr_x[i]))
    print(weibull(i + 1, 1))

wb.save('Weibull Distribution Function.xls')
plt.plot(arr_y, arr_x, label='EV lifecycle trend')
plt.show()
