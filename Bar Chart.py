import matplotlib.pyplot as plt

height = [10, 20, 30, 40, 50,60]
left = [1,2,3,4,5,6]

tick_label = ['2023', '2024', '2025', '2026', '2027', '2028']

plt.bar(left, height, tick_label = tick_label, width= 0.4, color = ['green', 'red'])

plt.xlabel('Years')
plt.ylabel('Progress')

plt.title('THE ONLY WAY IS UP')

plt.show()