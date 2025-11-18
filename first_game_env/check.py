print("we will do it insha allah")

f = open("asset/question_file.txt","r")
data = f.read().splitlines()
f.close()




question = print(data[2])
options = print(data[4],data[5],data[6],data[7])


# for line in data:
#     line = line.strip()
#     print(line)

#     if line.endswith("?"):
#         question = line
        
#     elif line.startswith(("A)","B)","C)","D)")):
#         options.append(line)

# print(question)
# print(options)