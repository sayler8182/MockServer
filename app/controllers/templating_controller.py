from app.adapters.environment_adapter import EnvironmentAdapter
from app.models.models.environment import Environment


def environment() -> Environment:
    return EnvironmentAdapter.get_environment()
