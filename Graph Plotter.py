import matplotlib.pyplot as plt

x1 = [2, 10, 6, 2]
y1 = [2, 2, 20, 2]
plt.plot(x1, y1, color = 'red', linestyle = 'dashed', linewidth = 3, marker = 'o', markerfacecolor = 'yellow', markersize = 12, label = 'Triangle')

plt.ylim(1,21)
plt.xlim(1,11)

x2 = [2, 10, 6, 2]
y2 = [20, 20, 2, 20]
plt.plot(x2, y2,color = 'black', linestyle = 'dashed', linewidth = 3, marker = 'o', markerfacecolor = 'red', markersize = 12, label = 'Opp. Triangle')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('TRI-SYMBOL')

plt.legend()

plt.show()