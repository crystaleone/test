class Person:
	def __init__(self, name, age, pay=0, job=None):
		self.name = name
		self.job = job
		self.pay = pay
	def __getattr__(self, attr):
		if attr == 'tax':
			return self.pay * 0.30
		else:
			raise AttributeError()
	def info(self):
		return self.name, self.job, self.pay, self.tax	
