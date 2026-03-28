from common.types import types_pb2 as _types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountTenant(_message.Message):
    __slots__ = ("id", "version", "tenant_id", "role_id", "email", "is_confirmed", "is_email_verified", "is_blocked", "profile_name", "profile_surname", "profile_photos", "last_login_at", "last_request_at")
    class PhotoFiles(_message.Message):
        __slots__ = ("original_file", "s100x100_file")
        ORIGINAL_FILE_FIELD_NUMBER: _ClassVar[int]
        S100X100_FILE_FIELD_NUMBER: _ClassVar[int]
        original_file: _types_pb2.File
        s100x100_file: _types_pb2.File
        def __init__(self, original_file: _Optional[_Union[_types_pb2.File, _Mapping]] = ..., s100x100_file: _Optional[_Union[_types_pb2.File, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    IS_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    IS_EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_SURNAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PHOTOS_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    tenant_id: str
    role_id: int
    email: str
    is_confirmed: bool
    is_email_verified: bool
    is_blocked: bool
    profile_name: str
    profile_surname: str
    profile_photos: AccountTenant.PhotoFiles
    last_login_at: _timestamp_pb2.Timestamp
    last_request_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., tenant_id: _Optional[str] = ..., role_id: _Optional[int] = ..., email: _Optional[str] = ..., is_confirmed: bool = ..., is_email_verified: bool = ..., is_blocked: bool = ..., profile_name: _Optional[str] = ..., profile_surname: _Optional[str] = ..., profile_photos: _Optional[_Union[AccountTenant.PhotoFiles, _Mapping]] = ..., last_login_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_request_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
