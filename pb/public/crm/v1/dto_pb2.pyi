from common.types import types_pb2 as _types_pb2
from common.types import crm_types_pb2 as _crm_types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCandidatesRequest(_message.Message):
    __slots__ = ("limit", "offset", "search_query")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    search_query: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., search_query: _Optional[str] = ...) -> None: ...

class ListCandidatesResponse(_message.Message):
    __slots__ = ("items", "total")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_crm_types_pb2.ListCandidate]
    total: int
    def __init__(self, items: _Optional[_Iterable[_Union[_crm_types_pb2.ListCandidate, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class GetCandidateRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCandidateResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _crm_types_pb2.Candidate
    def __init__(self, item: _Optional[_Union[_crm_types_pb2.Candidate, _Mapping]] = ...) -> None: ...

class CreateCandidateRequestPayload(_message.Message):
    __slots__ = ("name", "surname", "gender", "birthday", "resume_files")
    class ResumeFiles(_message.Message):
        __slots__ = ("file_id",)
        FILE_ID_FIELD_NUMBER: _ClassVar[int]
        file_id: str
        def __init__(self, file_id: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    RESUME_FILES_FIELD_NUMBER: _ClassVar[int]
    name: str
    surname: str
    gender: _types_pb2.Gender
    birthday: _types_pb2.OptionalDate
    resume_files: CreateCandidateRequestPayload.ResumeFiles
    def __init__(self, name: _Optional[str] = ..., surname: _Optional[str] = ..., gender: _Optional[_Union[_types_pb2.Gender, str]] = ..., birthday: _Optional[_Union[_types_pb2.OptionalDate, _Mapping]] = ..., resume_files: _Optional[_Union[CreateCandidateRequestPayload.ResumeFiles, _Mapping]] = ...) -> None: ...

class CreateCandidateRequest(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: CreateCandidateRequestPayload
    def __init__(self, payload: _Optional[_Union[CreateCandidateRequestPayload, _Mapping]] = ...) -> None: ...

class CreateCandidateResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _crm_types_pb2.Candidate
    def __init__(self, item: _Optional[_Union[_crm_types_pb2.Candidate, _Mapping]] = ...) -> None: ...

class PatchCandidateRequestPayload(_message.Message):
    __slots__ = ("name", "surname", "gender", "birthday", "resume_files", "resume_files_clear")
    class ResumeFiles(_message.Message):
        __slots__ = ("file_id",)
        FILE_ID_FIELD_NUMBER: _ClassVar[int]
        file_id: str
        def __init__(self, file_id: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    RESUME_FILES_FIELD_NUMBER: _ClassVar[int]
    RESUME_FILES_CLEAR_FIELD_NUMBER: _ClassVar[int]
    name: str
    surname: str
    gender: _types_pb2.Gender
    birthday: _types_pb2.OptionalDate
    resume_files: PatchCandidateRequestPayload.ResumeFiles
    resume_files_clear: bool
    def __init__(self, name: _Optional[str] = ..., surname: _Optional[str] = ..., gender: _Optional[_Union[_types_pb2.Gender, str]] = ..., birthday: _Optional[_Union[_types_pb2.OptionalDate, _Mapping]] = ..., resume_files: _Optional[_Union[PatchCandidateRequestPayload.ResumeFiles, _Mapping]] = ..., resume_files_clear: bool = ...) -> None: ...

class PatchCandidateRequest(_message.Message):
    __slots__ = ("id", "payload", "version", "skip_version_check")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SKIP_VERSION_CHECK_FIELD_NUMBER: _ClassVar[int]
    id: str
    payload: PatchCandidateRequestPayload
    version: int
    skip_version_check: bool
    def __init__(self, id: _Optional[str] = ..., payload: _Optional[_Union[PatchCandidateRequestPayload, _Mapping]] = ..., version: _Optional[int] = ..., skip_version_check: bool = ...) -> None: ...

class PatchCandidateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCandidateRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteCandidateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UploadCandidateResumeFileRequest(_message.Message):
    __slots__ = ("file", "filename")
    FILE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    file: bytes
    filename: str
    def __init__(self, file: _Optional[bytes] = ..., filename: _Optional[str] = ...) -> None: ...

class UploadCandidateResumeFileResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _types_pb2.FilesMap
    def __init__(self, data: _Optional[_Union[_types_pb2.FilesMap, _Mapping]] = ...) -> None: ...
