import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# 画散点，三种颜色模式
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=14)
# plt.scatter(x_values, y_values, c='blue', edgecolor='none', s=14)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=14)

plt.title(label=r'$y=x^2$', fontsize=24)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

# [xmin, xmax, ymin, ymax]
plt.axis([0, 1100, 0, 1100000])

# plt.show()

# 保存照片，并裁掉空白。
plt.savefig('squares_plot.png', bbox_inches='tight')
