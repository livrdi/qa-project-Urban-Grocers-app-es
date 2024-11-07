# Proyecto Urban Grocers 

El proyecto qa-project-Urban-Grocers-app-es, consiste en realizar pruebas para el campo name de un kit de productos, para ello,
debemos seguir los siguientes requisitos:

1. Ejecutar la terminal "Pycharm"
2. Abrir el proyecto qa-project-Urban-Grocers-app-es.
3. En caso de que no estén creados los archivos (READ.md, data.py, configuration.py, sender_stand_request.py, gitignore, create_kit_name_kit_test.py) deberás crearlos.
4. Dentro del archivo configuration.py ingresa la URL del servidor, este debe ser actualizado cada vez que se realice una prueba.
5. En el archivo create_kit_name_kit_test.py, debes asegurarte que se encuentre seleccionado "current file".
6. No olvides descargar o actualizar los paquetes "pytest" y "requests".
7. Puedes ejecutar las pruebas con el comando "python -m pytest" en la consola o con la flecha "play" de color verde en la parte superior.

### Las pruebas a realizar de acuerdo a los requerimientos son los siguientes:


kit_body_test_1 = "A",
Resultado esperado: 201

kit_body_test_2 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
Resultado esperado: 201

kit_body_test_3 = ""
Resultado esperado: 400

kit_body_test_4= "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
Resultado esperado: 400

kit_body_test_5= "\"№%@\","
Resultado esperado: 201

kit_body_test_6 = "A Aaa"
Resultado esperado: 201

kit_body_test_7 = "123"
Resultado esperado: 201

kit_body_test_8 = { }
Resultado esperado: 400

kit_body_test_9 = 123

Resultado esperado: 400

Con esta lista, se trabajará en automatizar las pruebas para corroborar que los resultados son los esperados.
