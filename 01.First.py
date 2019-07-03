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


#
generator1 = iter([1,2,3,4])
print(next(generator1))


# Functional Programming




