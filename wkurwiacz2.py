#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time, sleep, mktime
from datetime import date, datetime
import random
import os


class Annoyer(object):
        def __init__(self, seconds):
            self.number=4
            self.zarty=["'Kiedy ktoś opowie hamski żart przy stole. '",
                    "'Jak nazywa się moment przed zjedzeniem bułki? Preambuła. Hahahaha'",
                    "'Wiesz dlaczego nóż poszedł do piekła? Bo został potępiony.'",
                    "'Co robi koala w płonącym lesie? Płonie.'"]
        def losuj(self, number):
            return random.choice(self.zarty)

        def anoy(self):
            WARNING =self.losuj(1)
            os.system("espeak -s100 -a100 -v pl -k40 " + WARNING)
            with open('wkurwiaczlog.txt', 'a') as wl:
                wl.write(f'\n{datetime.now()}: {WARNING}')


hold = 60*random.uniform(0, 120)
sleep(hold)

deadline = mktime(date(2022, 6, 17).timetuple()) + 8*60*60
time_left = deadline - time()

if time_left < 0:
	WARNING = "wszyscy zginiemy!"
	os.system("'espeak -s100 -a100 -v pl -k40 " + WARNING + "'")
	exit()

session = Annoyer(time_left)
session.anoy()
