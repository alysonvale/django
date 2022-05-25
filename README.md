# Django
Django é um framework web Python de alto nível que encoraja o desenvolvimento rápido e design limpo e pragmático.

## Verificar se o Django está instalado
```bash

# Verificar se tenho django e qual versão tenho.
$ python -m django --version

```


## PIP
* Sistema de gerenciamento de pacotes.
* Utilizado para instalar e gerenciar pacotes/bibliotecas em Python.
* Já vem empacotado com Python desde a versão 3.4 do Python.

```bash

$ pip install django collecting django

```

## Virtualenv
* Ferramenta para criar ambientes Python isolados.
* Vem integrado com Python desde a versão 3.3 do Python.
* Extremamente útil para se trbalhar com projetos que utilizam bibliotecas com versões diferente.

```bash

# Criando o virtualenvs
$ python -m venv .\.virtualenvs\[nome-virtualenv]

# Ativar o virtualenvs
$.\.virtuallenvs\[nome-virtualenv]\Scripts\activate

# instalar Django
$ pip install django

```

## IDE

- **[Pycharm](https://www.jetbrains.com/pt-br/pycharm/)**

## Criando um projeto Django
Para criar um projeto Django é necessário uma estrutura padrão que pode ser criada a partir:

```bash

$ django-admin startproject [nome-projeto]

```

## Criando um App com o Django
Para criar um app no Django é necessário uma estrutura padrão que pode ser criada a partir:

```bash

# Criando o projeto do App
$ django-admin startapp [nome-app]

# Entrando na pasta
$ .\[nome-projeto]\

# Olhando os arquivos
$ ls

```

## Servidor de desenvolvimento

```bash

# Verificando se o servidor funciona.
-> Vá ao diretório projeto: exemplo: [mysite]
$ python manage.py runserver

# Alterando servidor:
$ python manage.py runserver 8080

# 

```

