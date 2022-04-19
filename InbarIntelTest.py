import os
def sedFunc(fileOrStr,oldWord,newWord): 
        if os.path.isfile(fileOrStr): #checkink if the user insert a file
            with open(fileOrStr,'r') as file:
                fileInfo=file.read() #copying the file into a string
            fileInfo=fileInfo.replace(oldWord,newWord) #rearange the string
            with open(fileOrStr,'w') as file: 
                file.write(fileInfo) #writing the correct text back
        else: #if the user insert a string just replace 
            fileOrStr=fileOrStr.replace(oldWord,newWord)
        return fileOrStr
def main():
    str=input("please insert a file name or a string: ")
    old=input("please insert the text you want to be replace: ")
    new=input("please insert the text you want to replace with: ")
    if os.path.isfile(str):#check if it's a file to know how to print it
           with open(str,'r') as file:
                fileInfo=file.read()
                print("old one:\n"+ fileInfo)
                str=sedFunc(str,old,new)
                file.seek(0)
                fileInfo=file.read()
                print("new one:\n"+ fileInfo)
    else:
        print("old one:\n" + str)
        str=sedFunc(str,old,new)
        print("new one:\n"+str)

if __name__ == "__main__":
    main()

