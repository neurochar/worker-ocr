from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AccessClaims(_message.Message):
    __slots__ = ("account_id", "session_id", "tenant_id", "role_id", "meta")
    class MetaEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    session_id: str
    tenant_id: str
    role_id: int
    meta: _containers.ScalarMap[str, str]
    def __init__(self, account_id: _Optional[str] = ..., session_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., role_id: _Optional[int] = ..., meta: _Optional[_Mapping[str, str]] = ...) -> None: ...
