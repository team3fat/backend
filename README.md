# Backend

***

## Introduccion

Este proyecto se basa en crear un sistema web para el campamento “El Diquecito”. Este campamento se trata de una organización sin fines de lucro.

### Proposito

La aplicación web facilitará la organización del campamento a la hora de la comunicación con el cliente, para efectuar reservas del mismo y brindar información del mismo.

### Scope

Produciremos un sistema web bajo el nombre de “Campamento Diquecito”.  Este contará con:

- Inicio de sesión del usuario para que se pueda registrar
- Toda la información necesaria para que el usuario pueda reservar las fechas.
- Reservacion de una ubicación exacta del alojamiento.
- Ubicación del campamento, para que el usuario no se extravíe.
- Información para poder contactar a los administradores del campamento.

## Comandos

Lista de comandos para poder correr el proyecto localmente

`sudo apt update`

### Instalacion de Git

Para poder tener el repositorio localmente, hay que instalar **git** primero

`sudo apt install git`

Y luego inicializamos el repositorio localmente

`git init`

Añadimos el link del proyecto remote como *origin*

`git remote add origin https://github.com/team3fat/backend.git`

Fetcheamos el proyecto remoto

`git fetch origin`

Traemos la rama *master* a nuestro repositorio local

`git pull origin master`

Y entonces, localmente tendremos *master*, la version del producto oficial que ha sido testeada
y aceptada para ser considerada valida de usar

Si se quiere tener la version *develop* no estable en el repositorio local, entonces se tiene
que correr

`git checkout develop`

### [Packet Manager] Instalacion de pip

`sudo apt install python-pip`

### [Opcional] Creacion de entornos virtuales

`sudo apt install python3-venv`

`python3 -m venv [nombre de directorio del entorno virtual]`

### Instalacion de Requerimientos

`pip install requirements.txt`

En caso de que la instalacion de los requerimientos falle debido a uno/varios paquetes no disponibles,
el siguiente comando soluciona este problema instalando cada requerimiento individualmente

`cat requirements.txt | xargs -n 1 pip install`

## Tech Stack

### Requerimientos

- **“Base”** Python == 3.6
- **“Build System”** Django == 2.2.3
- **“Package Manager”** pip == Dependiendo de la version de Python
- **“Configuration”** pipenv == Dependiendo de la version de Python
- django-cors-headers == 3.0.2
- djangorestframework == 3.10.1
- djangorestframework-jwt == 1.11.0
- PyJWT == 1.7.1
- sqlparse == 0.3.0

### Tecnologias usadas

- IDE Visual Studio Code == 1.36.1
- **“Scrum Tool”** IceScrum
- **“Operative System”** Ubuntu == 18.04

### Support

#### Github

##### Branch strategy Git-flow

2 a mas repositorios

- Master
- Develop
- Feature (per/User Story)

### Diagramas

#### UML

[uml](https://docs.google.com/drawings/d/1XqeEOYqTLx5LdtMM8u_Mby8EgA3s9WIHtVM6l_oG1R4/edit)

#### DTE (**D**iagrama de **T**ranscision de **E**stados)

[dte](https://docs.google.com/drawings/d/1BsCM58zch_OiY_SmOd51n7iqg-9ZTkE44gvu2-WZSHM/edit)
