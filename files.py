# How to append to a file?
def FileSave(filename,content):
    try:
        with open(filename, "a") as myfile:
            myfile.write(content)
    except IOError:
        print("An IO error occurred!")

FileSave("test.txt","test1 \n")
FileSave("test.txt","test2 \n")
    
# 'r+'  read + write text
# 'w+'  read + write text
# 'a+'  append + read text
# 'rb'  read binary
# 'wb'  write binary
# 'ab'  append binary
# 'rb+' read + write binary
# 'wb+' read + write binary
# 'ab+' append + read binary