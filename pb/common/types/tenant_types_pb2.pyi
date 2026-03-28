from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Tenant(_message.Message):
    __slots__ = ("id", "version", "text_id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TEXT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    text_id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., text_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
