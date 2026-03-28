from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkflowsQueue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WORKFLOWS_QUEUE_DEFAULT: _ClassVar[WorkflowsQueue]
    WORKFLOWS_QUEUE_OCR: _ClassVar[WorkflowsQueue]

class Workflow(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WORKFLOW_UNSPECIFIED: _ClassVar[Workflow]
    WORKFLOW_PROCESS_RESUME_FILE: _ClassVar[Workflow]
WORKFLOWS_QUEUE_DEFAULT: WorkflowsQueue
WORKFLOWS_QUEUE_OCR: WorkflowsQueue
WORKFLOW_UNSPECIFIED: Workflow
WORKFLOW_PROCESS_RESUME_FILE: Workflow

class WorkflowProcessResumeFileInput(_message.Message):
    __slots__ = ("resume_id", "data")
    class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILE_TYPE_UNSPECIFIED: _ClassVar[WorkflowProcessResumeFileInput.FileType]
        FILE_TYPE_PDF: _ClassVar[WorkflowProcessResumeFileInput.FileType]
        FILE_TYPE_WORD: _ClassVar[WorkflowProcessResumeFileInput.FileType]
    FILE_TYPE_UNSPECIFIED: WorkflowProcessResumeFileInput.FileType
    FILE_TYPE_PDF: WorkflowProcessResumeFileInput.FileType
    FILE_TYPE_WORD: WorkflowProcessResumeFileInput.FileType
    class FileData(_message.Message):
        __slots__ = ("name", "storage_bucket", "storage_key", "type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        STORAGE_BUCKET_FIELD_NUMBER: _ClassVar[int]
        STORAGE_KEY_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        storage_bucket: str
        storage_key: str
        type: WorkflowProcessResumeFileInput.FileType
        def __init__(self, name: _Optional[str] = ..., storage_bucket: _Optional[str] = ..., storage_key: _Optional[str] = ..., type: _Optional[_Union[WorkflowProcessResumeFileInput.FileType, str]] = ...) -> None: ...
    RESUME_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    resume_id: str
    data: WorkflowProcessResumeFileInput.FileData
    def __init__(self, resume_id: _Optional[str] = ..., data: _Optional[_Union[WorkflowProcessResumeFileInput.FileData, _Mapping]] = ...) -> None: ...

class WorkflowProcessResumeFileOutput(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
