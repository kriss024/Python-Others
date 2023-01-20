name = 'Pete'
sentence = 'Hello %s' % name
print(sentence)

num = 5
sentence = 'I have %x apples' % num
print(sentence)

person = {'name': 'Jenn', 'age': 23}
sentence = f'My name is {name} and I am {age} years old.'.format(name = person['name'], age = person['age'])
print(sentence)

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__ (self):
        return f'My name is {self.name} and I am {self.age} years old.'

p1 = Person('Jack', '33')

sentence = f'My name is {p1.name} and I am {p1.age} years old.'.format(p1)
print(sentence)
print(p1)

name = p1.name
sentence = f'Hello, {name}!'
print(sentence)

a = 10000000
sentence = f"{a:,}"
print(sentence)
# '10,000,000'

pi = 3.14159265
sentence = f'Pi is equal to {pi:.2f}'
print(sentence)
# '3.14'

b = 0.816562
sentence = f"{b:.2%}"
print(sentence)
# '81.66%'

numbers = [23.23, 0.123334987, 1, 4.223, 9887.2]

for number in numbers:
    print(f'{number:9.4f}')

for number in numbers:
    print(f'{number:09.4f}')

sentence = f'1 MB is equal to {} bytes'.format(10**6)
print(sentence)


import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

# March 01, 2016

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{:%B %d, %Y} fell on a {} and was the {} day of the year'.format(my_date)
print(sentence)