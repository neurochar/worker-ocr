from common.types import types_pb2 as _types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IsExistsRequest(_message.Message):
    __slots__ = ("text_id",)
    TEXT_ID_FIELD_NUMBER: _ClassVar[int]
    text_id: str
    def __init__(self, text_id: _Optional[str] = ...) -> None: ...

class IsExistsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PatchTenantRequestPayload(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PatchTenantRequest(_message.Message):
    __slots__ = ("id", "payload", "version", "skip_version_check")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SKIP_VERSION_CHECK_FIELD_NUMBER: _ClassVar[int]
    id: str
    payload: PatchTenantRequestPayload
    version: int
    skip_version_check: bool
    def __init__(self, id: _Optional[str] = ..., payload: _Optional[_Union[PatchTenantRequestPayload, _Mapping]] = ..., version: _Optional[int] = ..., skip_version_check: bool = ...) -> None: ...

class PatchTenantResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
