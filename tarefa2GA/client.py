import socket
import time
import matplotlib.pyplot as plt
 
message_sizes=[10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
times, bandwidths = [], []

address = '' # localhost or public IP
def client():
  global times, bandwidths
  # Creating socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((address, 6006))
    
    for size in message_sizes:
      message = b'x' * size
      start_time = time.time() 
      
      s.sendall(message)
      
      s.recv(size)
      end_time = time.time()
      
      elapsed_time = end_time - start_time
      bandwidth = (size * 8) / elapsed_time / 1_000_000

      # Append to lists to plot the chart
      times.append(elapsed_time)
      bandwidths.append(bandwidth)
      
      print(f'Tamanho: {size} bytes | Tempo: {elapsed_time:.6f} s | Largura de banda: {bandwidth:.2f} Mbps')
    s.close()

  # Plotting the chart
  plt.figure(figsize=(10, 5))

  # Chart of communication time
  plt.subplot(1, 2, 1)
  plt.plot(message_sizes, times, marker='o')
  plt.title('Tempo de Comunicação')
  plt.xlabel('Tamanho da Mensagem (bytes)')
  plt.ylabel('Tempo (segundos)')

  # Chart of bandwidth
  plt.subplot(1, 2, 2)
  plt.plot(message_sizes, bandwidths, marker='o', color='orange')
  plt.title('Largura de Banda')
  plt.xlabel('Tamanho da Mensagem (bytes)')
  plt.ylabel('Largura de Banda (Mbps)')

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  client()
