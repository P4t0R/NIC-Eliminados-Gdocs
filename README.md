## Descripción

El objetivo de este repositorio es hacer uso de API de Google para poblar un sheet, este será llenado con datos obtenidos desde una página web.

En concreto, se poblará con la lista de los últimos dominios eliminados, por lo tanto disponibles para ser inscritos.

<img alt="Build Status" src="https://raw.githubusercontent.com/P4t0R/NIC-Eliminados-Gdocs/main/img/demo1.png">

En la imagen anterior se muestra el resultado de la ejecución donde aparece la lista de dominios disponibles separados por el largo del nombre.


## Crear enviroment

``` bash
#Crear enviroment
$ python3 -m venv env

#Activar enviroment
$ . env/bin/activate
```


## Instalar dependencias

Instalación manual con la ayuda de `pip install`, instalar las siguientes dependencias:
- requests
- google-auth 
- google-auth-oauthlib 
- google-auth-httplib2 
- google-api-python-client

Otra opción es instalar dependencias desde requirements.txt incluido en el projecto:

```bash
pip install -r requirements.txt
```

## Nota
Es necesario obtener keys.json desde cuenta google, revisar star_api_gdocs.ipynb

- [star_api_gdocs](https://github.com/P4t0R/NIC-Eliminados-Gdocs/blob/main/start_api_gdocs.ipynb)