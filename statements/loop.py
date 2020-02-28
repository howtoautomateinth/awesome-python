def forloop():
    # traditionally for-loop
    for x in range(0, 3):
        print('We\'re on time %d' % (x))

def whileloop():
    x = 0
    # base on condition while
    while (x<15):
        print('To infinity and beyond! We\'re getting close, on %d now!' % (x))
        x += 1

def forelse():
    # after conditon will execute else block 
    for x in range(3):
        print(x)
    else:
        print('Final x = %d' % (x))

def forwithiterable():
    collection = ['hey', 5, 'd']
    for x in collection:
        print(x)

if __name__ == '__main__':
    forloop()
    whileloop()
    forelse()
    forwithiterable()