# x = input("请输入复数的实部和虚部：")
# a,b = map(float,x.split())
# m = complex(a,b)
# c = abs(m)
# print("输入的复数为："+str(m),",模为"+str(c))

# s=0
# n=0
# print("n"+"     "+"s")
# while s<=1000:
#     n+=1
#     s+=n*n
#     if s<=1000:
#         print(str(n)+"     "+str(s))


# import math
# def prime(n):
#     for i in range(2,int(math.sqrt(n))+1):
#         if(n%i==0):
#             return 0
#     else:
#         return 1
#
# num=int(input('请输入一个大于 2 的自然数：'))
# my_list=list(range(2,num))
# for i in my_list:
#     if(prime(i)==0):
#         my_list[i-2]=-1
# my_list=set(my_list)
# my_list=list(my_list)
# my_list.remove(-1)
# print(sorted(my_list))

# s = 0
# for i in range()


# # 输入两个集合
# setA = set(input('请输入集合A：'))
# setB = set(input('请输入集合B：'))
#
# # 并集
# s1 = setA | setB
# print(s1)
# # 交集
# s2 = setA & setB
# print(s2)
# # 差集
# s3 = setA - setB
# print(s3)


# import random
# x = [random.randint(0,100) for i in range(20)]
# #print(x) 打印x看看原列表
# y = x[::2]
# #print(y) 打印偶数坐标
# y.sort(reverse=True)
# x[::2] = y
# print(x)

# import string
# import random
# #利用string模块函数生成字符串abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# x=string.ascii_letters+string.digits+string.punctuation
# # print(x,len(x))
# #生成包含1000个随机字符的字符串
# # .join()连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
# y="".join([random.choice(x) for i in range(1000)])
# # y= ''.join(random.sample(x,94))  #sample从指定序列中随机获取指定长度的片段。sample函数不会修改原有的序列。
# print(y)
# d=dict() #使用字典保存每个字符出现次数
# for ch in y:
#     # d.get(ch,0) 返回ch出现的次数，若没有返回0
#     d[ch]= d.get(ch,0)+1
# print(d)

# import random
# m_str = "".join(random.choices("qwertyuioplkjhgfdsazxcvbnm", k=1000))
# print("字符串长度",len(m_str))
# # set集合去重
# m_set = set(m_str)
# x = (0,0,0,0)
# for i in m_set:
#     if(m_set[i]>= 'a'  && m_set[i] <= 'z'):
#         x[0]= x[0] + 1
#     else if(m_set[i] >= 'A' && m_set[i] <=)


# import math
#
# max = int(input('请输入一个大于二的自然数：'))
# lst = list(range(2, max))
# k = 0
# m = int(math.sqrt(max))
# for i in range(2, max):
#     flag = 1
#     for j in range(2, m):
#         if(bool(i % j)):
#             flag = 0
#     if(flag == 1):
#         lst[k] = i
#         ++k
# remover()
# print(lst)


# import math
# x=input("请输入复数的实部和虚部:")
# a,b=map(float,x.split())
# c=math.sqrt(a**2+b**2)
# print("输入的复数为:"+str(a)+"+"+str(b)+"j",",模为： "+str(c))

# import random
# import string
# x=string.ascii_letters+string.digits+string.punctuation
# print(x)
# y = [random.choice(x) for i in range(500)]
# z="".join(y)
# print('生成的 500 个随机字符： ', z)
# d=dict()
# for ch in z:
#     d[ch] = d.get(ch, 0) + 1
# #对于 ch 的每个值,将 ch 存到 key 处，数值 1 存到后面的对应位置
#     for k, v in d.items():
#         print(k, ':', v)#以列表返回可遍历的(键, 值) 元组数组
# print({k:v for k,v in sorted(d.items(),key=lambda item:item[1],reverse=True)}) #lambda 函数中项值为 0 的 key 参数表示要根据键对字典进行排序


