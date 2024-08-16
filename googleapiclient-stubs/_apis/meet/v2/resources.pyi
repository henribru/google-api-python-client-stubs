import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class MeetResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ConferenceRecordsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ParticipantsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ParticipantSessionsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ParticipantSessionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListParticipantSessionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListParticipantSessionsResponseHttpRequest,
                    previous_response: ListParticipantSessionsResponse,
                ) -> ListParticipantSessionsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ParticipantHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListParticipantsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListParticipantsResponseHttpRequest,
                previous_response: ListParticipantsResponse,
            ) -> ListParticipantsResponseHttpRequest | None: ...
            def participantSessions(self) -> ParticipantSessionsResource: ...

        @typing.type_check_only
        class RecordingsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> RecordingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListRecordingsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListRecordingsResponseHttpRequest,
                previous_response: ListRecordingsResponse,
            ) -> ListRecordingsResponseHttpRequest | None: ...

        @typing.type_check_only
        class TranscriptsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EntriesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TranscriptEntryHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListTranscriptEntriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTranscriptEntriesResponseHttpRequest,
                    previous_response: ListTranscriptEntriesResponse,
                ) -> ListTranscriptEntriesResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> TranscriptHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListTranscriptsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTranscriptsResponseHttpRequest,
                previous_response: ListTranscriptsResponse,
            ) -> ListTranscriptsResponseHttpRequest | None: ...
            def entries(self) -> EntriesResource: ...

        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> ConferenceRecordHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListConferenceRecordsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListConferenceRecordsResponseHttpRequest,
            previous_response: ListConferenceRecordsResponse,
        ) -> ListConferenceRecordsResponseHttpRequest | None: ...
        def participants(self) -> ParticipantsResource: ...
        def recordings(self) -> RecordingsResource: ...
        def transcripts(self) -> TranscriptsResource: ...

    @typing.type_check_only
    class SpacesResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Space = ..., **kwargs: typing.Any
        ) -> SpaceHttpRequest: ...
        def endActiveConference(
            self,
            *,
            name: str,
            body: EndActiveConferenceRequest = ...,
            **kwargs: typing.Any,
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> SpaceHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Space = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> SpaceHttpRequest: ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def conferenceRecords(self) -> ConferenceRecordsResource: ...
    def spaces(self) -> SpacesResource: ...

@typing.type_check_only
class ConferenceRecordHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ConferenceRecord: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListConferenceRecordsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConferenceRecordsResponse: ...

@typing.type_check_only
class ListParticipantSessionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListParticipantSessionsResponse: ...

@typing.type_check_only
class ListParticipantsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListParticipantsResponse: ...

@typing.type_check_only
class ListRecordingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRecordingsResponse: ...

@typing.type_check_only
class ListTranscriptEntriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTranscriptEntriesResponse: ...

@typing.type_check_only
class ListTranscriptsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTranscriptsResponse: ...

@typing.type_check_only
class ParticipantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Participant: ...

@typing.type_check_only
class ParticipantSessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ParticipantSession: ...

@typing.type_check_only
class RecordingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Recording: ...

@typing.type_check_only
class SpaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Space: ...

@typing.type_check_only
class TranscriptHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Transcript: ...

@typing.type_check_only
class TranscriptEntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TranscriptEntry: ...
