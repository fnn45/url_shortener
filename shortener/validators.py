from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    req_val = value
    if 'http' in req_val:
        new_value = req_val
    else:
        new_value = 'http//' + req_val
    try:
        url_validator(new_value)
    except:
        raise ValidationError('invalid URL')
    return value

