def if_else_elif():
	x,y = 2,8
	if(x < y):
		st= 'x is less than y'
	
	elif (x == y):
		st= 'x is same as y'
	
	else:
		st='x is greater than y'
	print(st)

def switch(argument):
    #Python language doesn’t have a switch statement.
    #This is alternative way
    switcher = {
        0: ' This is Case Zero ',
        1: ' This is Case One ',
        2: ' This is Case Two ',
    }
    return switcher.get(argument, 'nothing')

if __name__ == '__main__':
    if_else_elif()
    print(switch(1))