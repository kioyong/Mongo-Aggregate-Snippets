# import sublime
# import sublime_plugin
import random
from os import urandom as _urandom
# print("hello Python!")
# t1 = "hello my name is liangyong"
# t2 = t1[1:5]
# t3 = t1[16:]
# print ("t2 = ",t2)
# print("t3 = ",t3)
# t4 = "my name is liangyong,my age \
# is 20,i like cat and i like \
# play a LOL!"
# print(t4)
# print("let me try to print \\~ hei!")


# # print("print \a  \n   \v   \t  \r   ")
# print("print ","hello~"*2)

# t5 = "abcdefg"
# t6 = "ac"
# print(t6 in t5)
# t7 = "abcde\"   "

# print(t7)
# # print(R'dsff \'')
# print(min(t7))
# print(max(t7))
# print(t7.rstrip())#删除字符串后面的空格

# a,b = 0,1
# while b<1000:
#     print(a,b,sep='@')
#     a,b = b,a+b


# a = 10
# if a<6:
#     print("a<6")
# else:
#     print("a>6")

# if 0:
#     print("0")
# if 1:
#     print("1")
# if -5:
#     print("-5")


# num=int(input("输入一个数字："))
# if num%2==0:
#     if num%3==0:
#         print ("你输入的数字可以整除 2 和 3")
#     else:
#         prins
#     if num%3==0:
#         print ("你输入的数字可以整除 3，但不能整除 2")
#     else:
#         print  ("你输入的数字不能整除 2 和 3")

# i = 1
# sum = 0
# while i<=100:
#     i,sum = i+1,sum+i
# print("sum =  ",sum)
# print("sum = ",sum(range(100)))
# sum(range(101))
# # list = [1,2,3,4,5,6,7,8,9,10]
# list = range(10)
# for a in list:
#     print("b = ",a)

# list1 = ['baidu','google','runoob','taobao']
# for i in range(len(list1)):
#     print(i,list1[i],sep="")

# list2 = 'hello my name is liangyong'
# for i in list2:
#     if(i=='n'):
#         break
#     print(i)
# max =5
# for i in range(max):
#     i=i+1
#     for j in range(max):
#         j=j+1
#         print(i,"*",j,"=",i*j)
#         if i<j+1:
#             i=i+1
#             break
#         j=j+1
# import sys

# list = range(5)
# a = iter(list)

# while True:
#     try:
#         print(next(a))
#     except StopIteration:
#         # print("End")
#         # sys.exit()
#         break
# print('End')

# def fibonacci(n):
#     i,j = 0,1
#     for a in range(n):
#         yield i
#         i,j=j,j+i

# def listfibonacci(max):
#     n, a, b = 0, 0, 1
#     L = []
#     while n < max:
#         L.append(b)
#         a,b =b,a+b
#         n = n+1
#     return L
# list = listfibonacci(10)
# for i in list:
#     print("ii = ",i)


# list = fibonacci(10)
# for i in range(11):
#     print(next(list))

# list = range(10)
# it = iter(list)
# for i in range(10):
#     print(next(it))
# for i in list:
#     print("i=",i)
# for i in fibonacci(10):
#     print("i = ",i)

# a = "AAA"
# print(a)
# def changedstring(a):
#     a = "String param can not be changed in function"
#     print(a)

# changedstring(a)
# print(a)

# list =[1,2,3,4,5]
# print(list)
# def changedlist(a):
#     a[0] = 'list param can be changed in function'
#     print(a)
# changedlist(list)
# print(list)

# def printinfo(name,age=10):
#     print("name",name)
#     print("age",age)
# printinfo("names")

# 2017年9月10日 14:06:00   每天100行代码挑战

# 不定长函数
# def printinfo(*vartuple):
#     print("info:")
#     # print(arg1`)
#     for var in vartuple:
#         print(var)
#     return;

# printinfo()

# 匿名函数

# sum = lambda arg1,arg2:arg1 + arg2
# print(sum(10,20))

# def sum(v1,v2):
#     total =v1+v2
#     print(total)
#     return total
# result = sum(10,20)
# print("my result = ",result)

# def sum(*arg):
#     total = 0
#     for var in arg:
#         total =total +var
#     return total
# result = sum(10,20,30,40,50)
# print("my sum result = ",result)

# text = "default text";
# def printinfo(arg):
#     text = "my info is "+arg
#     return text
# printinfo("a0")
# print("text = ",text)

# total = 0;
# def sum(*arg):
#     for var in arg:
#         global total
#         total = total +var
#     return total
# sum(10,20,30)
# print("total = ",total)

# if/lif.else/try/except/for/while  不会引用新的作用域
# text = "default text"
# if True:
#     text = "changed text"
# print(text)

# result = 0
# def sum(v1,v2):
#     result = v1 + v2
#     def inner(v1,v2):
#         # global result
#         # nonlocal result
#         result = v1 * v2
#     inner(v1,v2)
#     return result
# result2 = sum(10,20)
# print("local result = ",result2)
# print("global result = ",result)
def printinfo(list):
    print("list = ", list)

# list = [1,2,3,4,5]
# list2 = [2,5,8]
# list.append(6)
# list.extend(list2)
# list.insert(4,7)
# list.remove(2)
# list2.clear()
# print("list 2 = ",list2)
# print("index = ",list.index(1))
# print("count(5) = ",list.count(5))
# list.sort()
# list.reverse()
# list3 = list.copy()
# list3.remove(2)
# printinfo(list)
# print(list3)

# 3*4 转换成 4*3
# matrix = [
#     [1,2,3,4,6,8],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# def maplist(arg,matrix):
#     list = []
#     result = []
#     for var in matrix:
#         for i in var:
#             global list
#             list.append(i)
#     i = 0
#     j = 0
#     list1 = []
#     for var in list:
#         if i<arg :
#             list1.append(var)
#             i = i+1
#             j = j+1
#             if j == len(list):
#                 result.append(list1)
#         else:
#             actualList = list1.copy()
#             result.append(actualList)
#             list1.clear()
#             list1.append(var)
#             i = 1
#             j = j+1
#     print("result = ",result)
# maplist(3,matrix)
# total = [[row[i] for row in matrix] for i in range(4)]
# print("total = ",total)
# test = [i for i in range(4)]
# test1 = [i for i in range(4)]
# printinfo(test)
# printinfo(test1)

# matrix = [
#     [1,2,3,4,6,8],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# def maplist(arg,matrix):
#     i = 0
#     list = []
#     result =[]
#     for sublist in matrix:
#         for n in sublist:
#             list.append(n)
#             i = i + 1
#             if i%arg==0:
#                 result.append(list.copy())
#                 list.clear()
#         if sublist == matrix[len(matrix)-1]:
#             result.append(list)
#     return result
# result = maplist(5,matrix)
# print("result = ",result)
#
# import test
# import sublime

# test.printinfo()

# import sys
# print("sys.path = ",sys.path)

# s ='hello runoob\n'
# print(s)
# str(s)
# t = repr(s)
# print(t)
# print("kkk")

# f =open("C:/Users/LiangYong/Sublime Text 3/data/Packages/User/Hello.py","r")
# str = f.readline()
# str = f.readline()
# print(str)
# for line in f:
    # print(f.readline())
    # print(line)


# f =open("C:/Users/LiangYong/Sublime Text 3/data/Packages/User/xx.txt","w")
# s = 'sdfdsfd'
# f.write(s)

# f.close()


# from urllib import request
# response = request.urlopen("http://www.baidu.com/")
# str1 =response.read()
# fi = open("C:/Users/LiangYong/Sublime Text 3/data/Packages/User/xx.txt","w")
# fi.write(str(str1))
# # fi.close()


#

# response = request.urlopen("http://www.baidu.com/")
# str1 =response.read()
# fi = open("C:/Users/LiangYong/Sublime Text 3/data/Packages/User/xx.txt","w")
# fi.write(str(str1))
# # fi.close()

# random training
print("hello random")
# for i in range(10):
    ##生成范围内的随机浮点数
    # print("test random = ",random.uniform(10,20))
    # print("test random = ",random.randint(1,1000))
    # self.random()
BPF = 53        # Number of bits in a float
RECIP_BPF = 2**-53
# print("RECIP_BPF = ",RECIP_BPF)
aa = (int.from_bytes(_urandom(7), 'big') >> 3) * RECIP_BPF
# print("aa= ",aa)
# print("_urandom(7) = ",_urandom(7))
def uniform(a, b):
    "Get a random number in the range [a, b) or [a, b] depending on rounding."
    return a + (b-a) * aa
test = uniform(10,20)
print("test = ",test)


