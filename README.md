# SWAPI GraphQL Prueba tecnica

# Descripcion

Aplicacion escrita en python y framework Django para consulta de todo lo relacionado con los personajes, planetas y peliculas del universo de start wars.

# Utilidades

* Permite crear querys para listar personajes
* Realizar mutaciones para crear personajes, planetas, peliculas.

# Instalacion

* git clone https://github.com/afgaleano91/GraphQLStartwars.git
* cd GraphQLStartwars
* source VEntorno-env/bin/activate
* cd startWarsAPI
* python manage.py runserver

# URL

la direccion es: http://127.0.0.1:8000/graphql/

Datos de acceso:

* user: test
* password: test

# Carga de informacion por fixtures

* python manage.py loaddata [ fixture.json ]