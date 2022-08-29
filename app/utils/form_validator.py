import validators


def validate_not_empty(value, message):
    if not value:
        raise ValueError(message)


def validate_url(value, message):
    if not validators.url(value):
        raise ValueError(message)
