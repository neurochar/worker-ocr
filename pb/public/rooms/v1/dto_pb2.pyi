from common.types import types_pb2 as _types_pb2
from common.types import testing_types_pb2 as _testing_types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoomCandidate(_message.Message):
    __slots__ = ("candidate_name",)
    CANDIDATE_NAME_FIELD_NUMBER: _ClassVar[int]
    candidate_name: str
    def __init__(self, candidate_name: _Optional[str] = ...) -> None: ...

class RoomTechniqueItem(_message.Message):
    __slots__ = ("type", "question", "variants")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    type: _testing_types_pb2.TechniqueItemType
    question: str
    variants: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[_Union[_testing_types_pb2.TechniqueItemType, str]] = ..., question: _Optional[str] = ..., variants: _Optional[_Iterable[str]] = ...) -> None: ...

class Room(_message.Message):
    __slots__ = ("id", "status", "tenant_name", "candidate", "technique_data")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: _testing_types_pb2.RoomStatus
    tenant_name: str
    candidate: RoomCandidate
    technique_data: _containers.RepeatedCompositeFieldContainer[RoomTechniqueItem]
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[_testing_types_pb2.RoomStatus, str]] = ..., tenant_name: _Optional[str] = ..., candidate: _Optional[_Union[RoomCandidate, _Mapping]] = ..., technique_data: _Optional[_Iterable[_Union[RoomTechniqueItem, _Mapping]]] = ...) -> None: ...

class AnswerValue(_message.Message):
    __slots__ = ("string_value", "int_value", "double_value", "bool_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    int_value: int
    double_value: float
    bool_value: bool
    def __init__(self, string_value: _Optional[str] = ..., int_value: _Optional[int] = ..., double_value: _Optional[float] = ..., bool_value: bool = ...) -> None: ...

class Answers(_message.Message):
    __slots__ = ("data",)
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AnswerValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AnswerValue, _Mapping]] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.MessageMap[int, AnswerValue]
    def __init__(self, data: _Optional[_Mapping[int, AnswerValue]] = ...) -> None: ...

class GetRoomRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetRoomResponse(_message.Message):
    __slots__ = ("room",)
    ROOM_FIELD_NUMBER: _ClassVar[int]
    room: Room
    def __init__(self, room: _Optional[_Union[Room, _Mapping]] = ...) -> None: ...

class FinishRoomRequestPayload(_message.Message):
    __slots__ = ("answers",)
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    answers: Answers
    def __init__(self, answers: _Optional[_Union[Answers, _Mapping]] = ...) -> None: ...

class FinishRoomRequest(_message.Message):
    __slots__ = ("id", "payload")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    payload: FinishRoomRequestPayload
    def __init__(self, id: _Optional[str] = ..., payload: _Optional[_Union[FinishRoomRequestPayload, _Mapping]] = ...) -> None: ...

class FinishRoomResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
