import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 标题
plt.title(label=r'$y=x^2$', fontsize=24)

# x y 坐标轴名称
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

# 刻度的大小 x y both
plt.tick_params(axis='both', labelsize=14)

plt.show()
