from data import kit_body
import configuration
import requests
import data


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH)

response = get_users_table()
print(response.status_code)

def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # coloca URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_client_kit(data.user_body)
print(response.status_code)
print(response.json())



def get_kit_body():
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=data.headers)
response = get_kit_body()
print(response.status_code)
print(response.json())

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body, # Datos que envía la solicitud
                         headers=data.headers)

response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())
