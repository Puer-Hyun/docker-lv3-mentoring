"""libs for response."""

from functools import wraps


def as_dict(func):
    """ORM 객체나 ORM 객체 리스트를 딕셔너리 형태로 변환하는 데코레이터.

    ORM 객체의 to_dict 메서드가 있다면 해당 메서드를 사용하고,
    없다면 언더스코어(_)로 시작하지 않는 속성들을 딕셔너리로 변환합니다.

    Args:
        func: 데코레이트할 함수. ORM 객체, ORM 객체 리스트 또는 None을 반환해야 함

    Returns:
        dict: 다음 형식의 딕셔너리를 반환
            - ORM 객체인 경우: {"data": {속성: 값, ...}}
            - ORM 객체 리스트인 경우: {"data": [{속성: 값, ...}, ...]}
            - None인 경우: {"data": None}

    Example:
        @as_dict
        def get_user(user_id: int) -> User:
            return User.query.get(user_id)
    """

    def serialize_orm(obj):
        if hasattr(obj, "to_dict"):
            return obj.to_dict()
        return {k: v for k, v in obj.__dict__.items() if not k.startswith("_")}

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res is None:
            return {"data": None}
        elif isinstance(res, list):
            return {"data": [serialize_orm(x) for x in res]}
        else:
            return {"data": serialize_orm(res)}

    return wrapper
