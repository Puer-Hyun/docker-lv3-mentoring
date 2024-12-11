"""libs for restriction."""

from functools import wraps
from os import environ


def develop_only(func):
    """
    개발 환경에서만 실행되는 함수 데코레이터
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if environ.get("DEPLOY_PHASE", "dev") != "dev":
            return {
                "error": "This function is only available in development environment."
            }
        else:
            return func(*args, **kwargs)

    return wrapper
