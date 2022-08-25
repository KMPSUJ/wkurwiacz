#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time, sleep, mktime
from datetime import date, datetime
import random
import os
import sys

# consts
JOKES_PATH = os.path.dirname(os.path.realpath(__file__)) + "/zarty.txt"


class Annoyer(object):
        zarty: list
        number: int

        def __init__(self, jokes_path):
            self.load_jokes(jokes_path)
        
        def load_jokes(self, path) -> None:
            with open(path, "r") as f:
                selt.zarty = f.readlines()
            self.number = len(self.zarty)
            return None

        def losuj(self, number):
            return random.choice(self.zarty)

        def anoy(self):
            WARNING =self.losuj(1)
            os.system("espeak -s100 -a100 -v pl -k40 " + WARNING)
            with open('wkurwiaczlog.txt', 'a') as wl:
                wl.write(f'\n{datetime.now()}: {WARNING}')


if __name__ == '__main__':
    # date should be passed in the following way:
    # python3 THIS_SCRIPT_NAME YEAR MONTH DAY
    if len(sys.argv) != 4:
        raise Exception("Wrong argument format!\n\tPass th date of exams as 3 args:\n\tYEAR MONTH DAY")
    exams_date = date(*[int(i) for i in sys.argv[1:4]])

    hold = 60*random.uniform(0, 120)
    sleep(hold)

    deadline = mktime(exams_date.timetuple()) + 8*60*60
    time_left = deadline - time()

    if time_left < 0:
	    WARNING = "wszyscy zginiemy!"
	    os.system("'espeak -s100 -a100 -v pl -k40 " + WARNING + "'")
	    exit()

    session = Annoyer(JOKES_PATH)
    session.anoy()
