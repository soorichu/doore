# -*- coding: UTF-8 -*-
import random
import datetime
import json


class GameChractor:
	change = {"warrior":[5, 2, 1, 1], "wizzard":[1, 2, 5, 1], "person":[2, 3, 2, 1]}
	item = {"knife":[2, 2, 1, 0], "ax":[3, 2, 1, 0], "speer":[2, 3, 1, 0], 'stick':[0, 0, 5, 0], 'jewel':[1, 1, 1, 3], 'potion':[2, 2, 2, 2]}

	def __init__(self, name, job):
		self.name = name
		if job != "warrior" and job != "wizzard": self.job = "person"
		else: self.job = job
		self.ability = {"power": 10, "speed":10, "intel":10, "soul":10}
		self.level = 5
		self.before_abi = 30
		print("Hi {0}({1})".format(self.name, self.job))

	def level_up(self, i):
		self.level += i
		if i>0: print(self.name, "Level Up", self.level)
		elif i<0: print(self.name, "Level Down", self.level)

	def power_up(self, i):
		self.ability["power"] += self.change[self.job][0]*i
		self.level_check()

	def speed_up(self, i):
		self.ability["speed"] += self.change[self.job][1]*i
		self.level_check()

	def intel_up(self, i):
		self.ability["intel"] += self.change[self.job][2]*i
		self.level_check()

	def soul_up(self, i):
		self.ability["soul"] += self.change[self.job][3]*i
		self.level_check()

	def level_check(self):
		if self.ability["power"]<0: 
			self.level_up(-1); self.ability["power"]=5
			self.before_abi = self.ability["power"]+self.ability["speed"]+self.ability["intel"]
		if self.ability["speed"]<0: 
			self.level_up(-1); self.ability["speed"]=5
			self.before_abi = self.ability["power"]+self.ability["speed"]+self.ability["intel"]
		if self.ability["intel"]<0: 
			self.level_up(-1); self.ability["intel"]=5
			self.before_abi = self.ability["power"]+self.ability["speed"]+self.ability["intel"]

		temp_ability = self.ability["power"]+self.ability["speed"]+self.ability["intel"]
		if temp_ability - self.before_abi >= 10:
			self.level_up(+1)
			self.before_abi = temp_ability

	def fight(self, war2):
		print("Fight {0} vs {1} !".format(self.name, war2.name))
		war1_point = self.level*self.ability["speed"] + self.ability["power"]+self.ability["intel"] + random.randrange(-5, 5)
		war2_point = war2.level*war2.ability["speed"] + war2.ability["power"]+war2.ability["intel"] + random.randrange(-5, 5)
		if war1_point > war2_point:
			print(self.name, "is Victory!")
			self.power_up(+1); self.speed_up(+1); self.intel_up(+1)
			war2.power_up(-1); war2.speed_up(-1); war2.intel_up(-1)
		else:
			print(war2.name, "is victory!")
			self.power_up(-1); self.speed_up(-1); self.intel_up(-1)
			war2.power_up(+1); war2.speed_up(+1); war2.intel_up(+1)
			

	def show_info(self):
		p = {'name': self.name, 'job':self.job, 'power':self.ability['power'], 
			'speed':self.ability['speed'], 'intel':self.ability['intel'], 
			'soul':self.ability['soul'], 'level':self.level, 'before_abi':self.before_abi}
		j = json.dumps(p)
		print(j)

	def save(self):
		p = {'name': self.name, 'job':self.job, 'power':self.ability['power'], 
			'speed':self.ability['speed'], 'intel':self.ability['intel'], 
			'soul':self.ability['soul'], 'level':self.level, 'before_abi':self.before_abi}
		j = json.dumps(p)
		file = open("save.sv", "w")
		file.write(j)
		file.close()

	def __del__(self):
		self.save()
		print("Bye "+self.name)



def game(n, war1, war2):
	if n == 0: war1.power_up(+1)
	if n == 1: war1.speed_up(+1)
	if n == 2: war1.intel_up(+1)
	if n == 3: war1.fight(war2)
	if n == 4: war1.soul_up(+1)

w1 = GameChractor("Soori", "warrior")
w2 = GameChractor("Mini", "wizzard")
for i in range(100):
	rd1 = random.randrange(0, 5)
	rd2 = random.randrange(0, 5)
	print("\n###Try", i, "###")
	game(rd1, w1, w2); game(rd2, w2, w1)
	w1.show_info(); w2.show_info()
