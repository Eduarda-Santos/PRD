import concurrent.futures 

from threading import Thread 
from time import sleep 
from random import randint 


def tarefa(id):
    print(f"Iniciando thread..{id}") 
    x=0 

    while(x<10): 
        sleep(randint{1,3})
        x+=1 