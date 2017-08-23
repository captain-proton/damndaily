import random
import string

from .models import DamnDaily


def create_damndaily_id(self, length=6):
        choices = ''.join((string.ascii_letters,
                           string.ascii_lowercase,
                           string.ascii_uppercase))
        _id = None
        daily = 1

        while daily is not None:
            _id = ''.join([random.choice(choices) for _ in range(length)])
            daily = DamnDaily.objects.filter(external_id=_id)

        return _id
