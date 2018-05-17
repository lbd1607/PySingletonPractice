#Laura Davis 30 June 2017

#Lesson and source code from YouTube user Trevor Payne
#This program demonstrates how to create and use 
#singletons in Python

#singletons the long way
class MySingleton(object):
	_instance = None;
	def __new__(self):
		if not self._instance:
			self._instance = super(MySingleton, self).__new__(self)
			self.y = 10
		return self._instance
		
x = MySingleton()
print x.y
x.y = 20
z = MySingleton()
print z.y



#singletons the easy way [decorator]
def singleton(myClass):
	instances = {}
	def getInstance(*args, **kwargs):
		if myClass not in instances:
			instances[myClass] = myClass(*args, **kwargs)
		return instances[myClass]
	return getInstance
	
@singleton
class TestClass(object):
	pass
	
x = TestClass()

