import json
import string
import random

from faker import Faker


def seanify(sean_formatted_json):
    factorized_json = {}

    sean_json = json.loads(sean_formatted_json)
    for key, value in sean_json.items():
        try:
            factorized_json[key] = factorize(value)
        except ValueError as e:
            raise e
    return factorized_json


def factorize(value):
    if type(value) == list:
        return _factorize_values(_val=value)
    elif type(value) == dict:
        return _factorize_values(**value)
    

def factorize_string(length, frmt):
    if not length:
        raise ValueError("Invalid length for type string")
    value = _gen_string(length)
    if frmt:
        value = frmt.format(value)
    return value


def factorize_int(length, frmt):
    if not length:
        raise ValueError("Invalid length for type int")
    value = _gen_int(length)
    if frmt:
        value = frmt.format(value)
    return value


def factorize_dict(sean_val):
    factor_dict = {}
    for key, value in sean_val.items():
        val = factorize(value)
        factor_dict[key] = val
    return factor_dict


def factorize_list(sean_val, length=0):
    factor_list = []
    for i in range(1, length+1):
        val = factorize(sean_val)
        factor_list.append(val)
    return factor_list


def _factorize_values(_type=None, _len=0, _format=None, _val=None):
    fake = Faker()

    if not _type:
        return random.choice(_val)
    elif _type == 'string':
        return factorize_string(_len, _format)
    elif _type == 'int':
        return factorize_int(_len, _format)
    elif _type == 'dict':
        return factorize_dict(_val)
    elif _type == 'list':
        return factorize_list(_val, _len)
    elif _type == 'bool':
        return fake.boolean()
    elif _type == 'text':
        return fake.text()
    elif _type == 'sentence':
        return fake.sentence()
    elif _type == 'name':
        return fake.name()
    elif _type == 'email':
        return fake.email()
    elif _type == 'timestamp':
        return int(fake.date_time_this_month().strftime("%s"))


def _gen_string(size):
    ascii_chars = string.ascii_letters + "0123456789"
    return ''.join(random.choice(ascii_chars) for i in range(size))


def _gen_int(size):
    return random.randint(10**(size-1), (10**size)-1)
