import random
import string

from faker import Faker
fake = Faker()


def sean_random_choice(**kwargs):
    return random.choice(kwargs['_val'])


def sean_string(**kwargs):
    _len = kwargs.get('_len')
    _format = kwargs.get('_format', None)
    ascii_chars = string.ascii_letters + "0123456789"
    val = ''.join(random.choice(ascii_chars) for i in range(_len))
    if _format:
        val = _format.format(val)
    return val


def sean_int(**kwargs):
    _len = kwargs.get('_len')
    _format = kwargs.get('_format', None)
    val = random.randint(10**(_len-1), (10**_len)-1)
    if _format:
        val = _format.format(val)
    return val


def sean_bool(**kwargs):
    return fake.boolean()


def sean_text(**kwargs):
    return fake.text()


def sean_sentence(**kwargs):
    return fake.sentence()


def sean_name(**kwargs):
    return fake.name()


def sean_email(**kwargs):
    return fake.email()


def sean_timestamp(**kwargs):
    return int(fake.date_time_this_month().strftime("%s"))


def sean_datetime(**kwards):
    return fake.date_time_this_month().isoformat()


DEFAULT_HANDLERS = {
    None: sean_random_choice,
    'string': sean_string,
    'int': sean_int,
    'bool': sean_bool,
    'text': sean_text,
    'sentence': sean_sentence,
    'name': sean_name,
    'email': sean_email,
    'timestamp': sean_timestamp,
    'datetime': sean_datetime,
}
