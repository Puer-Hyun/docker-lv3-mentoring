"""
애플리케이션의 제한 관련 기능을 제공하는 모듈입니다.

개발 환경과 운영 환경에서의 기능 제한을 관리합니다.
"""

from functools import wraps
from os import environ


def develop_only(func):
    """
    개발 환경에서만 실행을 허용하는 데코레이터입니다.

    Args:
        func (callable): 데코레이트할 함수

    Returns:
        callable: 래핑된 함수. 개발 환경이 아닌 경우 에러 메시지를 반환합니다.

    Example:
        @develop_only
        def debug_function():
            return "디버그 정보"
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
