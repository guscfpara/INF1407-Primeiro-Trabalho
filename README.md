# Primeiro Trabalho de Programação para Web de 2021/2
## Servidor Web

O que foi implementado :

- Implemente o método GET.
- Permita a conexão de mais de um cliente simultaneamente. Como sugestão, inclua dentro do servidor um delay para testar conexões simultâneas (eu vou fazer isso para testar o seu trabalho).
- Emita mensagens de erro ao tentar executar o seu trabalho e houver alguma inconsistência no arquivo de configuração (ver descrição de arquivo de configuração abaixo).
- Comente, no arquivo de configuração exemplo, como configurar o seu trabalho. Inclua algumas sugestões nos comentários.
- O seu servidor deverá servir arquivos HTML, JS, JPEG (JPG), PNG e GIF.
- No caso de recurso inexistente (página não encontrada), exibir código de erro 404

## Testes

Para executar os testes é preciso configurar o arquivo [configs.py]
### Configs
```sh
web_server_config = {
    # Lista de arquivos default
    "defaults_files" : ["dog.gif","golden.jpg","index.html","javascript.js","labrador.png"],
    # Porta que será escutada
    "port" : 8080,
    # Diretório Local
    "local_dir" : "views",
    # Página de Erro
    "error_file" : "404.html",
    # Char codification
    "code" : "iso-8859-1"
}
```
### GET localhost:8080/index
```sh
GET /index HTTP/1.1
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 2e139804-256e-417c-bbad-c5aeb4b6a585
Host: 0.0.0.0:8080
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

HTTP/1.1 200 OK
Server: Windows-10-10.0.19041-SP0
Content-Type: text/html
Content-Length: 43
Date : Sat, 11 Sep 2021 01:57:41 PM Hora oficial do Brasil
Connection: close
Body :  b'<html>\r\n\t<body>Hello there!</body>\r\n</html>'
```

### GET localhost:8080/dog
```sh
GET /dog HTTP/1.1
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 9a24601c-6cc1-4955-9490-c806d6da21be
Host: 0.0.0.0:8080
Accept-Encoding: gzip, deflate, br
Connection: keep-alive


HTTP/1.1 200 OK
Server: Windows-10-10.0.19041-SP0
Content-Type: image/gif
Content-Length: 194945
Date : Sat, 11 Sep 2021 02:09:53 PM Hora oficial do Brasil
Connection: close
Body :  b'GIF
```

## Rodando o Código

```sh
python .\web_server.py
```

## Comentários

O código foi desenvolvido de uma forma aonde o servidor fica rodando em um ```while True ```, esperando a conexão de algum cliente, quando é feita essa conexão roda uma função capaz de fazer toda a lógica capaz de puxar o arquivo dentro do diretório padrão.

## Author

Gustavo Paraguassu - 1520172

**Think!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [configs.py]: <https://github.com/guscfpara/INF1407-Primeiro-Trabalho/blob/main/configs.py>
