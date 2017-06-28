
# coding: utf-8

# ## 目录

# ### Task0:markdown、GitHub、jupyter notebook用法
# ### Task1:显示（print）
# ### Task2:数学运算；while循环
# ### Task3:if语句；分隔符；
# ### Task4:定义函数
# ### Task5:编程规划；多行文本；random模块；math模块
# ### Task6:序列list；for循环；format；字符转义
# ### Task7:图形字符；序列切片；元组；id( )函数
# ### Task8:文件读取及写入；字符处理；序列处理；random模块；打开文件模式
# ### Task9:统计词频；

# ## 常用运算符号

# In[1]:

print(4+6)      #运算符:'+'。功能：加法。结果：10
print(3.5-2)    #运算符:'-'，功能：减法。结果：1.5
print(9*9)      #运算符:'*'，功能：乘法。结果：81
print(5/2)      #运算符:'/'，功能：除法。结果：2.5
print(5**3)     #运算符:'**'，功能：乘幂。结果：125
print(5//2)     #运算符:'//'，功能：整除(舍去小数部分)。结果：2
print(7%3)      #运算符:'%'，功能：求余数(模)。结果：1


# ## 比较符号

# In[1]:

print(10 == 10)       #运算符：'=='。说明：等于。表达式值：True
print(10 != 10)       #运算符：'!='。说明：不等于。表达式值：False
print(10 > 5.1)       #运算符：'>'。说明：大于。表达式值：True
print(10.2 < 5)       #运算符：'<'。说明：小于。表达式值：False
print(5 >= 10)        #运算符：'>='。说明：大于等于。表达式值：False
print(5 <= 10)        #运算符：'<='。说明：小于等于。表达式值：True


# ## 分隔符

# In[2]:

print('多个参数', 5, 4078%211, 407.8//211)
print('多个参数', 5, 4078%211, 407.8//211, sep = '  ')
print('多个参数', 5, 4078%211, 407.8//211, sep = ',')
print('多个参数', 5, 4078%211, 407.8//211, sep = ' ')
print('多个参数', 5, 4078%211, 407.8//211, sep = ' ,')
print('多个参数', 5, 4078%211, 407.8//211, sep = '')


# ## 常用math模块

# 几个常用的函数如下：
# math.ceil(x)
# Return the ceiling of x, the smallest integer greater than or equal to x.
# math.floor(x)
# Return the floor of x, the largest integer less than or equal to x.
# math.exp(x)
# Return e**x
# math.log(x[, base])
# With one argument, return the natural logarithm of x (to base e).
# With two arguments, return the logarithm of x to the given base.
# math.log2(x)
# Return the base-2 logarithm of x. This is usually more accurate than log(x, 2).
# math.log10(x)
# Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).
# math.sqrt(x)
# Return the square root of x.
# math.sin(x)
# Return the sine of x radians.
# math.cos(x)
# Return the cosine of x radians.
# 

# ## 改变字符串格式

# In[4]:

print('a={0},b={1},c={2}'.format(0,1,2))
print('a={1},b={0},c={2}'.format(0,1,2))
print('----------分隔符-------------')
# 基本用法 2：
n=20
print('{:3},{:3}'.format(n,10*n))
print('{:3},{:3}'.format(10*n,n))


# ## 序列切片

# In[1]:

line = '北京语言大学信息科学学院'

print(line[2:6])
print(line[2:8:2])
print(line[8:1:-2])

print('-'*15 + '分割线' + '-'*15)

print(line[0:6])
print(line[:6])
print(line[6:12])
print(line[6:])
print(line[:])
print(line[::2])

print('-'*15 + '分割线' + '-'*15)

print(line[-5:-2])
print(line[0:4] + line[3::-1])


# ## 字符处理

# In[3]:

replace() #替换字符；字符串.replace(old_str, new_str)
split() #将字符按照分隔符分开；字符串.split(sep)
write() #向文件写入字符串;文件对象.write(str)


# ## 序列处理

# In[ ]:

str.join(...) #将序列内所有元素之间均用str进行连接的方法;分隔字符串.join(...)
choice() #在序列随机抽取对象；random.choice(seq)
shuffle(...) #random模块中的随机打乱序列内部对象顺序；random.shuffle(序列)
permutations(..., int) #得到序列全排列的函数，第一个参数是序列，第二个参数是取第一个序列中多少个元素来做全排列,该函数在itertools模块中，需要提前import


# ## 统计

# In[ ]:



