class Person:
	def __init__(self, name, age, pay=0, job=None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job
	def tax(self):
		return self.pay * 0.25
	def info(self):
		return self.name, self.job, self.pay, self.tax()	
