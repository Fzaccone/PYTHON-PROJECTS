import requests

#IMPOSTA L'URL DEL SERVER DVWA

url = "inserire indirizzo ip con http:// davanti" #MODIFICA L'URL IN BASE AL TUO SERVE DVWA

#FUNZIONE PER INVIARE UNA RICHIESTA HTTP GENERICA (GET, POST, PUT, DELETE)

def send_request (method, url, data = None):

	try:
		if method == "GET":
			response=requests.get(url)
		elif method == "POST":
			response=requests.post(url,data=data)
		elif method == "PUT":
			response=requests.put(url,data=data)
		elif method == "DELETE":
			response=requests.delete(url)
		else:
			print("metodo http non supportato")

#STAMPA LA RISPOSTA

		print("\n{method} Request:")
		print(f"status code: {response.status_code}")
		print(f"response text: {response.text[:200]}...") #MOSTRA SOLO I PRIMI 200 CARATTERI

	except requests.exceptions.RequestException as e:
		print(f"errore nella richiesta {method}:{e}")

#FUNZIONE PRINCIPALE 

def main ():

#INVIO DELLE RICHIESTE CON I METODI HTTP

	send_request("GET", url)
	send_request("POST", url, data={"username": "admin","password": "password"})
	send_request("PUT", url, data={"key": "value"})
	send_request("DELETE", url)

main()
