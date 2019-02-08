#with 关键字可以在不许要使用文件时关闭文件，相对于close更为智能
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
#相对地址打开
with open("text_files\pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents)
#逐行打开
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
"""
为何在输出出现这些换行符，这是因为在文件每行末尾有一个看不见的换行符，
print函数也自带一个换行符所以加入了多行空格，如果想去除空格可以使用rstrip()
"""
with open(filename) as file_object:
    for line in file_object:
        print(line.strip()) 