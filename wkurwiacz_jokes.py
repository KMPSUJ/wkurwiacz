#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time, sleep, mktime
from datetime import date, datetime
import random
import os
import sys

# consts
JOKES_PATH = os.path.dirname(os.path.realpath(__file__)) + "/zarty.txt"


class JokesAnnoyer(object):
        jokes: list

        def __init__(self, jokes_path):
            self.load_jokes(jokes_path)
        
        def load_jokes(self, path) -> None:
            with open(path, "r") as f:
                self.jokes = f.readlines()

        def pick_joke(self) -> str:
            return random.choice(self.jokes)

        def anoy(self) -> None:
            CHOSEN_JOKE = self.pick_joke()
            os.system("espeak -s100 -a100 -v pl -k40 " + CHOSEN_JOKE)
            with open('wkurwiaczlog.txt', 'a') as wl:
                wl.write(f'\n{datetime.now()}: {CHOSEN_JOKE}')


if __name__ == '__main__':
    # date should be passed in the following way:
    # python3 THIS_SCRIPT_NAME YEAR MONTH DAY
    if len(sys.argv) != 4:
        raise Exception("Wrong argument format!\n\tPass the date of exams as 3 args:\n\tYEAR MONTH DAY")
    exams_date = datetime(*[int(i) for i in sys.argv[1:4]],8)

    hold = 60*random.uniform(0, 120)
    # sleep(hold)

    deadline = mktime(exams_date.timetuple())
    time_left = deadline - time()

    if time_left < 0:
	    WARNING = "wszyscy zginiemy!"
	    os.system("espeak -s100 -a100 -v pl -k40 '" + WARNING + "'")
	    sys.exit()

    session = JokesAnnoyer(JOKES_PATH)
    session.anoy()
