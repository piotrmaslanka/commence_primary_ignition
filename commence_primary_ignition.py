import requests
from satella.coding.concurrent import TerminableThread, ThreadCollection
from satella.os import hang_until_sig
from satella.random import random_word


class CounterTerroristsWin(TerminableThread):
    def loop(self):
        email = random_word(random.randint(5, 15)) + '@' + random_word(random.randint(5, 15)) + '.' + random_word(2)
        password = random_word(random.randint(10, 30))

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
