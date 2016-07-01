#!/usr/bin/env python
#-*- coding:utf-8 -*-
#-----------------------类的继承-----------------------
#-----------------------类的多重继承-----------------------
#-----------------------内置迭代器iter()-----------------------
#-----------------------生成器创建Yield()有问题-----------------------
#-----------------------装饰器函数有问题-----------------------
#-----------------------装饰器类不理解-----------------------
#-----------------------闭包-----------------------
#-----------------------闭包与延迟求值-----------------------
#-----------------------闭包与泛型函数-----------------------
#-----------------------字典构成分支程序-----------------------
#-----------------------重载类的特殊方法-----------------------
#----------------------鸭子类型与多态-----------------------
#----------------------文件读取操作-----------------------
#----------------------用threading.Thread直接在线程中运行-----------------------
#----------------------通过继承threading.Thread类来创建线程(有问题)-----------------------
#----------------------纯程类Thread使用(join()属性函数基本用法)-----------------------
#----------------------纯程类Thread使用(daemon属性函数基本用法)(有问题)-----------------------
#----------------------纯程锁RLock的使用-----------------------
#----------------------纯程通过Event唤醒对方-----------------------
#----------------------进程基础调用系统基础-----------------------
#----------------------用Popen类创建进程(有问题)-----------------------
'''
#-----------------------类的继承-----------------------
class Ant:
	def __init__(self,x=0,y=0,color='black'):
		self.x = x
		self.y = y
		self.color = color
	def crawl(self,x,y):
		self.x = x
		self.y = y
		print 'paxing...'
	def info(self):
		print 'The now plance %d,%d'%(self.x,self.y)
	def attack(self):
		print 'mouth...'
class FlyAnt(Ant):
	def attack(self):
		print 'The zhen zha!!!'
	def fly(self,x,y):
		print 'fly......'
		self.x = x
		self.y = y 
		self.info()
flyant = FlyAnt()
flyant.crawl(3,5)
flyant.fly(10,14)
flyant.attack()
'''
#-----------------------类的多重继承-----------------------
'''
class PrintA:
	namea = 'PrintA'
	def set_value(self,a):
		self.a = a
	def set_namea(self,namea):
		PrintA.namea = namea
	def info(self):
		print 'PrintA:%s,%s'%(PrintA.namea,self.a)
class PrintB:
	nameb = 'PrintB'
	def set_nameb(self,nameb):
		PrintB.nameb = nameb
	def info(self):
		print 'PrintB:%s'%PrintB.nameb
class Sub(PrintA,PrintB):
	pass
class Sub2(PrintB,PrintA):
	pass
class Sub3(PrintA,PrintB):
	def info(self):
		PrintA.info(self)
		PrintB.info(self)

print 'Use first subprocess class:'
sub = Sub()
sub.set_value('aaaa')
sub.info()
sub.set_nameb('BBBB')
sub.info()

print 'Use second subprocess class:'
sub2 = Sub2()
sub2.set_value('aaaaa')
sub2.info()
sub2.set_nameb('BBBBB')
sub2.info()

print 'Use Thirtd subprocess class:'
sub3 = Sub3()
sub3.set_value('aaaaa')
sub3.info()
sub3.set_nameb('BBBBBB')
sub3.info()
'''
#-----------------------内置迭代器iter()-----------------------
'''
class Counter:
	def __init__(self,x=0):
		self.x = x
counter = Counter()
def used_iter():
	counter.x += 2
	return counter.x
for i in iter(used_iter,8):
	print 'This craw is :',i
'''
#-----------------------生成器创建Yield()有问题-----------------------
'''
def myYield(n):
	while n>0:
		print "start is shengcheng...:"
		yield n
		print "the over one !"
		n -= 1
if __name__ == '__main__':
	for i in myYield(4):
		print "bian li is values:",i 
	print ()
	my_yield = myYield(3)
	print 'yijingshilihuashengchengduixiang'
	my_yield.__next__()
	print 'second diaoyong next'
	my_yield.__next__()
'''
'''
def myYield(n):
	while n>0:
		rcv = yield n 
		n -= 1
		if rcv is not None:
			n = rcv
if __name__ == '__main__':
	my_yield = myYield(3)
	print my_yield.__next__()
'''
#-----------------------装饰器函数有问题-----------------------
'''
def abc(fun):
	def wrapper(*args,**kwargs):
		print 'Start Runing...!!!'
		fun(*args,**kwargs)
		print 'Runing Stop....!!!'
		return wrapper
@abc
def demo_decoration(x):
	a = []
	for i in range(x):
		a.append(i)
	print a

@abc
def hello(name):
	print 'Hello',name

if __name__ == '__main__':
	demo_decoration(5)
	print ()
	hello('John')
'''
#-----------------------装饰器类不理解-----------------------
'''
def abc(myclass):
	class InnerClass:
		def __init__(self,z=0):
			self.z = 0
			self.wrapper = myclass()
		def position(self):
			self.wrapper.position()
			print('z axis:',self.z)
	return InnerClass
@abc
class coordination:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y
	def position(self):
		print ('x axis:',self.x)
		print ('y axis:', self.y)

if __name__ == '__main__':
	coor = coordination()
	coor.position()
'''
#-----------------------闭包-----------------------
'''
x = 14
def foo():
	x = 3
	def bar():
		print ('x is %d'%x)
	bar()
if __name__ == '__main__':
	foo()
'''
#-----------------------闭包与延迟求值-----------------------
'''
def delay_fun(x,y):
	def caculator():
		return x + y
	return caculator
if __name__ == '__main__':
	print 'return a sum function,'
	msum = delay_fun(3,4)
	print ( )
	print ('qiu he:')
	print (msum())
'''
#-----------------------闭包与泛型函数-----------------------
'''
def line(a,b):
	def aline(x):
		return a*x + b 
	return aline 
if __name__ == '__main__':
	line23 = line(2,3)
	line50 = line(5,0)
	print (line23(4))
	print (line50(2))
'''
#-----------------------字典构成分支程序-----------------------
'''
import random
def path_a():
	print ('papth_branch_A')
def path_b():
	print ('path_brahch_B')
def path_c():
	print ('path_brahch_C')
if __name__ == '__main__':
	path_dict = {}
	path_dict['a'] = path_a
	path_dict['b'] = path_b
	path_dict['c'] = path_c
	paths = 'abc'
	for i in range(4):
		path = random.choice(paths)
		print ('You Choice path:',path)
		path_dict[path]()
'''
#-----------------------重载类的特殊方法-----------------------
'''
class Book:
	def __init__(self,name="Python入门到应用"):
		self.name = name
	def __add__(self,obj):
		return self.name + ' add ' + obj.name
	def __len__(self):
		return len(self.name)
if __name__ == '__main__':
	booka = Book()
	bookb = Book('Java入门到应用')
	print ("len(booka):",len(booka))
	print ("len(bookb:",len(bookb
'''
#----------------------鸭子类型与多态-----------------------
'''
class Duck:
	def __init_(self,name='Duck'):
		self.name = name
	def quack(self):
		print ("嗄嗄嗄...")

class Cat:
	def __init__(self,name="Cat"):
		self.name = name
	def quack(self):
		print ("喵喵喵...")

class Tree:
	def __init__(self,name="Tree"):
		self.name = name

def duck_demo(obj):
	obj.quack()

if __name__ == '__main__':
	duck = Duck()
	cat = Cat()
	tree = Tree()
	duck_demo(duck)
	duck_demo(cat)
	#duck_demo(tree)  无quack()此方法所以出现异
'''
#----------------------文件读取操作-----------------------
'''
def file_hdl(name='README.md'):
	f = open(name)
	read = f.readlines()
	print read
if __name__ == '__main__':
	file_hdl('../12306.txt')
'''
#----------------------用threading.Thread直接在线程中运行-----------------------
'''
import threading
def thrfun(x,y):
	for i in range(x,y):
		print (str(i*i)+';')
ta = threading.Thread(target=thrfun,args=(1,6))
tb = threading.Thread(target=thrfun,args=(16,21))
ta.start()
tb.start()
'''
#----------------------通过继承threading.Thread类来创建线程(有问题)-----------------------
'''
import threading
class myThread(threading.Thread):
	def __init__(self,mynum):
		super().__init__()
		self.mynum = mynum
	def run(self):
		for i in range(self.mynum,self.mynum+5):
			print (str(i*i)+';')
ma = myThread(1)
ma.start()
'''
#----------------------纯程类Thread使用(join()属性函数基本用法)-----------------------
'''
import threading
import time
def thrfun(x,y,thr=None):
	if thr:
		thr.join()
	else:
		time.sleep(2)
	for i in range(x,y):
		print(str(i*i)+';')
ta = threading.Thread(target=thrfun,args=(1,6))
tb = threading.Thread(target=thrfun,args=(16,21,ta))
ta.start()
tb.start()
'''
#----------------------纯程类Thread使用(daemon属性函数基本用法)(有问题)-----------------------
'''
import threading
import time
class myThread(threading.Thread):
	def __init__(self,mysum):
		super().__init__()
		self.mynum = mynum
	def run(self):
		time.sleep(1)
		for i in range(self.mynum,self.mynum+5):
			print(str(i*i+';'))
def main():
	print('start...')
	ma=myThread(1)
	mb=myThread(16)
	ma.daemon=True 
	mb.daemon=True
	ma.start()
	mb.start()
	print('end...')
if __name__ == '__main__':
	main()
'''
#----------------------纯程锁RLock的使用-----------------------
'''
import threading
import time
class myThread(threading.Thread):
	def run(self):
		global x
		lock.acquire()
		for i in range(3):
			x += 10
		time.sleep(1)
		print(x)
		lock.release()
x = 0
lock = threading.RLock()
def main():
	thrs = []
	for item in range(5):
		thrs.append(myThread())
	for item in thrs:
		item.start() 
if __name__ == '__main__':
	main()
'''
#----------------------纯程通过Event唤醒对方-----------------------
'''
import threading
import time
class myThreada(threading.Thread):
	def run(self):
		evt.wait()
		print(self.name,':Good morning!')
		evt.clear()
		time.sleep(1)
		evt.set()
		time.sleep(1)
		evt.wait()
		print(self.name,":I'm fine,thak you.")

class myThreadb(threading.Thread):
	def run(self):
		print(self.name,':Good morning!')
		evt.set()
		time.sleep(1)
		evt.wait()
		print(self.name,':How are you?')
		evt.clear()
		time.sleep(1)
		evt.set()

evt = threading.Event()

def main():
	John = myThreada()
	John.name = "John"
	Smith = myThreadb()
	Smith.name = "Smith"
	John.start()
	Smith.start()

if __name__ == '__main__':
	main()
'''
#----------------------进程基础调用系统基础-----------------------
'''
import subprocess
print('call() test:',subprocess.call(['python','protest.py']))
print('')
print('check_call() test:',subprocess.check_call(['python','protest.py']))
print('')
#print('getstatusoutput() test:',subprocess.getstatusoutput(['python','protest.py']))
print('')
'''
#----------------------用Popen类创建进程(有问题)-----------------------
'''
import subprocess
prcs = subprocess.Popen(['python','protest.py'],
						stdout=subprocess.PIPE,
						stdin=subprocess.PIPE
												stderr=subprocess.PIPE,
						universal_newlines=True,
						shell=True
						)
prcs.communicate('These strings are from stdin.')
print("subprocess pid:",prcs.pid)
print('\nSTDOUT:')
print(str(prcs.communicate()[0]))
print('STDERR:')
print(prcs.communicate()[1])
'''