# import random
# import string
# x=string.ascii_letters+string.digits+string.punctuation
# y = [random.choice(x) for i in range(1000)]
# z="".join(y)
# print('生成的 1000 个随机字符： ', z)
# sta=[0,0,0,0]
# for ch in z:
#     if ch.isupper():
#         sta[2]+=1
#     elif ch.islower():
#         sta[3]+=1
#     elif ch.isdigit():
#         sta[1]+=1
#     else:
#         sta[0]+=1
# print(tuple(sta))

# def fac(num):
#     for i in range(2,num):
#         if num%i==0:
#             print(i)
# n=int(input("请输入一个数： "))
# fac(n)

# def division_algorithm(a,b):#辗转相除法
#     mul=a*b
#     if a>b:
#         remainder=a%b
#         while (remainder !=0):
#             a=b
#             b=remainder
#             remainder=a%b
#     else:
#         remainder=b%a
#         while(remainder!=0):
#             b=remainder
#             remainder=a%b
#             a=b
#     print("最大公约数： ",str(b))
#     print("最小公倍数： ", str(int(mul/b)))
# if __name__=="__main__":
#     x,y=map(int,input("please input integers:").split())
# #print(hcf(x,y))
# #print(lcm(x,y))
# division_algorithm(x,y)

# def sta(s):
#     num1=max(s)
#     num2=min(s)
#     num3=len(s)
#     return (num1,num2,num3)
# S1=[9,7,8,3,2,1,55,6]
# S2=["apple","pear","melon","kiwi"]
# S3="TheQuickBrownFox"
# print("List="+str(S1))
# print("最大值="+str(sta(S1)[0])+",最小值="+str(sta(S1)[1])+",元素个数="+str(sta(S1)[2]))
# print("List="+str(S2))
# print("最大值="+str(sta(S2)[0])+",最小值="+str(sta(S2)[1])+",元素个数="+str(sta(S2)[2]))
# print("List="+str(S3))
# print("最大值="+str(sta(S3)[0])+",最小值="+str(sta(S3)[1])+",元素个数="+str(sta(S3)[2]))

# def sum(*nums): # 定义一个变量，来保存结果
#     result = 0
#     for n in nums:# 遍历元组，并将元组中的数进行累加
#         result += n
#         print(result)
# sum(123,456,789,10,20,30,40)

# def fn2(i) :
#     if i % 2 == 0:
#         return True
#     return False
# def fn(func, lst):
# # fn()函数可以将指定列表中的所有偶数获取出来，并保存到一个新列表中返回
# # 参数 lst：要进行筛选的列表
#     new_list = []# 创建一个新列表
#     for n in lst:# 对列表进行筛选
#         if func(n): # 判断 n 的奇偶
#             new_list.append(n)
#     return new_list# 返回新列表
# l = [1,2,3,4,5,6,7,8,9,10]
# print(fn(fn2, l))

# from random import randrange #randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为 1。
# def init():
#     result = {i: 'goat' for i in range(3)} #返回一个字典，键为 3 个门号，值为门后面的物品
#     r = randrange(3)#在某个随机门后放着一辆汽车，其他两个门后面依然是山羊
#     result[r] = 'car'
#     return result
# def startGame():
# # 获取本次游戏中每个门的情况
#     doors = init()
# # 获取玩家选择的门号while True:
#     while True:
#         try:
#             firstDoorNum = int(input('Choose a door to open:'))
#             assert 0<= firstDoorNum <=2
#             break
#         except:
#             print('Door number must be between {} and {}'.format(0, 2))
# # 主持人查看另外两个门后的物品情况
# #字典的 keys 方法返回结果可以当作集合使用，支持使用减法计算差集
#     for door in doors.keys()-{firstDoorNum}:
# # 打开其中一个后面为山羊的门
#         if doors[door] == 'goat':
#             print('"goat" behind the door', door)
# # 获取第三个门号，让玩家纠结
#             thirdDoor = (doors.keys()-{door, firstDoorNum}).pop()
#             change = input('Switch to {}?(y/n)'.format(thirdDoor))
#             finalDoorNum = thirdDoor if change=='y' else firstDoorNum
#             if doors[finalDoorNum] == 'goat':
#                 return 'I Win!'
#             else:
#                 return 'You Win.'
# while True:
#     print('='*30)
#     print(startGame())
#     r = input('Do you want to try once more?(y/n)')
#     if r == 'n':
#         break

