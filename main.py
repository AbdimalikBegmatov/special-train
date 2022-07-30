# my_file = open("test.txt", 'r')
# print(my_file)
# my_file.close()

# try:
#     some_file=open("test.txt",'a')
#     try:
#         some_file.write("Hello Uuljan ")
#     except Exception as e:
#         print(e)
#     finally:
#         some_file.close()
#         print("Finally")
# except Exception as ex:
#     print(ex)

# with open("test.txt", 'a') as somefile:
#     # somefile.write("Hello world")
#     print("Hello World",file=somefile)

# with open("test.txt", 'r') as file:
    # for line in file:
    #     print(line, end="\t")

    # str1=file.readline()
    # print(str1,end='\t')
    # str2 = file.readline()
    # print(str2, end='\t')

    # line=file.readline()
    # while line:
    #     print(line, end="")
    #     line = file.readline()

    # content = file.read()
    # print(content)

    # content = file.readlines()
    # print(content[1])
    # print(content[3])
    # print(content[0])

# with open("test.txt",'r',encoding="UTF=8") as file:
#     text=file.read()
#     print(text)

# FILENAME = 'msg.txt'
# msgs = []
# for i in range(4):
#     msg = input(f"Ведите строку {i}: ")
#     msgs.append(msg+"\n")
#
# with open(FILENAME,'a') as file:
#     for msg in msgs:
#         file.write(msg)
#
# with open(FILENAME) as file:
#     for msg in file:
#         print(msg, end="")

import csv

FILENAME = "users.csv"
users = [
    ['Tom', 28],
    ['Alice', 23],
    ['Bob', 34]
]

with open(FILENAME,'w',newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, 'a', newline="") as file:
    user=["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)

with open(FILENAME,'r',newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]} - {row[1]}")
