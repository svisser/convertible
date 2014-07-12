import jsonpickle
import os

class Struct(object):
    def __init__(self, adict):
        self.__dict__.update(adict)
        for k, v in adict.items():
            if isinstance(v, dict):
                self.__dict__[k] = Struct(v)

def to_object(structure):
    if isinstance(structure, list):
        return [to_object(item) for item in structure]
    return Struct(structure)

def limit(dictionary, keys):
    filtered = [key for key in dictionary.keys() if key not in keys]
    for key in filtered:
        dictionary.pop(key, None)

def to_dict(value):
    if isinstance(value, list):
        return [to_dict(item) for item in value]
    if isinstance(value, dict):
        cloned = value.copy()
        for key, value in cloned.items():
            cloned[key] = to_dict(value)
        return cloned
    if value is None or isinstance(value, (bool, basestring, str, unicode, int, long, float)):
        return value
    result = value.__dict__.copy()
    if hasattr(value, '__public__'):
        limit(result, value.__public__)
    for member, mvalue in result.items():
        result[member] = to_dict(mvalue)
    return result

def from_json(json_text):
    return to_object(jsonpickle.decode(json_text))

def to_json(value):
    return jsonpickle.encode(value, unpicklable=False)

def reformat(json_text):
    return to_json(from_json(json_text))

def read_json(filename):
    if not os.path.isfile(filename):
        return None
    json = open(filename, 'r').read()
    if json.strip(' \t\n\r') == '':
        return None
    return from_json(json)

def write_json(filename, obj):
    if not obj:
        json = ''
    else:
        json = to_json(obj)
    with open(filename, 'w') as file:
        file.write(json)