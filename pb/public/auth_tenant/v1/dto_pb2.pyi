from common.types import types_pb2 as _types_pb2
from common.types import tenant_types_pb2 as _tenant_types_pb2
from common.types import users_tenant_types_pb2 as _users_tenant_types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tokens(_message.Message):
    __slots__ = ("refresh_jwt", "refresh_life_sec", "access_jwt")
    REFRESH_JWT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_LIFE_SEC_FIELD_NUMBER: _ClassVar[int]
    ACCESS_JWT_FIELD_NUMBER: _ClassVar[int]
    refresh_jwt: str
    refresh_life_sec: int
    access_jwt: str
    def __init__(self, refresh_jwt: _Optional[str] = ..., refresh_life_sec: _Optional[int] = ..., access_jwt: _Optional[str] = ...) -> None: ...

class WhoIAmRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WhoIAmResponse(_message.Message):
    __slots__ = ("account", "tenant")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    account: _users_tenant_types_pb2.AccountTenant
    tenant: _tenant_types_pb2.Tenant
    def __init__(self, account: _Optional[_Union[_users_tenant_types_pb2.AccountTenant, _Mapping]] = ..., tenant: _Optional[_Union[_tenant_types_pb2.Tenant, _Mapping]] = ...) -> None: ...

class AccountVerifyEmailRequest(_message.Message):
    __slots__ = ("code_id", "code")
    CODE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code_id: str
    code: str
    def __init__(self, code_id: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class AccountVerifyEmailResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CheckAccountCodeRequest(_message.Message):
    __slots__ = ("id", "code")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    code: str
    def __init__(self, id: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class CheckAccountCodeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("email", "password", "tenant_text_id")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TENANT_TEXT_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    tenant_text_id: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ..., tenant_text_id: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("account", "tenant", "tokens")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    account: _users_tenant_types_pb2.AccountTenant
    tenant: _tenant_types_pb2.Tenant
    tokens: Tokens
    def __init__(self, account: _Optional[_Union[_users_tenant_types_pb2.AccountTenant, _Mapping]] = ..., tenant: _Optional[_Union[_tenant_types_pb2.Tenant, _Mapping]] = ..., tokens: _Optional[_Union[Tokens, _Mapping]] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefreshRequest(_message.Message):
    __slots__ = ("refresh_token",)
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ...) -> None: ...

class RefreshResponse(_message.Message):
    __slots__ = ("tokens",)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: Tokens
    def __init__(self, tokens: _Optional[_Union[Tokens, _Mapping]] = ...) -> None: ...

class RequestPasswordRecoveryRequest(_message.Message):
    __slots__ = ("email", "tenant_text_id")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TENANT_TEXT_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    tenant_text_id: str
    def __init__(self, email: _Optional[str] = ..., tenant_text_id: _Optional[str] = ...) -> None: ...

class RequestPasswordRecoveryResponse(_message.Message):
    __slots__ = ("code_id",)
    CODE_ID_FIELD_NUMBER: _ClassVar[int]
    code_id: str
    def __init__(self, code_id: _Optional[str] = ...) -> None: ...

class UpdatePasswordByCodeRequest(_message.Message):
    __slots__ = ("id", "code", "password", "password2")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD2_FIELD_NUMBER: _ClassVar[int]
    id: str
    code: str
    password: str
    password2: str
    def __init__(self, id: _Optional[str] = ..., code: _Optional[str] = ..., password: _Optional[str] = ..., password2: _Optional[str] = ...) -> None: ...

class UpdatePasswordByCodeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
