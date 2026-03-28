from common.types import types_pb2 as _types_pb2
from common.types import testing_types_pb2 as _testing_types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListRoomsSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIST_ROOM_SORT_UNSPECIFIED: _ClassVar[ListRoomsSort]
    LIST_ROOM_SORT_CREATED_AT: _ClassVar[ListRoomsSort]
    LIST_ROOM_SORT_FINISHED_AT: _ClassVar[ListRoomsSort]
    LIST_ROOM_SORT_RESULT_INDEX: _ClassVar[ListRoomsSort]
LIST_ROOM_SORT_UNSPECIFIED: ListRoomsSort
LIST_ROOM_SORT_CREATED_AT: ListRoomsSort
LIST_ROOM_SORT_FINISHED_AT: ListRoomsSort
LIST_ROOM_SORT_RESULT_INDEX: ListRoomsSort

class GetPersonalityTraitsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPersonalityTraitsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_testing_types_pb2.PersonalityTrait]
    def __init__(self, items: _Optional[_Iterable[_Union[_testing_types_pb2.PersonalityTrait, _Mapping]]] = ...) -> None: ...

class ListProfilesRequest(_message.Message):
    __slots__ = ("limit", "offset", "search_query")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    search_query: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., search_query: _Optional[str] = ...) -> None: ...

class ListProfilesResponse(_message.Message):
    __slots__ = ("items", "total")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_testing_types_pb2.TestingListProfile]
    total: int
    def __init__(self, items: _Optional[_Iterable[_Union[_testing_types_pb2.TestingListProfile, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class GetProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetProfileResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _testing_types_pb2.TestingProfile
    def __init__(self, item: _Optional[_Union[_testing_types_pb2.TestingProfile, _Mapping]] = ...) -> None: ...

class CreateProfileRequestPayload(_message.Message):
    __slots__ = ("name", "description", "personality_traits")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERSONALITY_TRAITS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    personality_traits: _testing_types_pb2.ProfilePersonalityTraitsMap
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., personality_traits: _Optional[_Union[_testing_types_pb2.ProfilePersonalityTraitsMap, _Mapping]] = ...) -> None: ...

class CreateProfileRequest(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: CreateProfileRequestPayload
    def __init__(self, payload: _Optional[_Union[CreateProfileRequestPayload, _Mapping]] = ...) -> None: ...

class CreateProfileResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _testing_types_pb2.TestingProfile
    def __init__(self, item: _Optional[_Union[_testing_types_pb2.TestingProfile, _Mapping]] = ...) -> None: ...

class PatchProfileRequestPayload(_message.Message):
    __slots__ = ("name", "description", "personality_traits")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERSONALITY_TRAITS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    personality_traits: _testing_types_pb2.ProfilePersonalityTraitsMap
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., personality_traits: _Optional[_Union[_testing_types_pb2.ProfilePersonalityTraitsMap, _Mapping]] = ...) -> None: ...

class PatchProfileRequest(_message.Message):
    __slots__ = ("id", "payload", "version", "skip_version_check")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SKIP_VERSION_CHECK_FIELD_NUMBER: _ClassVar[int]
    id: str
    payload: PatchProfileRequestPayload
    version: int
    skip_version_check: bool
    def __init__(self, id: _Optional[str] = ..., payload: _Optional[_Union[PatchProfileRequestPayload, _Mapping]] = ..., version: _Optional[int] = ..., skip_version_check: bool = ...) -> None: ...

class PatchProfileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteProfileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GenerateProfileDescriptionByNameRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GenerateProfileDescriptionByNameResponse(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class GenerateProfileTraitsMapByDescriptionRequest(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GenerateProfileTraitsMapByDescriptionResponse(_message.Message):
    __slots__ = ("traits",)
    TRAITS_FIELD_NUMBER: _ClassVar[int]
    traits: _testing_types_pb2.ProfilePersonalityTraitsMap
    def __init__(self, traits: _Optional[_Union[_testing_types_pb2.ProfilePersonalityTraitsMap, _Mapping]] = ...) -> None: ...

class ListRoomsRequest(_message.Message):
    __slots__ = ("limit", "offset", "sort", "filter_candidate_id", "filter_profile_id")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    FILTER_CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    sort: ListRoomsSort
    filter_candidate_id: str
    filter_profile_id: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., sort: _Optional[_Union[ListRoomsSort, str]] = ..., filter_candidate_id: _Optional[str] = ..., filter_profile_id: _Optional[str] = ...) -> None: ...

class ListRoomsResponse(_message.Message):
    __slots__ = ("items", "total")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_testing_types_pb2.TestingListRoom]
    total: int
    def __init__(self, items: _Optional[_Iterable[_Union[_testing_types_pb2.TestingListRoom, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class GetRoomRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetRoomResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _testing_types_pb2.TestingRoom
    def __init__(self, item: _Optional[_Union[_testing_types_pb2.TestingRoom, _Mapping]] = ...) -> None: ...

class CreateRoomRequestPayload(_message.Message):
    __slots__ = ("candidate_id", "profile_id")
    CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    candidate_id: str
    profile_id: str
    def __init__(self, candidate_id: _Optional[str] = ..., profile_id: _Optional[str] = ...) -> None: ...

class CreateRoomRequest(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: CreateRoomRequestPayload
    def __init__(self, payload: _Optional[_Union[CreateRoomRequestPayload, _Mapping]] = ...) -> None: ...

class CreateRoomResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _testing_types_pb2.TestingRoom
    def __init__(self, item: _Optional[_Union[_testing_types_pb2.TestingRoom, _Mapping]] = ...) -> None: ...

class DeleteRoomRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteRoomResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProcessRoomRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ProcessRoomResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
