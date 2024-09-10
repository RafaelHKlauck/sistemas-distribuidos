# Exercício 2 do GA

## Desenvolvedores

- Cícero Calsing
- Rafael Hansen Klauck

## Instruções

Desenvolva em sockets TCP um programa Ping-Pong e o teste com diferentes tamanhos de mensagens. Você deve entregar o código do programa e 2 gráficos tempo de comunicação e consumo de largura de banda. Mensagens: 10, 100, 1000, 5000, 10k, 50K, 100k, 500k, 1M. (em bytes)

## Como rodar

Para rodar o programa, basta instalar as dependências. Após isso executar os arquivos `server.py` e `client.py` em terminais diferentes, na respectiva ordem. Também é necessário configurar qual endereço e porta o servidor irá escutar e qual endereço e porta o cliente irá se conectar.

## Execução e Resultados

Nós executamos o server em uma máquina virtual da AWS e o client em uma máquina local. Então configuramos o server para escutar no IP da máquina virtual e o client para se conectar no IP da máquina virtual. A porta utilizada foi a 6006.

Os resultados obtidos foram os seguintes:
