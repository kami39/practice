#-*- coding: UTF-8 -*-

class human(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print("human born %s %d"% (name, age))
	def speak(self,content):
		print("hello! %s"%content)

class male(human):
	# def __init__(self,name,age,height):
	# 	human.__init__(self,name,age)		#调用父类方法要加self
	# 	self.height = height
	# 	print("i tall %d " % height + "cm")
	def talk(self,content):
		human.speak(self,content)			#调用父类方法要加self
		print("-----------------------")
		print(content)

if __name__ == "__main__":
	# t = human("tt",18)
	# t.speak("model")
	watasi = male("wusz",18)
	watasi.talk("xixixi")

