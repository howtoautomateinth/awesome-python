# Counter
# count on collection
from collections import Counter
l = [1,1,1,2,3,4,5,6,2,3,4,6,7,5]
print(Counter(l))
s = 'asdsadasdadwqeqwcdzddqaewqe'
print(Counter(s))
sq = 'How many times does each word show up in this sentence word word word'
print(Counter(sq.split()))
print(Counter(sq.split()).most_common())

print('\n')
# Default Dict
# default value for dictionary
from collections import defaultdict
d = {'k1':'v1','k2':'v2'}
print(d['k2'])
# will errror if no key
# print(d['k3'])

dd = defaultdict(lambda: 0)
dd['one1']
for item in dd:
    print(dd)

print('\n')
# OrderedDict
# dictionary with order
# interesting information on python 3.6+ = https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6
# you should stick with OrderedDict if want orderd collection
from collections import OrderedDict
dic = {}
dic['a'] = 1
dic['c'] = 3
dic['b'] = 2
dic['d'] = 4
dic['e'] = 5
print('Regular dict')

for k,v in dic.items():
    print(k,v)

print('\n')
od = OrderedDict()
od['a'] = 1
od['c'] = 3
od['b'] = 2
od['d'] = 4
od['e'] = 5

print('Order dict')
for k,v in od.items():
    print(k,v)

print('Insertion Order dict')
od['f'] = 6
for k,v in od.items():
    print(k,v)

print('\n')
# namedtuple
# new object type allow name field
from collections import namedtuple

t = (1,2,3)
print('Regular Tuple')
print(t[0])

print('Named Tuple')
Dog = namedtuple('Dog','age breed name')

sam = Dog(age=2,breed='Lab',name='Sammy')
print(sam.age)
print(sam.breed)
print(sam.name)