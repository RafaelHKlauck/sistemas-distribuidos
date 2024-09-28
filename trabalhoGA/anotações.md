# RabittMQ

- sistemas mais consolidados e usados para trabalhar com comunição assincrona entre sistemas. Ou seja, não temos o resultado na hora.
- Ele é um intermediário entre os sistemas, ou seja, recebe a mensagem de um sistema e envia para outro sistema.
- Ele é um mensage Broker, ou seja, ele é um intermediário entre os sistemas.
- Ele funciona com o protocolo AMQP (Advanced Message Queuing Protocol).

## História
- Criado em 2006 pela empresa LShift
- O projeto foi criado com o objetivo de fornecer uma solução de mensageria confiável, escalável e orientada a mensagens, facilitando a comunicação entre sistemas distribuídos
- O uso do AMQP foi uma resposta à crescente demanda por interoperabilidade entre diferentes componentes de software.
- Atualmente ele pertence a VMware.
- A popularidade do RabbitMQ cresceu rapidamente, especialmente em arquiteturas de microsserviços e na nuvem, onde a comunicação assíncrona e a desacoplagem entre componentes são essenciais. Sua flexibilidade, facilidade de configuração e suporte para diversos protocolos além do AMQP, como STOMP, MQTT e HTTP, ajudaram a consolidar sua posição como uma das principais opções de filas de mensagens.

## Quando usar?

O caso de uso do RabbitMQ é quando temos um sistema que precisa enviar uma mensagem para outro sistema, mas não precisa(ou não pode) esperar a resposta. Ou seja, o sistema envia a mensagem e segue com a execução, sem esperar a resposta.

## Tipos de Exchanges

Uma exchange é um componente do RabbitMQ que recebe mensagens de produtores e as envia para filas. As exchanges podem ser de vários tipos:

### Direct:

Exemplo: vamos dizer que temos um producer que envia uma mensagem para três Consumers:

Cada consumer tem uma fila diferente. Isso acontece porque após um consumer ler a mensagem, ela é removida da fila. Então se dois consumers estão lendo a mesma fila, um deles não vai conseguir ler a mensagem.

A exchange Direct é usada para enviar mensagens para uma fila específica. Ou seja, o producer envia a mensagem para a exchange e a exchange envia para a fila específica. Não necessariamente a mensagem vai para todas as filas.

Para criar uma relação entre a exchange e fila é necessário criar um Bind, que é uma relação entre a exchange e a fila. Esse Bind é feito através de uma chave, chamada de routing key. Então toda vez que uma mensagem é enviada para a exchange, ela é enviada para a fila que tem a mesma routing key.

### Fanout:

Fanout é um tipo de exchange que envia a mensagem para todas as filas que estão conectadas a ela. Ou seja, se um producer envia uma mensagem para a exchange, a exchange envia a mensagem para todas as filas que estão conectadas a ela. Independente da routing key.

### Topic:

A topic exchange ela é flexível, porque ela envia a mensagem para todas as filas que tem um mesmo padrão de routing key, ou invés de uma routing key específica. Por exemplo, se uma routing key é `*.orange.*`, todas as filas que tem uma routing key que tem a palavra orange no meio, vão receber a mensagem.

## Protocolo AMQP

- Protocolo de comunicação em rede que permite que sistemas se comuniquem.
- Ele atua na camada de aplicação do modelo OSI. Ele utiliza como protocolo de transporte o TCP.
- Antes de sua existência, cada sistema tinha seu próprio protocolo de comunicação, o que dificultava a comunicação entre sistemas diferentes.
- Protocolo com muitas vantagens, como por exemplo:
  - Confiabilidade
  - Padrão aberto para protocolo de mensagens
  - permitir interoperabilidade entre sistemas (sistemas diferentes podem se comunicar)

### Modelo por trás do AMQP

Ele funciona assim: producers enviam mensagens para as exchanges, que por sua vez distribuem cópias dessas mensagens para as filas, utilizando regras de bindings.
Então os consumers acessam(ou assinam) as filas para receber as mensagens.

Quando uma mensagem é publicada por um producer, ela pode incluir alguns atributos, chamados de metadados da mensagem. Alguns desses atributos podem ser utilizados pelo próprio broker e outros podem ser utilizados pelos consumers.

## Por que usar?

- **Escalabilidade**: podemos adicionar mais consumers para uma fila, sem precisar alterar o producer
- **Tolerância a falhas**: Se um consumer falhar, a mensagem não é perdida, ela fica na fila até que um consumer consiga ler
- **Garantia de entrega**: Se um consumer falhar, a mensagem não é perdida, ela fica na fila até que um consumer consiga ler
- **Garantia de ordem**: Se precisamos garantir que as mensagens sejam lidas na ordem que foram enviadas, podemos usar uma fila única
- **Mensagens temporárias**: Se precisamos enviar uma mensagem para um sistema que está offline, podemos enviar a mensagem para uma fila e o sistema lê quando estiver online

## Concorrentes

Apache Kafka, Redis Pub/Sub, AWS SQS, IBM MQ, Azure MQ

## Referências

- https://www.rabbitmq.com/
- https://medium.com/@ramonpaolo/o-que-%C3%A9-o-rabbitmq-e-como-utilizar-c3ce2406a983
- https://fullcycle.com.br/como-funciona-o-rabbitmq/
- https://www.cloudamqp.com/blog/part1-rabbitmq-best-practice.html
- https://www.devmedia.com.br/introducao-ao-amqp-com-rabbitmq/33036
