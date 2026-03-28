from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TechniqueItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TECHNIQUE_ITEM_TYPE_UNSPECIFIED: _ClassVar[TechniqueItemType]
    TECHNIQUE_ITEM_TYPE_QUESTION_WITH_VARIANTS_SINGLE_ANSWER: _ClassVar[TechniqueItemType]

class RoomStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROOM_STATUS_UNSPECIFIED: _ClassVar[RoomStatus]
    ROOM_STATUS_NOT_STARTED: _ClassVar[RoomStatus]
    ROOM_STATUS_FINISHED: _ClassVar[RoomStatus]

class PersonalityTraitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERSONALITY_TRAIT_TYPE_UNSPECIFIED: _ClassVar[PersonalityTraitType]
    PERSONALITY_TRAIT_TYPE_BIPOLAR: _ClassVar[PersonalityTraitType]

class PersonalityTraitPriority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRESONALITY_TRAIT_PRIORITY_NONE: _ClassVar[PersonalityTraitPriority]
    PRESONALITY_TRAIT_PRIORITY_LOW: _ClassVar[PersonalityTraitPriority]
    PRESONALITY_TRAIT_PRIORITY_MEDIUM: _ClassVar[PersonalityTraitPriority]
    PRESONALITY_TRAIT_PRIORITY_HIGH: _ClassVar[PersonalityTraitPriority]

class TestingRoomResultAnalyzeHiringDecision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TESTING_ROOM_RESULT_ANALYZE_HIRING_DECISION_UNSPECIFIED: _ClassVar[TestingRoomResultAnalyzeHiringDecision]
    TESTING_ROOM_RESULT_ANALYZE_HIRING_DECISION_HIRE: _ClassVar[TestingRoomResultAnalyzeHiringDecision]
    TESTING_ROOM_RESULT_ANALYZE_HIRING_DECISION_HIRE_WITH_CONDITIONS: _ClassVar[TestingRoomResultAnalyzeHiringDecision]
    TESTING_ROOM_RESULT_ANALYZE_HIRING_DECISION_DONT_HIRE: _ClassVar[TestingRoomResultAnalyzeHiringDecision]
TECHNIQUE_ITEM_TYPE_UNSPECIFIED: TechniqueItemType
TECHNIQUE_ITEM_TYPE_QUESTION_WITH_VARIANTS_SINGLE_ANSWER: TechniqueItemType
ROOM_STATUS_UNSPECIFIED: RoomStatus
ROOM_STATUS_NOT_STARTED: RoomStatus
ROOM_STATUS_FINISHED: RoomStatus
PERSONALITY_TRAIT_TYPE_UNSPECIFIED: PersonalityTraitType
PERSONALITY_TRAIT_TYPE_BIPOLAR: PersonalityTraitType
PRESONALITY_TRAIT_PRIORITY_NONE: PersonalityTraitPriority
PRESONALITY_TRAIT_PRIORITY_LOW: PersonalityTraitPriority
PRESONALITY_TRAIT_PRIORITY_MEDIUM: PersonalityTraitPriority
PRESONALITY_TRAIT_PRIORITY_HIGH: PersonalityTraitPriority
TESTING_ROOM_RESULT_ANALYZE_HIRING_DECISION_UNSPECIFIED: TestingRoomResultAnalyzeHiringDecision
TESTING_ROOM_RESULT_ANALYZE_HIRING_DECISION_HIRE: TestingRoomResultAnalyzeHiringDecision
TESTING_ROOM_RESULT_ANALYZE_HIRING_DECISION_HIRE_WITH_CONDITIONS: TestingRoomResultAnalyzeHiringDecision
TESTING_ROOM_RESULT_ANALYZE_HIRING_DECISION_DONT_HIRE: TestingRoomResultAnalyzeHiringDecision

