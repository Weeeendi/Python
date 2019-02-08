filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
#若要删除输出的空格用strip()

"""
读取文件时，python默认将所有的文件信息作为字符串处理，若想作为数字进行处理
可以用int() or float()进行转化
"""
filename1 = 'pi_million_digits.txt'

with open(filename1) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + "……")
print(len(pi_string))

birthday = input("Enter your birthday,in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday in the first million digits of pi!")
else:
    print("Your birthday don't in the first million digits of pi!")

message = "I really like dogs."
message1 = message.replace('dog', 'cat')
print(message1)