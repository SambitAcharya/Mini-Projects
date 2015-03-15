from matplotlib import pyplot as plt
# from matplotlib import style
import numpy as np


'''

Importing From CSV



x,y = np.loadtxt('examplefile.csv',unpack=True, delimiter = ',')

plt.bar(x,y, color = 'g', align = 'center')


plt.title('Coder Profile')
plt.ylabel('Percentile')
plt.xlabel ('Languages')


'''

'''
BAR Plots

# # x = [1,3,5,7]
# # y = [70,30,80,30]
# #
# # x2 = [2,4,6,8]
# # y2 = [60,70,20,60]
# #
# # plt.bar(x,y,color = 'g', align = 'center')
# #
# # plt.bar(x2,y2,color = 'c', align = 'center')
#
# # plt.xticks([1000, 2000, 3000, 4000,5000, 6000, 7000, 8000,])
# plt.title('Coder Profile')
# plt.ylabel('Percentile')
# plt.xlabel ('Languages')
# # plt.legend()

'''

'''
Subplots


'''

x = np.linspace(0,5,10)
y = x**2

plt.figure()
plt.plot(x,y,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title')

plt.subplot(1,2,1)
plt.plot(x,y,'r--')
plt.subplot(1,2,2)
plt.plot(y,x,'g*-')


plt.show()
