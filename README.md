## Automatização de Gerenciamento de Containers Docker com Python
Esta é uma automação de gerenciamento de containers Docker usando a linguagem de programação Python e a biblioteca Docker SDK para Python.  
Com esta automação, é possível criar, iniciar, parar e remover containers Docker com facilidade.

### Requisitos
Antes de usar esta automação, é necessário ter o Docker instalado em sua máquina. Além disso, é necessário instalar a biblioteca Docker SDK para Python. Isso pode ser feito executando o seguinte comando:  
`pip install docker`  
  
Também é necessário instalar a biblioteca click para criar a interface de linha de comando. Isso pode ser feito executando o seguinte comando:  
`pip install click`

### Como usar
Para usar esta automação, basta executar o seguinte comando na linha de comando:  
`python docker_automation.py --create --start --list`

As opções `--create`, `--start` e `--list` podem ser usadas para criar um novo container, iniciar um container existente e listar todos os containers, respectivamente.

Ao escolher a opção --create, você será solicitado a fornecer o nome do container, o nome da imagem e o comando a ser executado.  
Ao escolher a opção --start, você será solicitado a fornecer o nome do container.  
Ao escolher a opção --list, uma lista de todos os containers será exibida na tela.
