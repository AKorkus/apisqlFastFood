import json

def read_json(filename):
    with open(filename, "r") as f:
        result = json.load(f)
    return result

def quot(arg):
    """
    Adds quotation marks for string arguments.
    >>>print(quot(1))
    1
    >>>print(quot("arg"))
    'arg'
    """
    if type(arg) == str:
        return f"'{arg}'"
    return arg

def tuple_to_json(header, body):
    dikt = {}
    for i in range(len(header)):
        dikt[header[i]] = body[i]
    return dikt

def tuple_list_to_json_list(header, touple_list):
    json_list = []
    for touple in touple_list:
        json_list.append(tuple_to_json(header, touple))
    return json_list