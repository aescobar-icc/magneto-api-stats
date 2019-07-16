# magneto-api-stats

Acceso a las estadísticas de las verificaciones de ADN Mutante hechas por magneto-api. 

Esta solución implementa un micro servicio para un Docker Container.

# Instalacion Local
### 1.- Instalar `Docker` .

**Instalación OSX**

        brew cask install docker
Luego corre **Docker.app** . Click next. Te pedirá permisos de acceso que debes confirmar. Te aparecerá el icono de una ballena en la barra de tareas has click en él y espera a que aparezca **"Docker is running"**.   

**Instalación Ubuntu**

        sudo apt install docker.io
        sudo systemctl start docker


### 2.- Obtén  el proyecto

        https://github.com/aescobar-icc/magneto-api-stats.git

### 4.- Configurar conexión a Base
Por simplicidad la uri de conexión a la base se debe especificar en el archivo `Dockerfile`

		ENV SQLALCHEMY_URI=mysql+pymysql://admin:admin@123.123.123.123:3306/magneto
Para este ejemplo de conexión, estoy asumiendo que el servidor MySql es local y para poder accederlo desde el contenedor se debe anexar un alias de IP a la interfaz de red, para ello en la máquina host debes correr el siguiente comando:

		sudo ifconfig lo0 alias 123.123.123.123/24
En caso de que estés accediendo a un servidor con IP pública el paso anterior no es necesario.

### 5.- Crea una imagen docker a partir del proyecto

        $ cd magneto-api-stats
        $ sudo docker build -t magneto-api-stats:v1 .
        
 Verificar si la imagen se creó correctamente.

	$ sudo docker images
	REPOSITORY        TAG IMAGE ID     CREATED   SIZE 
	magneto-api-stats v1  349e5abc9fec 5sec ago  343MB
### 6.- Correr la Api 
Ahora que ya tienes la imagen creada puedes correr el micro servicio.

        $ sudo docker run -it -p 5060:5000 magneto-api-stats:v1

Aquí se está especificando que en el `host` la API será visible en el puerto 5060 y que en el `contenedor` corre en el puerto 5000.

### 7.- Probar API usando postman

Nuestra imagen se ha publicado en http://localhost:5060/stats podemos testear fácilmente nuestra API usando `postman`.


![enter image description here](https://raw.githubusercontent.com/aescobar-icc/magneto-api-stats/master/img/postman-stats.png)


### 8.- Instalacion GCloud

Para una completa guía de como instalar esta API en la nube de google sigue esta tutorial:

[https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app](https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app)
