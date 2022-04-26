from tarfile import TarError
from threading import Thread
import time

COUNT = 90


def reload():
    global COUNT
    while True:
        print(COUNT)
        time.sleep(3)
        COUNT = 0


Thread(target=reload).start()
input("XD")
