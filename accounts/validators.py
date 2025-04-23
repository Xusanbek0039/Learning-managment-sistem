import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class ASCIIUsernameValidator(validators.RegexValidator):
    regex = r'^[a-zA-Z]+\/(...)\/(....)'  # Regex o'zgarmaydi
    message = _(
        'Faqat lotin harflari, sonlar va @/./+/-/_ belgilari ishlatilgan to\'g\'ri foydalanuvchi nomini kiriting.'
    )
    flags = re.ASCII