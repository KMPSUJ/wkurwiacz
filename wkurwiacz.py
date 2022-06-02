#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time, sleep, mktime
from datetime import date
import random
import os


class Annoyer(object):
	def __init__(self, seconds):
		self.minutes = int((seconds - (seconds%60))/60)
		self.hours = int((self.minutes - (self.minutes%60))/60)
		self.days = int((self.hours - (self.hours%24))/24)
		self.minutes = self.minutes - 60*self.hours
		self.hours = self.hours - 24*self.days

	def mh_end(self, number):
		if number == 1:
			return "a "
		if number in [12, 13, 14]:
			return " "
		if number%10 in [2, 3, 4]:
			return "y "
		else:
			return " "

	def days_end(self):
		if self.days == 1:
			return "dzień, "
		else:
			return "dni, "

	def dwojkopoprawiacz(self, number):
		if number%10 == 2 and number != 12:
			return str(number-2) + " dwie"
		else:
			return str(number)

	def anoy(self):
		WARNING = "'Do sesji zostało " + str(self.days) + " " + self.days_end() \
		        + self.dwojkopoprawiacz(self.hours) + " godzin" + self.mh_end(self.hours) \
		        + "i " + self.dwojkopoprawiacz(self.minutes) + " minut" + self.mh_end(self.minutes) \
		        + ". Ruszcie się wy nieroby!'"
		os.system("espeak -s100 -a100 -v pl -k40 " + WARNING)


hold = 60*random.uniform(0, 120)
sleep(hold)

deadline = mktime(date(2020, 1, 29).timetuple()) + 8*60*60
time_left = deadline - time()

if time_left < 0:
	WARNING = "wszyscy zginiemy!"
	os.system("'espeak -s100 -a100 -v pl -k40 " + WARNING + "'")
	exit()

session = Annoyer(time_left)
session.anoy()
