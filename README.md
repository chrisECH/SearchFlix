# SEARCHFLIX 

_Aplicación web desarrollado en Flask, elaborada con propositos de estudio. Permite a un usuario realizar busqueda de películas y shows de TV. Los usuarios pueden buscar películas, así como consultar recomendaciones de otros usuarios. También pueden consultar las busquedas que se han realizado._

### Pre-requisitos 📋

_El programa cuenta con una base de datos (searchflix.sql), la cuál sirve para poder visualizar los películas recomendadas y las busqudas recientes_

```
Insertar el archivo searchflix.sql en phpmyadmin, así como activar los servicios de Apache y MySQL en WAMPP, XAMPP ó LAMPP, dependiendo de cual se tenga instalado
```

### Instalación 🔧

_Para el correcto funcionamiento de este programa es necesario instalar algunas librerias:_

_Primeramente debemos clonar el proyecto con el comando:_

```
git clone 
```

_Para instalar las librerias ejecutamos los siquientes comandos:_

_Para instalar el framework **Flask**:_

```
pip install flask
```

_Se utilizo la api de **IMDBpy**, para instalarla ejecutamos el comando:_

```
pip install imdbpy
```

_Para la conexión de la base de datos con nuestra aplicación web utilizamos la libreria **flask_mysqldb**, ejecutamos el comando:

```
pip install flask_mysqldb
```

_Finalmente, utilizamos el comando_
```
pip install tmdbsimple
```

_Son todas las librerias que se utilizaron_


## Funcionamiento ⚙️
**Busqueda de películas**
_Un usuario puede imgresar el nombre de alguna película en el input de la pantalla principal, se le mostrara una lista con las peliculas que tengan ese nombre o alguno similar, el usuario puede dar clic sobre alguna de esa lista y se le mostrará la información de esta, tal como el titulo, una descripción, el año en que salio, directores, escritores, el raking que tuve, etc. De este punto partimos para el siguiente_

**Busquedas recientes**
_Cuando un usuario da clic para acceder a la información de una película, automaticamente se registra esa película en un tabla de la BD. En la pantalla principal, en la parta superior izquierda hay un menu con varias opciones, entre ellas **Busquedas recientes** al hacer clic sobre ella, se podrá observar todas aquellas películas que los uuarios dieron clic para ver si información_

**Recomendación de películas**
_Partiendo del puneto donde el usuario accede a ver la información de una película, en esa misma ventana en la parte inferior se encuentra un botón que dice **Recomendar película**, los usuarios pueden hacer clic sobre el para añadir esa película a la BD, y que algun otro usuario pueda ver las películas que otros usuarios encuentren interesantes._

**Top 250 de películas y shows de TV**
_Como parte de los servicios que nos ofrece la API de **IMDBpy** estan la posibilidad de ver el top 250 de las películas y shows de TV, tiene el mismo funcionamiento que los puntos anteriores_


## Construido con 🛠️

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - El framework web usado
* [XAMPP](https://www.apachefriends.org/es/index.html)
* [Bootstrap V 4.6.x](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Usado generar las vistas



