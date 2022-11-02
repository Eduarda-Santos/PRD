from threading import Thread
from queue import Queue
import time

class Produtor(Thread):
  def __init__(self, file, queue):
    Thread.__init__(self)
    self.file = file
    self.queue = queue
    
  def run(self):
    file = open(self.file, 'rt')
    
    for line in file:
      line = line[:-1]
      print(f'Linha: {line}')
      words = line.split(' ')
      for word in words:
        print(f'\n: {word}')
        self.queue.put(word)
    self.queue.put('!!FIM!!')
    file.close()
    print('Fim!')
        
class Consumidor(Thread):
  def __init__(self, file, queue):
    Thread.__init__(self)
    self.file = file
    self.queue = queue
    
  def run(self):
    flag = True
    bib = {}
    
    while flag:
      word = self.queue.get()
      if (word == '!!FIM!!'):
        flag = False
      else:
        if word in bib:
          bib[word] += 1
        else:
          bib[word] = 1
          self.queue.task_done()
          
    file = open(self.file, 'wt', encoding='utf-8')
    
    file.write(str(bib))
    file.close()
      
if __name__ == '__main__':
  for i in range(10):
    duration = time.time()
  
    queue = Queue(4)
    produtor = Produtor('dicionario.txt', queue)
    produtor.start()
    
    consumidor = Consumidor('bib.txt', queue)
    consumidor.start()
    
    produtor.join()
    consumidor.join()
    
    duration = time.time() - duration
    
    with open('tempos.txt', 'a+', encoding='utf-8') as file:
      file.write(f'Tempo com (Thread): {duration}\n')
      if(i == 9):
        file.write(f'FIM\n')
    print('Finalizado!')
  