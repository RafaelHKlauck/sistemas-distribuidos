import socket

def start_server():
  host='0.0.0.0' # Listen to all interfaces
  port=6006

  # Creating socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f'Servidor ouvindo em {host}:{port}')
    conn, addr = s.accept()
    with conn:
      print(f'Conectado por {addr}')
      while True:
        try:
          data = conn.recv(1024)
          if not data:
            print("Cliente desconectado.")
            break
          conn.sendall(data)
        except ConnectionResetError:
          print("Cliente desconectado.")
          break
        except BrokenPipeError:
          print("Cliente desconectado.")
          break

if __name__ == "__main__":
  start_server()