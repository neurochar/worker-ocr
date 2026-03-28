from common.types import types_pb2 as _types_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Candidate(_message.Message):
    __slots__ = ("id", "version", "tenant_id", "name", "surname", "gender", "birthday", "resume_file")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    RESUME_FILE_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    tenant_id: str
    name: str
    surname: str
    gender: _types_pb2.Gender
    birthday: _date_pb2.Date
    resume_file: _types_pb2.File
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., tenant_id: _Optional[str] = ..., name: _Optional[str] = ..., surname: _Optional[str] = ..., gender: _Optional[_Union[_types_pb2.Gender, str]] = ..., birthday: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., resume_file: _Optional[_Union[_types_pb2.File, _Mapping]] = ...) -> None: ...

class ListCandidate(_message.Message):
    __slots__ = ("id", "version", "tenant_id", "name", "surname", "gender", "birthday")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    tenant_id: str
    name: str
    surname: str
    gender: _types_pb2.Gender
    birthday: _date_pb2.Date
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., tenant_id: _Optional[str] = ..., name: _Optional[str] = ..., surname: _Optional[str] = ..., gender: _Optional[_Union[_types_pb2.Gender, str]] = ..., birthday: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...
