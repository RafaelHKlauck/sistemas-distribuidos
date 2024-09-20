import socket
import time
import matplotlib.pyplot as plt
 
message_sizes=[10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
times, bandwidths = [], []

address = '' # Adicionar o endereço IP do servidor
def client():
  global times, bandwidths
  
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((address, 6006))
    
    for size in message_sizes:
      message = b'x' * size
      repetitions = 10 if size < 10000 else 3 # Repetir 10 vezes para mensagens menores que 10KB, e 3 vezes para mensagens maiores
      elapsed_time_total = 0
      for _ in range(repetitions):
        start_time = time.time() 
        
        s.sendall(message)
        
        s.recv(size)
        end_time = time.time()
        elapsed_time_total += (end_time - start_time)
      
      elapsed_time = elapsed_time_total / repetitions
      band_width = (size * 8) / elapsed_time / 1_000_000

      # Adicionando valores para gráfico
      times.append(elapsed_time)
      bandwidths.append(band_width)
      
      print(f'Tamanho: {size} bytes | Tempo: {elapsed_time:.6f} s | Largura de banda: {band_width:.2f} Mbps')
    s.close()

  plt.figure(figsize=(12, 6))

  # Gráfico de Tempo de Comunicação
  plt.subplot(1, 2, 1)
  plt.plot(message_sizes, times, marker='o', color='blue', label='Tempo de Comunicação')
  plt.xscale('log') 
  plt.title('Tempo de Comunicação')
  plt.xlabel('Tamanho da Mensagem (bytes)')
  plt.ylabel('Tempo (segundos)')

  # Adicionando valores nos pontos
  for i, (size, time_val) in enumerate(zip(message_sizes, times)):
      plt.annotate(f'{time_val:.6f}', (size, time_val), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

  # Gráfico de Largura de Banda
  plt.subplot(1, 2, 2)
  plt.plot(message_sizes, bandwidths, marker='s', color='orange', label='Largura de Banda')
  plt.xscale('log') 
  plt.title('Largura de Banda')
  plt.xlabel('Tamanho da Mensagem (bytes)')
  plt.ylabel('Largura de Banda (Mbps)')

  # Adicionando valores nos pontos
  for i, (size, bw_val) in enumerate(zip(message_sizes, bandwidths)):
      plt.annotate(f'{bw_val:.2f}', (size, bw_val), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  client()
