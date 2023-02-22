#print可以打印数字
print(520)

#print可以打印表达式
print(3+12)

#print可以打印字符串
print("hello world")

#不换行输出
print('hello','world')

#以上是输出到显示器

#输出到文件
fp = open('D:\code\python\python_2_22/test.txt','a+')
print('hello world',file = fp)
fp.close()
