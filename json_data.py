import json
#print json 
# with open('example.json', 'r') as f:
#     json_data = json.load(f)
#     print(json_data)

#print specific item of dictionary
# with open('example.json', 'r') as f:
#     json_data = json.load(f)
#     items_data = json_data["menu"]["items"]
    
#     for i in items_data:
#         print(i["id"])

#create json 
file_to_write = {'president': {'name': 'Zaphod Beeblebrox','species': 'Betelgeusian'    }}

with open('written_file.json','w') as f:
    json.dump(file_to_write, f, indent=4)
