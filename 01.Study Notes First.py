#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'01.Study Notes First.py'

__author__ = 'Kyle'

# 第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# 第2行注释表示.py文件本身使用标准UTF-8编码
# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
# 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

import functools
from functools import reduce
import sys
from types import MethodType

print("hello word!")
print('hello','word','!')
print(1+1)
print('1 + 1 =',1+1)
inputTxt  = input()
print(inputTxt)

if inputTxt == 'test': # 当语句以冒号:结尾时，缩进的语句视为代码块
    print("Y")
else:
    print("X")

strTxt = 'I\'m \"OK\"'
print(strTxt)

# 字符串默认不转义
print(r'\\\\\\\\')

# 多行
print('''line1
line2
line3''')

# 布尔值
print(True and False)
print(not False)

# 空值
print(True == None)


declare = True
declare = 'True'
print(type(declare))

print('中文')

# byte
byte = b'abc'
byteStr = 'abc'
byte = byteStr.encode('utf-8')
print(byte.decode('utf-8'))


len(byteStr)


print('hello %s'%'word!')
print('hello {0}'.format('word!'))


lists = ['0','1','2']
print(lists)
print(len(lists))
print(lists[0])

lists.append('3')
lists.insert(4, [0,1,2])
lists.pop(0) # 删除
print(lists[3][2])

if inputTxt == 'kyle':
    print('kyle')
elif inputTxt == 'kyle1':
    print('kyle1')
else:
    print('other')

if inputTxt:
    print('非零数值、非空字符串、非空list等')

print(type(int('1')))

names = ['kyle0','kyle1','kyle2']
for name in names:
    print('name:' + name)
    if(name == 'kyle1'):
        break
    if(name != 'kyle1'):
        continue;


dictionary = {'name':'kyle','age':25}
print(dictionary['name'])
print(18 in dictionary)  # exists
print(dictionary.get('name1'))  # return none
dictionary.pop('name') # remove
for value in dictionary.values():
    print(value)

# function
print(abs(1))
print(max(1,2,3))

# convertor
int('123')
float('1.23')
str(123)
bool(1)
print(isinstance(float('1.23'),(int,float)))

def my_method(para):
    return  para
print(my_method('kyle'))


def multipleResult():
    return 1,2
print(multipleResult())

def defaultPara(x1, x2 = 2):
    return  x2
print(defaultPara(1))

def variablePara(*numbers):
    return numbers[1]
print(variablePara(1,2,3))

def namePara(**dic):
    return  dic['name']
print(namePara(name='kyle'))

lists1 = ['0','1',2]
print(lists1[0:2])
print(lists1[0:3:2])
for index,item in enumerate(lists1):
    print(index)
    print(item)

# 列表生成式
print([m + n for m in 'ABC' for n in 'XYZ'])  # list
print((m + n for m in 'ABC' for n in 'XYZ'))  # generator


# generator
generator1 = iter([1,2,3,4])
print(next(generator1))


# Functional Programming
print(abs(-1))
def Fun(para):
    return para
funPara = Fun
print(funPara(1))

# 高阶函数
def higherOrderFunction(x, y, fun):
    return fun(x) + fun(y)
print(higherOrderFunction(1, 2, Fun))

def rideExtend():
    def ride(x):
        return x * x
    return ride
ridePara = rideExtend()
print(ridePara(1))

# map
def ride(x):
    return x * x;
mapList = map(ride, [1,2,3,4,5])
print(list(mapList))

# reduce 把结果继续和序列的下一个元素做累积计算，其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y
print(reduce(add, [1,2,3,4,5]))

# reduce参考：
# https://www.cnblogs.com/fuzhe1989/p/3413457.html
# https://storage.googleapis.com/pub-tools-public-publication-data/pdf/16cb30b4b92fd4989b8619a61752a2387c6dd474.pdf

# filter filter()函数用于过滤序列。filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def isOdd(x):
    return x % 2 == 1
print(list(filter(isOdd, [1,2,3,4,5])))

def notEmpty(x):
    return  x and x.strip()
print(list(filter(notEmpty, ['1','','2','3'])))

# sorted
print(sorted([1,2,3,5,4]))

# 匿名函数
print(list(map(lambda x: x * x, [1,2,3,4,5])))
AnonymousFunction = lambda x: x * x;
print(AnonymousFunction(2))

# Decorator
print(int('12345'))

# 偏函数
int2 = functools.partial(int, base = 2)
print(int2('1000000'))

# 使用模块
print(sys.argv)

# 作用域
# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
# 有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如__author__，__name__就是特殊变量
def _privateMethod():
    return "this is private method";
print(_privateMethod())

# Class
class Student(object):
    _last_name = "li"
    def __init__(self, n = 'default name'):  # 构造函数
        self.name = n
    def convert_name(self):
        return self.name + ' ' + self._last_name
student = Student();
print(student.name)
student = Student('kyle')
print(student.name)
print(student.convert_name())

class Animal(object):
    _name = ''
    def eat(self):
        print(self._name + ' is eating')
class Dog(Animal):
    _name = "dog"
dog = Dog()
dog.eat()

# type()
print(type(123))
print(isinstance(dog, Animal))

# __slots__：限制实例的属性
class Egg:
    pass
e = Egg()
e.name = "egg"
print(e.name)

# 给class实例绑定一个方法
def set_egg_name(self, name):
    self.name = name
e.set_egg_name = MethodType(set_egg_name, e)
e.set_egg_name('newegg')
print(e.name)

# 给class绑定一个方法
Egg.set_egg_name = set_egg_name
ne = Egg()
ne.set_egg_name('newnewegg')
print(ne.name)

# 限制实例的属性
class NewEgg(object):
    __slots__ = ('name')
newegg = NewEgg()
# newegg.otherAttr = '不可绑定其他属性'

# @property get set
class Geter(object):
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
get = Geter()
get.name = 'Kyle'
print(get.name)

# 多重继承
class RunnableMixIn(object):
    @property
    def run(self):
        return self._run
    @run.setter
    def run(self, value):
        self._run = value
class FlyableMixIn(object):
    @property
    def fly(self):
        return self._fly
    @fly.setter
    def fly(self, value):
        self._fly = value
class Bird(RunnableMixIn, FlyableMixIn):
    def __init__(self, name):
        self.fly = name + '_fly'
        self.run = name + '_run'
bird = Bird('kyle')
print(bird.fly)
print(bird.run)

# 