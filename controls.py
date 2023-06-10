global control_reference
control_reference = {}


# funcion para añadir controladores
def add_control_reference(key, value):
    global control_reference
    try:
        control_reference[key] = value
    except KeyError as e:
        print(e)
    finally:
        pass


# funcion que retorna el diccionario de controladores
def return_control_reference():
    global control_reference
    return control_reference
