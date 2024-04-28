
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account


KEY = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1HsKlwaKSJz-IJBj_4BXovGGe2XPNvnc6q5xtftRFrW4'   #Nic-Dominios

creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


def read_sheet():
	# Llamada a la api - Rango a leer
	result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Hoja 1!A1:A8').execute()
	# Extraemos values del resultado
	values = result.get('values',[])
	print(values)

def write_sheet(text_list):
	# Debe ser una matriz por eso el doble [[]]
	values = [text_list]
	# Llamamos a la api
	result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
								range='A1',
								valueInputOption='USER_ENTERED',
								body={'values':values}).execute()
	print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")

def write_sheet_data(text_list):
	# Debe ser una matriz por eso el doble [[]]
	values = text_list
	# Llamamos a la api
	result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
								range='A1',
								valueInputOption='USER_ENTERED',
								body={'values':values}).execute()
	print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")


def clear_sheet():	
    # Llama a la API para limpiar la hoja
    request = sheet.values().clear(spreadsheetId=SPREADSHEET_ID, 
								   range='Hoja 1')
    response = request.execute()
    print("Hoja limpiada exitosamente.")


def prepare_dict(data):
    """
    Prepara y estructura los datos contenidos en un diccionario para su visualización como tabla.

    Parameters:
    data (dict): Un diccionario donde las claves son strings y los valores son listas de elementos.

    Returns:
    list: Una lista de listas donde cada sublista representa una fila de la tabla preparada.
          La primera fila contiene descripciones de las claves y la longitud de las listas asociadas a esas claves.
          Las sublistas se rellenan con cadenas vacías para que todas tengan la misma longitud.

    Example:
    >>> data = {'A': [1, 2, 3], 'B': [4, 5], 'C': [6, 7, 8, 9]}
    >>> prepare_dict(data)
    [['Largo A [3]', 'Largo B [2]', 'Largo C [4]'],
     [1, 4, 6],
     [2, 5, 7],
     [3, '', 8],
     ['', '', 9]]
    """
    k = [f'Largo {key} [{len(data[key])}]' for key in data.keys()]
    v = list(data.values())

    # Encontrar la longitud de la sublista más larga
    max_len = max(len(sub_list) for sub_list in v)

    # Rellenar sublistas más cortas con cadenas vacías para igualar la longitud
    data_in = [sub_list + [''] * (max_len - len(sub_list)) for sub_list in v]

    # Transponer la lista
    data_out = [[row[i] for row in data_in] for i in range(max_len)]
    data_out.insert(0, k) #Agregar lista de keys que es utilizada como titulo  

    return data_out

def write_dict(dict):
	clear_sheet()
	data = prepare_dict(dict)
	write_sheet_data(data)

