def exception_example():
    try:
        raise Exception('Example raise exception')
    except Exception as error:
        print(error.args)
    else:
        print('No exception raise will print this.')
    finally:
        print('always run this code block.')

if __name__ == '__main__':
    exception_example()