# def power(n,i):
#     if i==1:
#         return n
#     return n*power(n,i-1)
# print(power(3,3))

# class Circle():
#     def __init__(self,radius):
#         self.radius=radius
#     def length(self):
#         return self.radius*2*3.14
#     def area(self):
#         return self.radius**2*3.14
# a=int(input("please input a radius:"))
# c=Circle(a)
# print("The length is:",c.length(),"The area is:",c.area())

# class Vehicle:
#     def __init__(self,wheels,weight):
#         self.setWheels(wheels)
#         self.setWeight(weight)
#     def setWheels(self,wheels):
#         self.__wheels=wheels
#     def setWeight(self,weight):
#         self.__weight=weight
#     def getWheels(self):
#         return self.__wheels
#     def getWeight(self):
#         return self.__weight
#     def display(self):
#         print("车轮={0},重量={1}".format(self.getWheels(),self.getWeight()))
# class Car(Vehicle):
#     def __init__(self,wheels,weight,passenger_load=4):
#         super(Car,self).__init__(wheels,weight)
#         self.setPassenger(passenger_load)
#     def setPassenger(self,passenger_load,):
#         self.__passenger_load=passenger_load
#     def getPassenger(self):return self.__passenger_load
#     def display(self):
#         print("车轮={0},重量={1},载客数量={2}".format(self.getWheels(),
#         self.getWeight(),self.getPassenger()))
# class Truck(Vehicle):
#     def __init__(self,wheels,weight,passenger_load,payload):
#         super(Truck,self).__init__(wheels,weight)
#         self.setPassenger(passenger_load)
#         self.setPayload(payload)
#     def setPassenger(self,passenger_load):
#         self.__passenger_load=passenger_load
#     def setPayload(self,payload):
#         self.__payload=payload
#     def getPassenger(self):
#         return self.__passenger_load
#     def getPayload(self):
#         return self.__payload
#     def display(self):
#         print("车轮={0},重量={1},载客数量={2},载重量={3}".format(self.getWheels(),
#         self.getWeight(),self.getPassenger(),self.getPayload()))
# vehicle=Vehicle(4,10000)
# vehicle.display()
# car=Car(4,5000,4)
# car.display()
# truck=Truck(8,20000,12,12000)
# truck.display()


# class Person:
#     def __init__(self,number,name):
#         self.setNumber(number)
#         self.setName(name)
#     def setNumber(self,number):
#         self.__number=number
#     def setName(self,name):
#         self.__name=name
#     def getNumber(self):
#         return self.__number
#     def getName(self):
#         return self.__name
#     def show(self):
#         print("编号： {0},姓名： {1}".format(self.getNumber(),self.getName()))
# class Student(Person):
#     def __init__(self,number,name,ban,score):
#         super(Student, self).__init__(number,name)
#         self.setBan(ban)
#         self.setScore(score)
#     def setBan(self,ban):
#         self.__ban=ban
#     def setScore(self,score):
#         self.__score=score
#     def getBan(self):
#         return self.__ban
#     def getScore(self):
#         return self.__score
#     def show(self):
#         print("编号： {0},姓名： {1},班级： {2},成绩：{3}".format(self.getNumber(),self.getName(),self.getBan(),self.getScore()))
# class Teacher(Person):
#     def __init__(self,number,name,title,department):
#         super(Teacher, self).__init__(number,name)
#         self.setTitle(title)
#         self.setDepartment(department)
#     def setTitle(self,title):
#         self.__title=title
#     def setDepartment(self,department):
#         self.__department=department
#     def getTitle(self):
#         return self.__title
#     def getDepartment(self):
#         return self.__department
#     def show(self):
#         print("编号： {0},姓名： {1},职称： {2},部门：{3}".format(self.getNumber(),self.getName(),self.getTitle(),self.getDepartment()))
# person=Person(3,"周涛")
# person.show()
# student=Student(20,"张三丰",51853,88)
# student.show()
# teacher=Teacher(32,"吴用","讲师","软件学院")
# teacher.show()
