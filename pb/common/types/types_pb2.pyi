from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Gender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENDER_UNSPECIFIED: _ClassVar[Gender]
    GENDER_MALE: _ClassVar[Gender]
    GENDER_FEMALE: _ClassVar[Gender]
GENDER_UNSPECIFIED: Gender
GENDER_MALE: Gender
GENDER_FEMALE: Gender

class File(_message.Message):
    __slots__ = ("url", "id", "filename")
    URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    url: str
    id: str
    filename: str
    def __init__(self, url: _Optional[str] = ..., id: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class FilesMap(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: File
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[File, _Mapping]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.MessageMap[str, File]
    def __init__(self, map: _Optional[_Mapping[str, File]] = ...) -> None: ...

class OptionalDate(_message.Message):
    __slots__ = ("date",)
    DATE_FIELD_NUMBER: _ClassVar[int]
    date: _date_pb2.Date
    def __init__(self, date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...
