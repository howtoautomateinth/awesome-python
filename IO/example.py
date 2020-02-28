
def main():
    # w = create a file if it does not exist in library
    # r = read
    # a = apeend
    # + = open a file for reading and writing, if not include this it will do only file mode we selected
    myfile = open('myfile.txt','w+')
    for i in range(10):
        myfile.write("This is line %d\r\n" % (i+1))
    myfile.close()

if __name__== "__main__":
  main()