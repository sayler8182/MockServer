from datetime import datetime

from app.models.models.environment_static_key import EnvironmentStaticKey
from app.utils.utils import save_call_with_result


def get_value_for_static(key: str) -> str:
    value = {
        EnvironmentStaticKey.date.description: __get_date
    }.get(key.upper())
    return save_call_with_result(value)


# values
def __get_date() -> str:
    date = datetime.now()
    return date.isoformat()
