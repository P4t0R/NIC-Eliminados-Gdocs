import os
import requests
from gdocs_utils import * 



#Link descarga datos - txt ultima semana nic.cl
url= 'https://www.nic.cl/registry/Eliminados.do?t=1s&f=txt'

#Realizar la solicitud GET a la página
response = requests.get(url)

#Ordena dominios
domains = str(response.content).split('\\')
sorted_domains = sorted(set(domains), key=len)


#Creamos un dict que contendra la lista de dominios
final = {}
for domain in sorted_domains:
    if ".cl" in domain:
        domain = domain.replace(".cl","")
        len_domain = len(domain)
        if len_domain in final:
            final[len_domain].append(domain)
        else:
            final[len_domain] = [domain]

write_dict(final)