class PersonalityTrait(_message.Message):
    __slots__ = ("id", "type", "name", "description", "left_state_name", "right_state_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LEFT_STATE_NAME_FIELD_NUMBER: _ClassVar[int]
    RIGHT_STATE_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: PersonalityTraitType
    name: str
    description: str
    left_state_name: str
    right_state_name: str
    def __init__(self, id: _Optional[int] = ..., type: _Optional[_Union[PersonalityTraitType, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., left_state_name: _Optional[str] = ..., right_state_name: _Optional[str] = ...) -> None: ...

class ProfilePersonalityTraitsMapItem(_message.Message):
    __slots__ = ("priority", "target")
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    priority: PersonalityTraitPriority
    target: int
    def __init__(self, priority: _Optional[_Union[PersonalityTraitPriority, str]] = ..., target: _Optional[int] = ...) -> None: ...

class ProfilePersonalityTraitsMap(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ProfilePersonalityTraitsMapItem
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ProfilePersonalityTraitsMapItem, _Mapping]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.MessageMap[int, ProfilePersonalityTraitsMapItem]
    def __init__(self, map: _Optional[_Mapping[int, ProfilePersonalityTraitsMapItem]] = ...) -> None: ...

class TestingProfile(_message.Message):
    __slots__ = ("id", "version", "tenant_id", "name", "description", "personality_traits")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERSONALITY_TRAITS_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    tenant_id: str
    name: str
    description: str
    personality_traits: ProfilePersonalityTraitsMap
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., tenant_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., personality_traits: _Optional[_Union[ProfilePersonalityTraitsMap, _Mapping]] = ...) -> None: ...

class TestingListProfile(_message.Message):
    __slots__ = ("id", "version", "tenant_id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    tenant_id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., tenant_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class TestingRoomCandidate(_message.Message):
    __slots__ = ("id", "name", "surname")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    surname: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., surname: _Optional[str] = ...) -> None: ...

class TestingRoomProfile(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class TestingRoomResultTrait(_message.Message):
    __slots__ = ("match", "tip")
    MATCH_FIELD_NUMBER: _ClassVar[int]
    TIP_FIELD_NUMBER: _ClassVar[int]
    match: float
    tip: str
    def __init__(self, match: _Optional[float] = ..., tip: _Optional[str] = ...) -> None: ...

class TestingRoomResultAnalyzePersonalityFit(_message.Message):
    __slots__ = ("score", "summary", "key_matches", "key_gaps")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    KEY_MATCHES_FIELD_NUMBER: _ClassVar[int]
    KEY_GAPS_FIELD_NUMBER: _ClassVar[int]
    score: int
    summary: str
    key_matches: _containers.RepeatedScalarFieldContainer[str]
    key_gaps: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, score: _Optional[int] = ..., summary: _Optional[str] = ..., key_matches: _Optional[_Iterable[str]] = ..., key_gaps: _Optional[_Iterable[str]] = ...) -> None: ...

class TestingRoomResultAnalyze(_message.Message):
    __slots__ = ("hiring_decision", "confidence_score", "main_recomendation", "risks", "action_items", "personality_fit")
    HIRING_DECISION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    MAIN_RECOMENDATION_FIELD_NUMBER: _ClassVar[int]
    RISKS_FIELD_NUMBER: _ClassVar[int]
    ACTION_ITEMS_FIELD_NUMBER: _ClassVar[int]
    PERSONALITY_FIT_FIELD_NUMBER: _ClassVar[int]
    hiring_decision: TestingRoomResultAnalyzeHiringDecision
    confidence_score: float
    main_recomendation: str
    risks: _containers.RepeatedScalarFieldContainer[str]
    action_items: _containers.RepeatedScalarFieldContainer[str]
    personality_fit: TestingRoomResultAnalyzePersonalityFit
    def __init__(self, hiring_decision: _Optional[_Union[TestingRoomResultAnalyzeHiringDecision, str]] = ..., confidence_score: _Optional[float] = ..., main_recomendation: _Optional[str] = ..., risks: _Optional[_Iterable[str]] = ..., action_items: _Optional[_Iterable[str]] = ..., personality_fit: _Optional[_Union[TestingRoomResultAnalyzePersonalityFit, _Mapping]] = ...) -> None: ...

class TestingRoomResult(_message.Message):
    __slots__ = ("total_match", "total_match_tip", "traits", "analyze")
    class TraitsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestingRoomResultTrait
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestingRoomResultTrait, _Mapping]] = ...) -> None: ...
    TOTAL_MATCH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MATCH_TIP_FIELD_NUMBER: _ClassVar[int]
    TRAITS_FIELD_NUMBER: _ClassVar[int]
    ANALYZE_FIELD_NUMBER: _ClassVar[int]
    total_match: float
    total_match_tip: str
    traits: _containers.MessageMap[int, TestingRoomResultTrait]
    analyze: TestingRoomResultAnalyze
    def __init__(self, total_match: _Optional[float] = ..., total_match_tip: _Optional[str] = ..., traits: _Optional[_Mapping[int, TestingRoomResultTrait]] = ..., analyze: _Optional[_Union[TestingRoomResultAnalyze, _Mapping]] = ...) -> None: ...

class TestingRoom(_message.Message):
    __slots__ = ("id", "version", "tenant_id", "status", "created_at", "candidate", "profile", "result", "result_index", "finished_at", "personality_traits")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESULT_INDEX_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    PERSONALITY_TRAITS_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    tenant_id: str
    status: RoomStatus
    created_at: _timestamp_pb2.Timestamp
    candidate: TestingRoomCandidate
    profile: TestingRoomProfile
    result: TestingRoomResult
    result_index: int
    finished_at: _timestamp_pb2.Timestamp
    personality_traits: ProfilePersonalityTraitsMap
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., tenant_id: _Optional[str] = ..., status: _Optional[_Union[RoomStatus, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., candidate: _Optional[_Union[TestingRoomCandidate, _Mapping]] = ..., profile: _Optional[_Union[TestingRoomProfile, _Mapping]] = ..., result: _Optional[_Union[TestingRoomResult, _Mapping]] = ..., result_index: _Optional[int] = ..., finished_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., personality_traits: _Optional[_Union[ProfilePersonalityTraitsMap, _Mapping]] = ...) -> None: ...

class TestingListRoom(_message.Message):
    __slots__ = ("id", "version", "tenant_id", "status", "created_at", "candidate", "profile", "result_index", "hiring_decision", "finished_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    RESULT_INDEX_FIELD_NUMBER: _ClassVar[int]
    HIRING_DECISION_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    tenant_id: str
    status: RoomStatus
    created_at: _timestamp_pb2.Timestamp
    candidate: TestingRoomCandidate
    profile: TestingRoomProfile
    result_index: int
    hiring_decision: TestingRoomResultAnalyzeHiringDecision
    finished_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., tenant_id: _Optional[str] = ..., status: _Optional[_Union[RoomStatus, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., candidate: _Optional[_Union[TestingRoomCandidate, _Mapping]] = ..., profile: _Optional[_Union[TestingRoomProfile, _Mapping]] = ..., result_index: _Optional[int] = ..., hiring_decision: _Optional[_Union[TestingRoomResultAnalyzeHiringDecision, str]] = ..., finished_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
