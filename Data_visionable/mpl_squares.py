import matplotlib.pyplot as plt
input_values=[1,2,3,4,5]
squares = [1, 2, 6, 15, 19]
plt.plot(input_values,squares, linewidth=3)

#set up title of figure,and label the coordinate axis
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value", fontsize=14)

#设置标记刻度的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()