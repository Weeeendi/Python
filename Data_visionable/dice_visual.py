import pygal
from die import Die

#创建两个骰子
die_1 = Die()
die_2 = Die()

#掷几次色子,并将结果储存在一个列表中
results=[]
for roll_num in range(1000):
    result = die_1.roll()+die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_results=die_1.num_sides+die_2.num_sides
for value in range(2, max_results + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels=list(range(2,13))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)
hist.render_to_file('dice_visual.svg')