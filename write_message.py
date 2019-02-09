filename = 'programming.txt'

with open(filename, 'w') as object_file:
    object_file.write("I love programing.\n")
    object_file.write("I love creating new games.\n")

#使用a以附加模式打开文件
with open(filename, 'a') as object_file:
    object_file.write("I also love finding meaning in large datasets.\n")
    object_file.write("I love creating apps that can run in a browser.\n")        
