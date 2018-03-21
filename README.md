# respuc-neam-flask

## Outros



## FLASK

All commands must be executed in the command line or anaconda command line (windows). All commands should be executed inside the project folder unless stated otherwise.

# Environment 

## Create 
```
conda create --name respuc_neam python=3.5.2
```
## Activate

### Linux
```
source activate enem
```

### Windows
```
activate enem
```

## Install packages (after activating the environment)

```
pip install -r requirements.txt
```

# Configuring development environment variables

## Linux

```
export FLASK_APP=run.py
export FLASK_CONFIG=development
```

## Windows

```
SET FLASK_APP=run.py
SET FLASK_CONFIG=development
```

# Run in development

```
flask run
```

# Suggested 'IDE'

[Visual studio code](https://code.visualstudio.com/)

[Sublime](https://www.sublimetext.com/3)

[Notepad ++](https://notepad-plus-plus.org/)

# Tutorial flask - windows

O primeiro passo para começar a usar o python é instalar o [anaconda](https://repo.continuum.io/archive/Anaconda3-4.4.0-Windows-x86_64.exe).

Agora você deve criar uma pasta para o projeto do tutorial (flask_tutorial) e
adicionar o arquivo requirements.txt do projeto shekel a pasta criada.

Feito isso abra o command line anaconda, va até a pasta criada com cd
e dir e crie o ambiente virtual de desenvolvimento com

```
conda create --name flask_tutorial python=3.5.2
```

e acessar o ambiente com
```
activate flask_tutorial
```

Agora basta instalar os pacotes do tutorial com 
```
pip install -r requirements.txt
``` 

e seguir os 3 tutoriais abaixo, substituindo export
por SET e podendo pular os pip install.

[Parte "0" (Começar do Say "Hello World!" with Flask)](https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework), 
[Parte 1](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one), 
[Parte 2]( https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-two)

#Redis (windows)

Redis é o nosso "mini-banco" usado para administrar as variáveis de sessão guardadas no servidor (trabalha junto com o módulo Flask-KVSession).

Além da instalação do módulo Flask-Redis (provavelmente já instalado no requirements.txt), é necessária a execução de um servidor redis.

Para o windows, faça o downlaod [aqui](https://github.com/rgl/redis/downloads).

Após a instalação, é preciso navegar até a pasta em que o programa foi instalado e rodar os arquivos "redis-service.exe" e "redis-server.exe".

Antes do flask run.
