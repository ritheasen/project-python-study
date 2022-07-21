import os


f = open("newfile.txt","r")

if os.path.exists():
    f = open("newfile.txt", "r")
    print(f.read())
else:
    f = open("newfile.txt","x")
    print("File create successfully")



