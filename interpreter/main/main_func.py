def print_sth():
    print('something')

print('Top level')

if __name__ == '__main__':
    # if we run directly python will set buit in variable __name__ to __main__
    # because python language no main function
    print('run directly')
else:
    print('has been imported!')