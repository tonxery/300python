#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
import thread,random,time
def timer(interval):
	for i in range(5):
		time.sleep(random.choice(range(interval)))
		thread_id = thread.get_ident()
		print 'Thread:{0} Time:{1}\n'.format(thread_id,time.ctime())
def test():
	thread.start_new_thread(timer,(5,))
	thread.start_new_thread(timer,(5,))
if __name__ == '__main__':
	test()
'''
#-----------------------线程创建实例一-----------------------
'''
import threading,time,random
def timer(interval):
	for i in range(5):
		time.sleep(random.choice(range(interval)))
		thread_id=threading._get_ident()
		print 'Thread:{0} Time:{1}\n'.format(thread_id,time.ctime())
def test():
	t1 = threading.Thread(target=timer,args=(5,))
	t2 = threading.Thread(target=timer,args=(6,))
	t1.start();t2.start()
if __name__ == '__main__':
	test()
'''
'''
#-----------------------自定义派生实例对象-----------------------
import threading,time,random
class MyThread(threading.Thread):
	def __init__(self,interval):
		threading.Thread.__init__(self)
		self.interval=interval
	def run(self):
		for i in range(5):
			time.sleep(random.choice(range(self.interval)))
			thread_id = threading._get_ident()
			print 'Thread:{0} Time:{1}\n'.format(thread_id,time.ctime())
if __name__ == '__main__':
	t2 = MyThread(5)
	t1.start();t2.start()
'''
#-----------------------线程加入join()-----------------------
'''
import threading,time,random
class MyThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		for i in range(5):
			time.sleep(1)
			t = threading.current_thread()
			print '{0} at {1}\n'.format(t.name,time.ctime())
		print 'The Thread is OVER!!!'
def test():
	t1 = MyThread()
	t1.name = 't1'
	t1.start()
	print 'The main Thread status start(t1)2s';t1.join(2)
	print 'The main Thread status (t1)2sover'
	print 'The main start status over';t1.join()
	print 'the main over'

if __name__ == '__main__':
	test()
'''
print "########################3"
