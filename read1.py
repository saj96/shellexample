file = open('names.txt', 'r')

list_names = []
converted_list = []
for content in file.readlines():
    list_names.append(content)
for element in list_names:
    converted_list.append(element.strip())
print(converted_list)
file.close()
