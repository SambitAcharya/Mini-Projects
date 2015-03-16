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
'''

'''
Reading from a file



readFile = open('sampledata.txt','r')
sepFile = readFile.read().split('\n')

readFile.close()

fig = plt.figure()
rect = fig.patch
rect.set_facecolor('#314213')

x = []
y = []

for plotPair in sepFile:
    XandY = plotFair.split(',')
    x.append(intXandY[0])
    y.append(intXandY[1])


plt.plot(x,y)

ax1 = fig.add_subplot(1,1,1, axisbg = 'grey')
ax1.plot(x,y,'c', linewidth = 3.3)

ax1.tick_params(axis  = 'x', colors = 'c')
ax1.tick_params(axis  = 'y', colors = 'c')

ax1.spines['bottom'].set_color('w')
ax1.spines['top'].set_color('w')
ax1.spines['left'].set_color('w')
ax1.spines['right'].set_color('w')

ax1.yaxis.label.set_color('c')
ax1.xaxis.label.set_color('c')

ax1.set_title('matplotlib title')
ax1.set_title('xlabel')
ax1.set_title('ylabel')

plt.show()



readFile2 = open('sampledata2.txt','r')
sepFile2 = readFile2.read().split('\n')

readFile2.close()

fig = plt.figure()
rect = fig.patch
rect.set_facecolor('#314213')

x2 = []
y2 = []

for plotPair in sepFile2:
    XandY = plotFair.split(',')
    x2.append(intXandY[0])
    y2.append(intXandY[1])


plt.plot(x,y)

ax2 = fig.add_subplot(2,1,2, axisbg = 'grey')
ax2.plot(x,y,'c', linewidth = 3.3)

ax2.tick_params(axis  = 'x', colors = 'c')
ax2.tick_params(axis  = 'y', colors = 'c')

ax2.spines['bottom'].set_color('w')
ax2.spines['top'].set_color('w')
ax2.spines['left'].set_color('w')
ax2.spines['right'].set_color('w')

ax2.yaxis.label.set_color('c')
ax2.xaxis.label.set_color('c')

ax2.set_title('matplotlib title')
ax2.set_title('xlabel')
ax2.set_title('ylabel')

plt.show()

'''
