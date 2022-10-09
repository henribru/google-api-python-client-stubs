import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class GamesResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AchievementDefinitionsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> AchievementDefinitionsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AchievementDefinitionsListResponseHttpRequest,
            previous_response: AchievementDefinitionsListResponse,
        ) -> AchievementDefinitionsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class AchievementsResource(googleapiclient.discovery.Resource):
        def increment(
            self,
            *,
            achievementId: str,
            stepsToIncrement: int,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> AchievementIncrementResponseHttpRequest: ...
        def list(
            self,
            *,
            playerId: str,
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            state: typing_extensions.Literal[
                "ALL", "HIDDEN", "REVEALED", "UNLOCKED"
            ] = ...,
            **kwargs: typing.Any
        ) -> PlayerAchievementListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: PlayerAchievementListResponseHttpRequest,
            previous_response: PlayerAchievementListResponse,
        ) -> PlayerAchievementListResponseHttpRequest | None: ...
        def reveal(
            self, *, achievementId: str, **kwargs: typing.Any
        ) -> AchievementRevealResponseHttpRequest: ...
        def setStepsAtLeast(
            self, *, achievementId: str, steps: int, **kwargs: typing.Any
        ) -> AchievementSetStepsAtLeastResponseHttpRequest: ...
        def unlock(
            self, *, achievementId: str, **kwargs: typing.Any
        ) -> AchievementUnlockResponseHttpRequest: ...
        def updateMultiple(
            self, *, body: AchievementUpdateMultipleRequest = ..., **kwargs: typing.Any
        ) -> AchievementUpdateMultipleResponseHttpRequest: ...

    @typing.type_check_only
    class ApplicationsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            applicationId: str,
            language: str = ...,
            platformType: typing_extensions.Literal[
                "PLATFORM_TYPE_UNSPECIFIED", "ANDROID", "IOS", "WEB_APP"
            ] = ...,
            **kwargs: typing.Any
        ) -> ApplicationHttpRequest: ...
        def getEndPoint(
            self,
            *,
            applicationId: str = ...,
            endPointType: typing_extensions.Literal[
                "END_POINT_TYPE_UNSPECIFIED", "PROFILE_CREATION", "PROFILE_SETTINGS"
            ] = ...,
            **kwargs: typing.Any
        ) -> EndPointHttpRequest: ...
        def played(self, **kwargs: typing.Any) -> googleapiclient.http.HttpRequest: ...
        def verify(
            self, *, applicationId: str, **kwargs: typing.Any
        ) -> ApplicationVerifyResponseHttpRequest: ...

    @typing.type_check_only
    class EventsResource(googleapiclient.discovery.Resource):
        def listByPlayer(
            self,
            *,
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> PlayerEventListResponseHttpRequest: ...
        def listByPlayer_next(
            self,
            previous_request: PlayerEventListResponseHttpRequest,
            previous_response: PlayerEventListResponse,
        ) -> PlayerEventListResponseHttpRequest | None: ...
        def listDefinitions(
            self,
            *,
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> EventDefinitionListResponseHttpRequest: ...
        def listDefinitions_next(
            self,
            previous_request: EventDefinitionListResponseHttpRequest,
            previous_response: EventDefinitionListResponse,
        ) -> EventDefinitionListResponseHttpRequest | None: ...
        def record(
            self,
            *,
            body: EventRecordRequest = ...,
            language: str = ...,
            **kwargs: typing.Any
        ) -> EventUpdateResponseHttpRequest: ...

    @typing.type_check_only
    class LeaderboardsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, leaderboardId: str, language: str = ..., **kwargs: typing.Any
        ) -> LeaderboardHttpRequest: ...
        def list(
            self,
            *,
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LeaderboardListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: LeaderboardListResponseHttpRequest,
            previous_response: LeaderboardListResponse,
        ) -> LeaderboardListResponseHttpRequest | None: ...

    @typing.type_check_only
    class MetagameResource(googleapiclient.discovery.Resource):
        def getMetagameConfig(
            self, **kwargs: typing.Any
        ) -> MetagameConfigHttpRequest: ...
        def listCategoriesByPlayer(
            self,
            *,
            playerId: str,
            collection: typing_extensions.Literal["COLLECTION_UNSPECIFIED", "ALL"],
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> CategoryListResponseHttpRequest: ...
        def listCategoriesByPlayer_next(
            self,
            previous_request: CategoryListResponseHttpRequest,
            previous_response: CategoryListResponse,
        ) -> CategoryListResponseHttpRequest | None: ...

    @typing.type_check_only
    class PlayersResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            playerId: str,
            language: str = ...,
            playerIdConsistencyToken: str = ...,
            **kwargs: typing.Any
        ) -> PlayerHttpRequest: ...
        def getScopedPlayerIds(
            self, **kwargs: typing.Any
        ) -> ScopedPlayerIdsHttpRequest: ...
        def list(
            self,
            *,
            collection: typing_extensions.Literal[
                "CONNECTED", "VISIBLE", "FRIENDS_ALL"
            ],
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> PlayerListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: PlayerListResponseHttpRequest,
            previous_response: PlayerListResponse,
        ) -> PlayerListResponseHttpRequest | None: ...

    @typing.type_check_only
    class RevisionsResource(googleapiclient.discovery.Resource):
        def check(
            self, *, clientRevision: str, **kwargs: typing.Any
        ) -> RevisionCheckResponseHttpRequest: ...

    @typing.type_check_only
    class ScoresResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            playerId: str,
            leaderboardId: str,
            timeSpan: typing_extensions.Literal[
                "SCORE_TIME_SPAN_UNSPECIFIED", "ALL", "ALL_TIME", "WEEKLY", "DAILY"
            ],
            includeRankType: typing_extensions.Literal[
                "INCLUDE_RANK_TYPE_UNSPECIFIED", "ALL", "PUBLIC", "SOCIAL", "FRIENDS"
            ] = ...,
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> PlayerLeaderboardScoreListResponseHttpRequest: ...
        def get_next(
            self,
            previous_request: PlayerLeaderboardScoreListResponseHttpRequest,
            previous_response: PlayerLeaderboardScoreListResponse,
        ) -> PlayerLeaderboardScoreListResponseHttpRequest | None: ...
        def list(
            self,
            *,
            leaderboardId: str,
            collection: typing_extensions.Literal[
                "SCORE_COLLECTION_UNSPECIFIED", "PUBLIC", "SOCIAL", "FRIENDS"
            ],
            timeSpan: typing_extensions.Literal[
                "SCORE_TIME_SPAN_UNSPECIFIED", "ALL_TIME", "WEEKLY", "DAILY"
            ],
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LeaderboardScoresHttpRequest: ...
        def list_next(
            self,
            previous_request: LeaderboardScoresHttpRequest,
            previous_response: LeaderboardScores,
        ) -> LeaderboardScoresHttpRequest | None: ...
        def listWindow(
            self,
            *,
            leaderboardId: str,
            collection: typing_extensions.Literal[
                "SCORE_COLLECTION_UNSPECIFIED", "PUBLIC", "SOCIAL", "FRIENDS"
            ],
            timeSpan: typing_extensions.Literal[
                "SCORE_TIME_SPAN_UNSPECIFIED", "ALL_TIME", "WEEKLY", "DAILY"
            ],
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            resultsAbove: int = ...,
            returnTopIfAbsent: bool = ...,
            **kwargs: typing.Any
        ) -> LeaderboardScoresHttpRequest: ...
        def listWindow_next(
            self,
            previous_request: LeaderboardScoresHttpRequest,
            previous_response: LeaderboardScores,
        ) -> LeaderboardScoresHttpRequest | None: ...
        def submit(
            self,
            *,
            leaderboardId: str,
            score: str,
            language: str = ...,
            scoreTag: str = ...,
            **kwargs: typing.Any
        ) -> PlayerScoreResponseHttpRequest: ...
        def submitMultiple(
            self,
            *,
            body: PlayerScoreSubmissionList = ...,
            language: str = ...,
            **kwargs: typing.Any
        ) -> PlayerScoreListResponseHttpRequest: ...

    @typing.type_check_only
    class SnapshotsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, snapshotId: str, language: str = ..., **kwargs: typing.Any
        ) -> SnapshotHttpRequest: ...
        def list(
            self,
            *,
            playerId: str,
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> SnapshotListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: SnapshotListResponseHttpRequest,
            previous_response: SnapshotListResponse,
        ) -> SnapshotListResponseHttpRequest | None: ...

    @typing.type_check_only
    class StatsResource(googleapiclient.discovery.Resource):
        def get(self, **kwargs: typing.Any) -> StatsResponseHttpRequest: ...

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
    def achievementDefinitions(self) -> AchievementDefinitionsResource: ...
    def achievements(self) -> AchievementsResource: ...
    def applications(self) -> ApplicationsResource: ...
    def events(self) -> EventsResource: ...
    def leaderboards(self) -> LeaderboardsResource: ...
    def metagame(self) -> MetagameResource: ...
    def players(self) -> PlayersResource: ...
    def revisions(self) -> RevisionsResource: ...
    def scores(self) -> ScoresResource: ...
    def snapshots(self) -> SnapshotsResource: ...
    def stats(self) -> StatsResource: ...

@typing.type_check_only
class AchievementDefinitionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AchievementDefinitionsListResponse: ...

@typing.type_check_only
class AchievementIncrementResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AchievementIncrementResponse: ...

@typing.type_check_only
class AchievementRevealResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AchievementRevealResponse: ...

@typing.type_check_only
class AchievementSetStepsAtLeastResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AchievementSetStepsAtLeastResponse: ...

@typing.type_check_only
class AchievementUnlockResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AchievementUnlockResponse: ...

@typing.type_check_only
class AchievementUpdateMultipleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AchievementUpdateMultipleResponse: ...

@typing.type_check_only
class ApplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Application: ...

@typing.type_check_only
class ApplicationVerifyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApplicationVerifyResponse: ...

@typing.type_check_only
class CategoryListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CategoryListResponse: ...

@typing.type_check_only
class EndPointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EndPoint: ...

@typing.type_check_only
class EventDefinitionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EventDefinitionListResponse: ...

@typing.type_check_only
class EventUpdateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EventUpdateResponse: ...

@typing.type_check_only
class LeaderboardHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Leaderboard: ...

@typing.type_check_only
class LeaderboardListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LeaderboardListResponse: ...

@typing.type_check_only
class LeaderboardScoresHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LeaderboardScores: ...

@typing.type_check_only
class MetagameConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MetagameConfig: ...

@typing.type_check_only
class PlayerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Player: ...

@typing.type_check_only
class PlayerAchievementListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlayerAchievementListResponse: ...

@typing.type_check_only
class PlayerEventListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlayerEventListResponse: ...

@typing.type_check_only
class PlayerLeaderboardScoreListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlayerLeaderboardScoreListResponse: ...

@typing.type_check_only
class PlayerListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlayerListResponse: ...

@typing.type_check_only
class PlayerScoreListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlayerScoreListResponse: ...

@typing.type_check_only
class PlayerScoreResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlayerScoreResponse: ...

@typing.type_check_only
class RevisionCheckResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RevisionCheckResponse: ...

@typing.type_check_only
class ScopedPlayerIdsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ScopedPlayerIds: ...

@typing.type_check_only
class SnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Snapshot: ...

@typing.type_check_only
class SnapshotListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SnapshotListResponse: ...

@typing.type_check_only
class StatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> StatsResponse: ...
