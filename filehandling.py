import os
# modes : 1) Read 2) Write 3)append

file = open("data.txt","w")
file.write("\n this is new line")
file.close()
# if close function not implemented the file gets currupted

with open("data.txt", "a") as file:
    file.write("mknkjnkjn")
    file.write("gjvbjgvhjb")

#if file not there in read mode it throws error 
#file creates new file if not exit in write mode

f = open("poem.txt","w")
f.write("\n this is my poem")
f.close()


if os.path.exists("file123.txt"):
    os.remove("file123.txt")
    print("file deleted")
else:
    print("file does not exit")


with open("poem.txt","r") as f:
    content = f.read()
    words = content.split()
    print("total words", len(words))


with open("poem.txt","a") as f:
    f.write("\n hello world")
    


