from common.types import types_pb2 as _types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartRegistrationRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class StartRegistrationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FinishRegistrationRequestPayload(_message.Message):
    __slots__ = ("tenant_text_id", "profile_name", "profile_surname")
    TENANT_TEXT_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_SURNAME_FIELD_NUMBER: _ClassVar[int]
    tenant_text_id: str
    profile_name: str
    profile_surname: str
    def __init__(self, tenant_text_id: _Optional[str] = ..., profile_name: _Optional[str] = ..., profile_surname: _Optional[str] = ...) -> None: ...

class FinishRegistrationRequest(_message.Message):
    __slots__ = ("id", "payload")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    payload: FinishRegistrationRequestPayload
    def __init__(self, id: _Optional[str] = ..., payload: _Optional[_Union[FinishRegistrationRequestPayload, _Mapping]] = ...) -> None: ...

class FinishRegistrationResponse(_message.Message):
    __slots__ = ("id", "text_id", "url")
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    text_id: str
    url: str
    def __init__(self, id: _Optional[str] = ..., text_id: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class CheckRegistrationRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CheckRegistrationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
