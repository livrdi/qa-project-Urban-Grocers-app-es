import sender_stand_request
import data


def create_new_user_token_on_success():
    user_response = sender_stand_request.post_new_client_kit(data.user_body)
    return user_response.json()["authToken"]

def get_kit_body(name):
    current_body = data.kit_body()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

# prueba positiva

def positive_assert(kit_body, auth_token):
  # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
  user_response = sender_stand_request.post_new_kit(kit_body, auth_token)

  # Comprueba si el código de estado es 201
  assert user_response.status_code == 201

  # Comprueba que el campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
  assert user_response.json()["name"] == kit_body["name"]

#prueba negativa
def negative_assert(kit_body, auth_token):
  # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
  user_response = sender_stand_request.post_new_kit(kit_body, auth_token)

  # Comprueba si el código de estado es 400
  assert user_response.status_code == 400



# Prueba 1. El número permitido de caracteres (1)
def test_create_kit_1_character_in_name_get_success_response():
    auth_token = create_new_user_token_on_success()
    positive_assert(data.kit_body_test_1)

# Prueba 2. Kit creado con éxito. El número permitido de caracteres (511)
def test_create_kit_511_characters_in_name_get_success_response():
    positive_assert (data.kit_body_test_2)

# Prueba 3. Error. 	El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_characters_in_name_get_error_response():
    negative_assert (data.kit_body_test_3)

# Prueba 4. Error. 	El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_characters_in_name_get_error_response():
    negative_assert(data.kit_body_test_4)

# Prueba 5. Kit creado con éxito. Se permiten caracteres especiales
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_body_test_5)

# Prueba 6. Kit creado con éxito. Se permiten espacios
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(data.kit_body_test_6)

# Prueba 7. Kit creado con éxito. Se permiten números
def test_create_kit_has_number_in_first_name_get_success_response():
    positive_assert(data.kit_body_test_7)

# Prueba 8. Error. No contiene name en la solicitud
def test_create_kit_no_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    kit_body = data.kit_body.copy()
    # El parámetro no pasa en la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert(data.kit_body_test_8)

# Prueba 9. Error. Se ha pasado un tipo de parámetro diferente en name: número
def test_create_kit_number_type_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = data.kit_body_test_9
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)
