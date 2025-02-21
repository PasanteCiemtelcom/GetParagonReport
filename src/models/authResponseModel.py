from uuid import UUID
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Scope:
    id: UUID
    name: str
    display_name: str
    type: str

    def __init__(self, id: UUID, name: str, display_name: str, type: str) -> None:
        self.id = id
        self.name = name
        self.display_name = display_name
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Scope':
        assert isinstance(obj, dict)
        id = UUID(obj.get("id"))
        name = from_str(obj.get("name"))
        display_name = from_str(obj.get("display_name"))
        type = from_str(obj.get("type"))
        return Scope(id, name, display_name, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = str(self.id)
        result["name"] = from_str(self.name)
        result["display_name"] = from_str(self.display_name)
        result["type"] = from_str(self.type)
        return result


class Token:
    user_id: UUID
    user_name: str
    iat: int
    exp: int
    unique_identifier: str
    identity_provider_type: str

    def __init__(self, user_id: UUID, user_name: str, iat: int, exp: int, unique_identifier: str, identity_provider_type: str) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.iat = iat
        self.exp = exp
        self.unique_identifier = unique_identifier
        self.identity_provider_type = identity_provider_type

    @staticmethod
    def from_dict(obj: Any) -> 'Token':
        assert isinstance(obj, dict)
        user_id = UUID(obj.get("user_id"))
        user_name = from_str(obj.get("user_name"))
        iat = int(from_str(obj.get("iat")))
        exp = int(from_str(obj.get("exp")))
        unique_identifier = from_str(obj.get("unique_identifier"))
        identity_provider_type = from_str(obj.get("identity_provider_type"))
        return Token(user_id, user_name, iat, exp, unique_identifier, identity_provider_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user_id"] = str(self.user_id)
        result["user_name"] = from_str(self.user_name)
        result["iat"] = from_str(str(self.iat))
        result["exp"] = from_str(str(self.exp))
        result["unique_identifier"] = from_str(self.unique_identifier)
        result["identity_provider_type"] = from_str(self.identity_provider_type)
        return result


class AuthResponseModel:
    status: str
    user_id: UUID
    id_token: str
    token: Token
    scopes: List[Scope]
    identity_provider_type: str

    def __init__(self, status: str, user_id: UUID, id_token: str, token: Token, scopes: List[Scope], identity_provider_type: str) -> None:
        self.status = status
        self.user_id = user_id
        self.id_token = id_token
        self.token = token
        self.scopes = scopes
        self.identity_provider_type = identity_provider_type

    @staticmethod
    def from_dict(obj: Any) -> 'AuthResponseModel':
        assert isinstance(obj, dict)
        status = from_str(obj.get("status"))
        user_id = UUID(obj.get("user_id"))
        id_token = from_str(obj.get("id_token"))
        token = Token.from_dict(obj.get("token"))
        scopes = from_list(Scope.from_dict, obj.get("scopes"))
        identity_provider_type = from_str(obj.get("identity_provider_type"))
        return AuthResponseModel(status, user_id, id_token, token, scopes, identity_provider_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = from_str(self.status)
        result["user_id"] = str(self.user_id)
        result["id_token"] = from_str(self.id_token)
        result["token"] = to_class(Token, self.token)
        result["scopes"] = from_list(lambda x: to_class(Scope, x), self.scopes)
        result["identity_provider_type"] = from_str(self.identity_provider_type)
        return result


def auth_response_model_from_dict(s: Any) -> AuthResponseModel:
    return AuthResponseModel.from_dict(s)


def auth_response_model_to_dict(x: AuthResponseModel) -> Any:
    return to_class(AuthResponseModel, x)
