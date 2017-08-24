import random
import string

from .models import DamnDaily


def random_string(length=8, letters=True, uppercase=True, lowercase=True):
    choices = ((letters, string.ascii_letters),
               (uppercase, string.ascii_uppercase),
               (lowercase, string.ascii_lowercase))
    choices = ''.join([c[1] for c in choices if c[0]])
    return ''.join([random.choice(choices) for _ in range(length)])


def create_damndaily_id(length=6):
        _id = None
        daily = 1

        while daily is not None:
            _id = random_string(length=length)
            daily = DamnDaily.objects.filter(external_id=_id)

        return _id
