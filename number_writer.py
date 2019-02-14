import json

number = [2, 3, 4, 6, 8, 22, 13]

filenmae = 'number.json'
with open(filenmae, 'w') as f_obj:
    json.dump(number,f_obj)