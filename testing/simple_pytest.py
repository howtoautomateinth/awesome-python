# prefix our test function names with test_
def sum_nums(x,y):
    return x+y

def test_sum_nums():
    assert sum_nums(2,3) == 5

