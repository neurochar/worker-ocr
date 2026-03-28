from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientMsg(_message.Message):
    __slots__ = ("start", "chunk", "end", "ping")
    START_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    start: Start
    chunk: PdfChunk
    end: End
    ping: Ping
    def __init__(self, start: _Optional[_Union[Start, _Mapping]] = ..., chunk: _Optional[_Union[PdfChunk, _Mapping]] = ..., end: _Optional[_Union[End, _Mapping]] = ..., ping: _Optional[_Union[Ping, _Mapping]] = ...) -> None: ...

class ServerMsg(_message.Message):
    __slots__ = ("ready", "pong", "progress", "result", "error")
    READY_FIELD_NUMBER: _ClassVar[int]
    PONG_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ready: Ready
    pong: Pong
    progress: Progress
    result: Result
    error: Error
    def __init__(self, ready: _Optional[_Union[Ready, _Mapping]] = ..., pong: _Optional[_Union[Pong, _Mapping]] = ..., progress: _Optional[_Union[Progress, _Mapping]] = ..., result: _Optional[_Union[Result, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class Start(_message.Message):
    __slots__ = ("request_id", "filename", "content_type", "dpi", "device")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DPI_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    filename: str
    content_type: str
    dpi: int
    device: str
    def __init__(self, request_id: _Optional[str] = ..., filename: _Optional[str] = ..., content_type: _Optional[str] = ..., dpi: _Optional[int] = ..., device: _Optional[str] = ...) -> None: ...

class PdfChunk(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class End(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Ping(_message.Message):
    __slots__ = ("id", "ts_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    TS_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    ts_ms: int
    def __init__(self, id: _Optional[str] = ..., ts_ms: _Optional[int] = ...) -> None: ...

class Ready(_message.Message):
    __slots__ = ("request_id", "gpu", "device")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    GPU_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    gpu: bool
    device: str
    def __init__(self, request_id: _Optional[str] = ..., gpu: bool = ..., device: _Optional[str] = ...) -> None: ...

class Pong(_message.Message):
    __slots__ = ("id", "ts_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    TS_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    ts_ms: int
    def __init__(self, id: _Optional[str] = ..., ts_ms: _Optional[int] = ...) -> None: ...

class Progress(_message.Message):
    __slots__ = ("stage", "pages_done")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    PAGES_DONE_FIELD_NUMBER: _ClassVar[int]
    stage: str
    pages_done: int
    def __init__(self, stage: _Optional[str] = ..., pages_done: _Optional[int] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ("request_id", "engine", "gpu", "device", "dpi", "languages", "pages_text", "filename", "process_duration_ms")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    GPU_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    DPI_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    PAGES_TEXT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    PROCESS_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    engine: str
    gpu: bool
    device: str
    dpi: int
    languages: _containers.RepeatedScalarFieldContainer[str]
    pages_text: _containers.RepeatedScalarFieldContainer[str]
    filename: str
    process_duration_ms: int
    def __init__(self, request_id: _Optional[str] = ..., engine: _Optional[str] = ..., gpu: bool = ..., device: _Optional[str] = ..., dpi: _Optional[int] = ..., languages: _Optional[_Iterable[str]] = ..., pages_text: _Optional[_Iterable[str]] = ..., filename: _Optional[str] = ..., process_duration_ms: _Optional[int] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
