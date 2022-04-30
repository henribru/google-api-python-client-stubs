import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class GamesManagementResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AchievementsResource(googleapiclient.discovery.Resource):
        def reset(
            self, *, achievementId: str, **kwargs: typing.Any
        ) -> AchievementResetResponseHttpRequest: ...
        def resetAll(
            self, **kwargs: typing.Any
        ) -> AchievementResetAllResponseHttpRequest: ...
        def resetAllForAllPlayers(
            self, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def resetForAllPlayers(
            self, *, achievementId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def resetMultipleForAllPlayers(
            self,
            *,
            body: AchievementResetMultipleForAllRequest = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class ApplicationsResource(googleapiclient.discovery.Resource):
        def listHidden(
            self,
            *,
            applicationId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> HiddenPlayerListHttpRequest: ...
        def listHidden_next(
            self,
            previous_request: HiddenPlayerListHttpRequest,
            previous_response: HiddenPlayerList,
        ) -> HiddenPlayerListHttpRequest | None: ...

    @typing.type_check_only
    class EventsResource(googleapiclient.discovery.Resource):
        def reset(
            self, *, eventId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def resetAll(
            self, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def resetAllForAllPlayers(
            self, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def resetForAllPlayers(
            self, *, eventId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def resetMultipleForAllPlayers(
            self, *, body: EventsResetMultipleForAllRequest = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class PlayersResource(googleapiclient.discovery.Resource):
        def hide(
            self, *, applicationId: str, playerId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def unhide(
            self, *, applicationId: str, playerId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class ScoresResource(googleapiclient.discovery.Resource):
        def reset(
            self, *, leaderboardId: str, **kwargs: typing.Any
        ) -> PlayerScoreResetResponseHttpRequest: ...
        def resetAll(
            self, **kwargs: typing.Any
        ) -> PlayerScoreResetAllResponseHttpRequest: ...
        def resetAllForAllPlayers(
            self, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def resetForAllPlayers(
            self, *, leaderboardId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def resetMultipleForAllPlayers(
            self, *, body: ScoresResetMultipleForAllRequest = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def achievements(self) -> AchievementsResource: ...
    def applications(self) -> ApplicationsResource: ...
    def events(self) -> EventsResource: ...
    def players(self) -> PlayersResource: ...
    def scores(self) -> ScoresResource: ...

@typing.type_check_only
class AchievementResetAllResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AchievementResetAllResponse: ...

@typing.type_check_only
class AchievementResetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AchievementResetResponse: ...

@typing.type_check_only
class HiddenPlayerListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HiddenPlayerList: ...

@typing.type_check_only
class PlayerScoreResetAllResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlayerScoreResetAllResponse: ...

@typing.type_check_only
class PlayerScoreResetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlayerScoreResetResponse: ...
