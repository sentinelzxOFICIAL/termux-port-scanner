import socket
import subprocess
import sys
from datetime import datetime

def clear_screen():
    subprocess.call('clear', shell=True)

def get_target():
    return input("Digite o endereço IP remoto a ser escaneado: ")

def scan_ports(remoteServerIP):
    print("-" * 60)
    print("Por favor, espere, escaneando o host remoto", remoteServerIP)
    print("-" * 60)
    
    start_time = datetime.now()

    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print(f"Porta {port}: Aberta")
            sock.close()

    except KeyboardInterrupt:
        print("\nSaindo do programa.")
        sys.exit()

    except socket.gaierror:
        print("\nHostname não pôde ser resolvido.")
        sys.exit()

    except socket.error:
        print("\nNão foi possível conectar ao servidor.")
        sys.exit()

    end_time = datetime.now()
    total_time = end_time - start_time
    print("\nEscaneamento completado em: ", total_time)

def main():
    clear_screen()
    remoteServer = get_target()
    remoteServerIP = socket.gethostbyname(remoteServer)
    scan_ports(remoteServerIP)

if __name__ == "__main__":
    main()
