import csv #top part was edited for dependency injection exercise

def csv_reader():
    with open('small.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        #next(reader) #skips the first header 
        dict_list = []
        for row in reader:
            dict_list.append(row)
        print(dict_list)
        return dict_list
    #printing
    # csv_reader = csv.reader(csv_file, delimiter=',')
    # for row in csv_reader:
    #         print(row)
import json 
def json_saver(data):
    with open('personal.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
def data_transformer(heading, value, readit, saveit):
    add_to_dict = readit()
    for index in add_to_dict:
        index[heading] = value
    saveit(add_to_dict)
    print(add_to_dict)
data_transformer('diabetic', True, csv_reader, json_saver)

#making a csv file with new data
# names = ['ollie', 'sarah', 'iman']
# pets =  ['cats', 'dogs', 'fish']

# with open('newdata.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(names)
#     writer.writerow(pets)

# places = ['london', 'leeds', 'bristol']
# with open('newdata.csv', 'a') as file:
#     writer = csv.writer(file)
#     writer.writerow(places)