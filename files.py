def Zad2():
     import string
     import os

     i=input()
     f= open("files.txt","w")
     f.write(i)
     f.close
     with open("files.txt", "r") as f:
          m=f.read()
     print(m)
     os.remove("files.txt")