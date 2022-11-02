import time
import requests
import concurrent.futures

def get_wiki_page_existence(wiki_page_url, timeout=10):
	
	response = requests.get(url=wiki_page_url, timeout=timeout)

	page_status = "unknown"
	if response.status_code == 200:
		page_status = "exists"
	elif response.status_code == 404:
		page_status = "doesn't exist"
		
	return wiki_page_url + " - " + page_status
		
if __name__ == '__main__':
	
    print("Excutando com threads:")

	wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(15)]
		
	inicio = time.time()
		
	executor = concurrent.futures.ThreadPoolExecuteor(max_worker=2)

	f = open('arquivo', 'w')
	respostas = []
	arquivo = respostas.split(",")

	for url in  wiki_page_urls:
		respostas.append(executor.submit(get_wiki_page_existence,wiki_page_url=url))
		
	print("Tarefas submetidas..")

	executor.shutdown(wait=True)
		
	for future in concurrent.futures.as_completed(respostas):
		print(future.result())

	fim = time.time()

	print(f"Tempo sequencial: {fim-inicio}s")