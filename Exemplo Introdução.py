from multiprocessing import Process 
import multiprocessing 
import time 


def soneca(id,tempo): 

    id = multiprocessing.current_process 

    print(f“Processo {id} indo dormir...”) 

    time.sleep(tempo) 

    print(f“Processo {id} acordei...”) 

 

if __name__ == ‘__main__’: 


    inicio = time.time() 

    p1 =
     Process(target=soneca,args=(1,1)) 
    p2 = Process(target=soneca,args=(2,1)) 

    p1.start() 
    p2.start() 

    

    p1.join() 
    p2.join() 

    

    fim = time.time() 

    

    print(f“tempo total (fim-inicio)”) 