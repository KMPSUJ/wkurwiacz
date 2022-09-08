#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time, sleep, mktime
from datetime import date, datetime
import random
import os
import sys


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
		if number == 1:
			return "jedna"
		if number == 2:
			return "dwie"
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
		with open('wkurwiaczlog.txt', 'a') as wl:
			wl.write(f'\n{datetime.now()}: {WARNING}')


if __name__ == '__main__':
    # date should be passed in the following way:
    # python3 THIS_SCRIPT_NAME YEAR MONTH DAY
    if len(sys.argv) != 4:
        raise Exception("Wrong argument format!\n\tPass the date of exams as 3 args:\n\tYEAR MONTH DAY")
    exams_date = datetime(*[int(i) for i in sys.argv[1:4]],8)

    hold = 60*random.uniform(0, 120)
    #sleep(hold)

    deadline = mktime(exams_date.timetuple())
    time_left = deadline - time()

    if time_left < 0:
	    WARNING = "wszyscy zginiemy!"
	    os.system("espeak -s100 -a100 -v pl -k40 '" + WARNING + "'")
	    sys.exit()

    session = Annoyer(time_left)
    session.anoy()
