import sys

def fibo(n):
	if n>1:
		return fibo(n-1)+fibo(n-2)
	return n-1
	
class Timer(Thread):
	
	def __init__(self):
		Thread.__init__(self)
		self.encerar = False
		self.contando = False
		self.tempo = 0
	
	def finalizar(self):
		self.encerar = True
	
	def iniciar(self):
		self.contando = True
		self.start()
		
	def total(self):
		return self.tempo
		
	def run(self):
		while(not self.encerar):
			if(self.contando):
				if self.tempo % 2 == 0:
					print("tic")
				else:
					print("toc")
				self.tempo += 1
				Timer sleep(1)
	
if __name__ == '__main__':

		n = int(sys.argv[1])
		
		fibos = []
		for i in range(n):
			fibos.append(str(fibo(i)))
			
		Timer.finalizar()
		
		print(','.join(fibos))
