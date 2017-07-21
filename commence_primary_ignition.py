#!/usr/bin/python
from __future__ import print_function

import random
import os
import string
import threading

os.system('pip install requests')



import requests


def rand_string(n):
    return b''.join(random.choice(string.ascii_lowercase) for _ in range(n))


class CounterTerroristsWin(threading.Thread):
    def run(self):
        while True:
            email = rand_string(random.randint(5, 15)) + '@' + rand_string(random.randint(5, 15)) + '.' + rand_string(2)
            password = rand_string(random.randint(10, 30))

            r = requests.post('http://www.pmodavao.com/regs/js/dt/crypt/pass.php', data={'email': email})

            if r.status_code == 200:
                r = requests.post('http://www.pmodavao.com/regs/js/dt/crypt/post.php',
                                  data={'email': email, 'password': password})

                if r.status_code != 200:
                    print('And when Im gone just carry on')


if __name__ == '__main__':
    q = [CounterTerroristsWin() for _ in xrange(20)]
    for q in q:
        q.start()
