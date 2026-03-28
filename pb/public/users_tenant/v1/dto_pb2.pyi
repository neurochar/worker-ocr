from common.types import types_pb2 as _types_pb2
from common.types import users_tenant_types_pb2 as _users_tenant_types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListAccountsRequest(_message.Message):
    __slots__ = ("limit", "offset")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListAccountsResponse(_message.Message):
    __slots__ = ("items", "total")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_users_tenant_types_pb2.AccountTenant]
    total: int
    def __init__(self, items: _Optional[_Iterable[_Union[_users_tenant_types_pb2.AccountTenant, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetAccountResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _users_tenant_types_pb2.AccountTenant
    def __init__(self, item: _Optional[_Union[_users_tenant_types_pb2.AccountTenant, _Mapping]] = ...) -> None: ...

class CreateAccountRequestPayload(_message.Message):
    __slots__ = ("email", "password", "role_id", "profile_name", "profile_surname", "profile_photos")
    class PhotoFiles(_message.Message):
        __slots__ = ("original_file_id", "s100x100_file_id")
        ORIGINAL_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        S100X100_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        original_file_id: str
        s100x100_file_id: str
        def __init__(self, original_file_id: _Optional[str] = ..., s100x100_file_id: _Optional[str] = ...) -> None: ...
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_SURNAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PHOTOS_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    role_id: int
    profile_name: str
    profile_surname: str
    profile_photos: CreateAccountRequestPayload.PhotoFiles
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ..., role_id: _Optional[int] = ..., profile_name: _Optional[str] = ..., profile_surname: _Optional[str] = ..., profile_photos: _Optional[_Union[CreateAccountRequestPayload.PhotoFiles, _Mapping]] = ...) -> None: ...

class CreateAccountRequest(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: CreateAccountRequestPayload
    def __init__(self, payload: _Optional[_Union[CreateAccountRequestPayload, _Mapping]] = ...) -> None: ...

class CreateAccountResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _users_tenant_types_pb2.AccountTenant
    def __init__(self, item: _Optional[_Union[_users_tenant_types_pb2.AccountTenant, _Mapping]] = ...) -> None: ...

class PatchAccountRequestPayload(_message.Message):
    __slots__ = ("is_blocked", "password", "role_id", "profile_name", "profile_surname", "profile_photos", "profile_photos_clear")
    class PhotoFiles(_message.Message):
        __slots__ = ("original_file_id", "s100x100_file_id")
        ORIGINAL_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        S100X100_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        original_file_id: str
        s100x100_file_id: str
        def __init__(self, original_file_id: _Optional[str] = ..., s100x100_file_id: _Optional[str] = ...) -> None: ...
    IS_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_SURNAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PHOTOS_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PHOTOS_CLEAR_FIELD_NUMBER: _ClassVar[int]
    is_blocked: bool
    password: str
    role_id: int
    profile_name: str
    profile_surname: str
    profile_photos: PatchAccountRequestPayload.PhotoFiles
    profile_photos_clear: bool
    def __init__(self, is_blocked: bool = ..., password: _Optional[str] = ..., role_id: _Optional[int] = ..., profile_name: _Optional[str] = ..., profile_surname: _Optional[str] = ..., profile_photos: _Optional[_Union[PatchAccountRequestPayload.PhotoFiles, _Mapping]] = ..., profile_photos_clear: bool = ...) -> None: ...

class PatchAccountRequest(_message.Message):
    __slots__ = ("id", "payload", "version", "skip_version_check")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SKIP_VERSION_CHECK_FIELD_NUMBER: _ClassVar[int]
    id: str
    payload: PatchAccountRequestPayload
    version: int
    skip_version_check: bool
    def __init__(self, id: _Optional[str] = ..., payload: _Optional[_Union[PatchAccountRequestPayload, _Mapping]] = ..., version: _Optional[int] = ..., skip_version_check: bool = ...) -> None: ...

class PatchAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateMyProfileRequestPayload(_message.Message):
    __slots__ = ("profile_name", "profile_surname", "profile_photos", "profile_photos_clear")
    class PhotoFiles(_message.Message):
        __slots__ = ("original_file_id", "s100x100_file_id")
        ORIGINAL_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        S100X100_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        original_file_id: str
        s100x100_file_id: str
        def __init__(self, original_file_id: _Optional[str] = ..., s100x100_file_id: _Optional[str] = ...) -> None: ...
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_SURNAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PHOTOS_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PHOTOS_CLEAR_FIELD_NUMBER: _ClassVar[int]
    profile_name: str
    profile_surname: str
    profile_photos: UpdateMyProfileRequestPayload.PhotoFiles
    profile_photos_clear: bool
    def __init__(self, profile_name: _Optional[str] = ..., profile_surname: _Optional[str] = ..., profile_photos: _Optional[_Union[UpdateMyProfileRequestPayload.PhotoFiles, _Mapping]] = ..., profile_photos_clear: bool = ...) -> None: ...

class UpdateMyProfileRequest(_message.Message):
    __slots__ = ("payload", "version", "skip_version_check")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SKIP_VERSION_CHECK_FIELD_NUMBER: _ClassVar[int]
    payload: UpdateMyProfileRequestPayload
    version: int
    skip_version_check: bool
    def __init__(self, payload: _Optional[_Union[UpdateMyProfileRequestPayload, _Mapping]] = ..., version: _Optional[int] = ..., skip_version_check: bool = ...) -> None: ...

class UpdateMyProfileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateMyPasswordRequestPayload(_message.Message):
    __slots__ = ("current_password", "new_password", "new_password2")
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD2_FIELD_NUMBER: _ClassVar[int]
    current_password: str
    new_password: str
    new_password2: str
    def __init__(self, current_password: _Optional[str] = ..., new_password: _Optional[str] = ..., new_password2: _Optional[str] = ...) -> None: ...

class UpdateMyPasswordRequest(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UpdateMyPasswordRequestPayload
    def __init__(self, payload: _Optional[_Union[UpdateMyPasswordRequestPayload, _Mapping]] = ...) -> None: ...

class UpdateMyPasswordResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UploadProfilePhotoFileRequest(_message.Message):
    __slots__ = ("file", "filename")
    FILE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    file: bytes
    filename: str
    def __init__(self, file: _Optional[bytes] = ..., filename: _Optional[str] = ...) -> None: ...

class UploadProfilePhotoFileResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _types_pb2.FilesMap
    def __init__(self, data: _Optional[_Union[_types_pb2.FilesMap, _Mapping]] = ...) -> None: ...
