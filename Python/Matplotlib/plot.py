from matplotlib import pyplot as plt
# from matplotlib import style

x = [1,3,5,7]
y = [7,3,8,3]

x2 = [2,4,6,8]
y2 = [6,7,2,6]

plt.bar(x,y,color = 'c')

plt.bar(x2,y2,color = 'g')

plt.title('Coder Profile')
plt.ylabel('Percentile')
plt.xlabel ('Languages')
# plt.legend()

plt.show()
