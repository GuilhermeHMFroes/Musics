
# Aplicação Flask

## Passos para inicializar a aplicação

Vá até o arquivo ```app.py``` e altere a seguinte linha:

```app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://teste:teste@localhost/music'```

Em ```mysql+pymysql``` é o banco de dados da máquina no caso esse sistema foi desenvolvido utilizando o banco de dados mysql-server.

Em ```teste:teste@localhost``` é o usuário e a senha do um usuário do seu banco de dados.

No seu SGBD crie um novo banco de dados chamado ```music```.

Em ```/music``` é nome da tabela que você vai usar no sistema.



## Executando a aplicação

Acesse o diretório _**`modelo`**_ e execute os seguintes comandos no terminal:


```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ flask run
```

Agora basta acessar a aplicação através do navegador pelo endereço http://127.0.0.1:5000

## Banco de dados

O arquivo ```musicas.csv``` contém algumas músicas para fazer a importação no banco de dados.

## Cadastro de  músicas

O cadastro de músicas deve ser realizado da seguinte forma:

Nome da música: É um campo obrigatório onde registra o nome da música. Ex.: Dynasty

Artista: É um campo obrigatório onde registra o artista responsável pela música. Ex.: MIIA

Vídeo: É um campo obrigatório onde coloca o link de incorporação de vídeo que o youtube disponibiliza. Ex.: < iframe width="560" height="315" src="https://www.youtube.com/embed/pY8oa8XS3ko" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> (Entre o primeiro < e o iframe não deve ter o espaço, foi colocado apenas para mostrar como o código é)

Link: Campo obrigatório onde coloca o link do youtube, vai ser usado em futuras atualizações. Ex.: https://www.youtube.com/watch?v=pY8oa8XS3ko&ab_channel=CentralVibes

Grênero: Campo opicional
