#字符串
#下标
s='vbcsnbbkjvcsinkprwp23456'
'''print(s[1])  #从左到右从零开始数，第一个是b
print(s[-1])  #从右到左从‘-1’开始数，显示‘6’
print(s[-5])#从右到左从‘-1’开始数，显示‘2’
print(s[3:6]) #从左到右不包括后面的数6，依次显示snb
print(s[-8:-2])#从右到左从‘-1’开始数，依次显示‘rwp234’，不包含“-2”代表的数字
print(s[4:10:2])#依次显示下标为4、4+2、4+2+2（4+2+2+2=10，不包括10）的字符串为‘nbj’
print(s[-3:-10:-1])#y依次显示下标为-3、-3+(-1)、-3+(-1-1)……（的字符串为‘432pwrp’
print(len(s))    #字符串的长度‘24’
print(s.find('n'))#字符串里面包含n,显示的是第一个找到的下标4
print(s.find('n',8))#字符串里面包含n,显示的是从第8个下标对应的字符开始找，找到的下标13
print(s.find('hello'))#字符串里面不包含“hello”,显示的是“-1”'''
s1='    hdnoicv  '
print(s1.strip())
s2='192.168.0.1'
print(s2.split('.'))