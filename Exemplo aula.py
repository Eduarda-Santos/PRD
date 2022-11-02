import threading
from threading import Thread
import time

def operacao(valor):

    for i in range(10):
        print(f"{threading.current_thread().getName()}Realizando opeação {valor}")
        time.sleep(2)

if __name__ == "__main__":

    N = 5

    threads = []

    for i in range(N):
        thread  = Thread(target=operacao, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


    print("F")

    operacao()

