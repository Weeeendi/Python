import json

def write_number():
    user_number = input("Please input your favourite number: ")
    filename = 'usernum.json'
    with open(filename,'w') as f_obj:
        json.dump(user_number, f_obj)
    return user_number
    

def read_number():
    filename='usernum.json'
    try:
        with open(filename) as f_obj:
            faver_num = json.load(f_obj)
    except FileNotFoundError:
        print("You have never created any records.")
    else:    
        return faver_num
        
def comfirm():
    faver_num = read_number()
    if not faver_num:
        faver_num = write_number()
    
    comfirm_number = input("Is " + faver_num + " your favourite number?(Y/N)")  
    if comfirm_number=='Y':
        print("I know your favourite number is " + faver_num + '.')
        return False
    else:
        write_number()

while True:
    flag = comfirm()
    if flag == False:
        break
    