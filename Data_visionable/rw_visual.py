import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    
    #标出终点和起点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    
    plt.show()

    keeprunning = input("Make anthor walk? (Y/N): ")
    if keeprunning.title() == 'N':
        break