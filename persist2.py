# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

# file = open('words.txt','w')

# for word in people:
#     file.write(word + '\n')
    
# file.close()

# 2. try-catch
# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
# file = None
# try:
#     file = open('words2.txt','w')
#     for word in people:
#         file.write(word + '\n')
# except: 
#     print('unable to write file woops')
# file.close()

#3.try catch people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
# file = None
# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
# try:
#     file = open('words3.txt','w')
#     for word in people:
#         file.write(word + '\n')
# except: 
#     print('unable to write file woops')
# finally:
#     file.close()

#4. file context manager
# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
# try:
#     with open('words4.txt','w') as word_files:
#         for word in people:
#             word_files.write(word + '\n')
# except: 
#     print('unable to write file woops')

#5. repeated names 
with open('repeated.txt','r') as rep_files:
    lines = rep_files.readlines()
    namecount = {}
    for word in lines:
        word = word.strip()
        if word in namecount:
            namecount[word] = 1
        else:
            for key, values in items
print(namecount)
# for line in lines:
#     #line = line.strip()
#     people_dict[line] = people_dict.get(line,0) +1

