## Descripción

El objetivo de este repositorio es de forma sencilla realizar uso de API de google para poblar un sheet, este sera llenado con datos obtenidos desde una pagina web.


## Crear enviroment

``` bash
#Crear enviroment
$ python3 -m venv env

#Activar enviroment
$ . env/bin/activate
```


## Instalar dependencias

Instalación manual con la ayudad de `pip install`, instalar:
- requests
- google-auth 
- google-auth-oauthlib 
- google-auth-httplib2 
- google-api-python-client

Otra opcion es instalar dependencias desde requirements.txt incluido en el projecto:

```bash
pip install -r requirements.txt
```

## Nota
Es necesario obtener keys.json desde cuenta google, revisar star_api_gdocs.ipynb