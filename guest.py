user_name = input("Please enter your name,sir or miss(enter 'exit' to quit): ")
print("Hello " + user_name.title() + ", welcome to login in MySteam.")
filename = "guest.txt"
with open(filename, 'w') as file_object:
    file_object.write(user_name + '\n')

flag_sign = True
while flag_sign:
    user_name = input("Please enter your name,sir or miss(enter 'exit' to quit): ")
    if user_name == 'exit':
        flag_sign = False
        break
    print("Hello" + user_name.title() + ", welcome to login in MySteam.")
    with open(filename, 'a') as file_object:
        file_object.write(user_name + '\n')
