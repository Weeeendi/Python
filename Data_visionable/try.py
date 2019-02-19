import matplotlib.pyplot as plt
x_1 = list(range(1, 5001))
y_1 = [x**3 for x in x_1]
plt.scatter(x_1,y_1,c=y_1,cmap=plt.cm.Reds,edgecolors='none',s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("number of square", fontsize=14)
plt.ylabel("square",fontsize=14)
plt.show()