import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class GamesResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccesstokensResource(googleapiclient.discovery.Resource):
        def generatePlayGroupingApiToken(
            self, *, packageName: str = ..., persona: str = ..., **kwargs: typing.Any
        ) -> GeneratePlayGroupingApiTokenResponseHttpRequest: ...
        def generateRecallPlayGroupingApiToken(
            self,
            *,
            packageName: str = ...,
            persona: str = ...,
            recallSessionId: str = ...,
            **kwargs: typing.Any,
        ) -> GenerateRecallPlayGroupingApiTokenResponseHttpRequest: ...

    @typing.type_check_only
    class AchievementDefinitionsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            platformType: typing_extensions.Literal["ANDROID", "IOS", "WEB_APP"] = ...,
            **kwargs: typing.Any,
        ) -> ApplicationHttpRequest: ...
        def getEndPoint(
            self,
            *,
            applicationId: str = ...,
            endPointType: typing_extensions.Literal[
                "PROFILE_CREATION", "PROFILE_SETTINGS"
            ] = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            collection: typing_extensions.Literal["ALL"],
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> PlayerHttpRequest: ...
        def getMultipleApplicationPlayerIds(
            self, *, applicationIds: str | _list[str] = ..., **kwargs: typing.Any
        ) -> GetMultipleApplicationPlayerIdsResponseHttpRequest: ...
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
            **kwargs: typing.Any,
        ) -> PlayerListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: PlayerListResponseHttpRequest,
            previous_response: PlayerListResponse,
        ) -> PlayerListResponseHttpRequest | None: ...

    @typing.type_check_only
    class RecallResource(googleapiclient.discovery.Resource):
        def gamesPlayerTokens(
            self,
            *,
            sessionId: str,
            applicationIds: str | _list[str] = ...,
            **kwargs: typing.Any,
        ) -> RetrieveGamesPlayerTokensResponseHttpRequest: ...
        def lastTokenFromAllDeveloperGames(
            self, *, sessionId: str, **kwargs: typing.Any
        ) -> RetrieveDeveloperGamesLastPlayerTokenResponseHttpRequest: ...
        def linkPersona(
            self, *, body: LinkPersonaRequest = ..., **kwargs: typing.Any
        ) -> LinkPersonaResponseHttpRequest: ...
        def resetPersona(
            self, *, body: ResetPersonaRequest = ..., **kwargs: typing.Any
        ) -> ResetPersonaResponseHttpRequest: ...
        def retrieveTokens(
            self, *, sessionId: str, **kwargs: typing.Any
        ) -> RetrievePlayerTokensResponseHttpRequest: ...
        def unlinkPersona(
            self, *, body: UnlinkPersonaRequest = ..., **kwargs: typing.Any
        ) -> UnlinkPersonaResponseHttpRequest: ...

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
            timeSpan: typing_extensions.Literal["ALL", "ALL_TIME", "WEEKLY", "DAILY"],
            includeRankType: typing_extensions.Literal[
                "ALL", "PUBLIC", "SOCIAL", "FRIENDS"
            ] = ...,
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
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
            collection: typing_extensions.Literal["PUBLIC", "SOCIAL", "FRIENDS"],
            timeSpan: typing_extensions.Literal["ALL_TIME", "WEEKLY", "DAILY"],
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
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
            collection: typing_extensions.Literal["PUBLIC", "SOCIAL", "FRIENDS"],
            timeSpan: typing_extensions.Literal["ALL_TIME", "WEEKLY", "DAILY"],
            language: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            resultsAbove: int = ...,
            returnTopIfAbsent: bool = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> PlayerScoreResponseHttpRequest: ...
        def submitMultiple(
            self,
            *,
            body: PlayerScoreSubmissionList = ...,
            language: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def accesstokens(self) -> AccesstokensResource: ...
    def achievementDefinitions(self) -> AchievementDefinitionsResource: ...
    def achievements(self) -> AchievementsResource: ...
    def applications(self) -> ApplicationsResource: ...
    def events(self) -> EventsResource: ...
    def leaderboards(self) -> LeaderboardsResource: ...
    def metagame(self) -> MetagameResource: ...
    def players(self) -> PlayersResource: ...
    def recall(self) -> RecallResource: ...
    def revisions(self) -> RevisionsResource: ...
    def scores(self) -> ScoresResource: ...
    def snapshots(self) -> SnapshotsResource: ...
    def stats(self) -> StatsResource: ...

@typing.type_check_only
class AchievementDefinitionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AchievementDefinitionsListResponse: ...

@typing.type_check_only
class AchievementIncrementResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AchievementIncrementResponse: ...

@typing.type_check_only
class AchievementRevealResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AchievementRevealResponse: ...

@typing.type_check_only
class AchievementSetStepsAtLeastResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AchievementSetStepsAtLeastResponse: ...

@typing.type_check_only
class AchievementUnlockResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AchievementUnlockResponse: ...

@typing.type_check_only
class AchievementUpdateMultipleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AchievementUpdateMultipleResponse: ...

@typing.type_check_only
class ApplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Application: ...

@typing.type_check_only
class ApplicationVerifyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ApplicationVerifyResponse: ...

@typing.type_check_only
class CategoryListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CategoryListResponse: ...

@typing.type_check_only
class EndPointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EndPoint: ...

@typing.type_check_only
class EventDefinitionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventDefinitionListResponse: ...

@typing.type_check_only
class EventUpdateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventUpdateResponse: ...

@typing.type_check_only
class GeneratePlayGroupingApiTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GeneratePlayGroupingApiTokenResponse: ...

@typing.type_check_only
class GenerateRecallPlayGroupingApiTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateRecallPlayGroupingApiTokenResponse: ...

@typing.type_check_only
class GetMultipleApplicationPlayerIdsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetMultipleApplicationPlayerIdsResponse: ...

@typing.type_check_only
class LeaderboardHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Leaderboard: ...

@typing.type_check_only
class LeaderboardListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LeaderboardListResponse: ...

@typing.type_check_only
class LeaderboardScoresHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LeaderboardScores: ...

@typing.type_check_only
class LinkPersonaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LinkPersonaResponse: ...

@typing.type_check_only
class MetagameConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MetagameConfig: ...

@typing.type_check_only
class PlayerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Player: ...

@typing.type_check_only
class PlayerAchievementListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlayerAchievementListResponse: ...

@typing.type_check_only
class PlayerEventListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlayerEventListResponse: ...

@typing.type_check_only
class PlayerLeaderboardScoreListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlayerLeaderboardScoreListResponse: ...

@typing.type_check_only
class PlayerListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlayerListResponse: ...

@typing.type_check_only
class PlayerScoreListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlayerScoreListResponse: ...

@typing.type_check_only
class PlayerScoreResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlayerScoreResponse: ...

@typing.type_check_only
class ResetPersonaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ResetPersonaResponse: ...

@typing.type_check_only
class RetrieveDeveloperGamesLastPlayerTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RetrieveDeveloperGamesLastPlayerTokenResponse: ...

@typing.type_check_only
class RetrieveGamesPlayerTokensResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RetrieveGamesPlayerTokensResponse: ...

@typing.type_check_only
class RetrievePlayerTokensResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RetrievePlayerTokensResponse: ...

@typing.type_check_only
class RevisionCheckResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RevisionCheckResponse: ...

@typing.type_check_only
class ScopedPlayerIdsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ScopedPlayerIds: ...

@typing.type_check_only
class SnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Snapshot: ...

@typing.type_check_only
class SnapshotListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SnapshotListResponse: ...

@typing.type_check_only
class StatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> StatsResponse: ...

@typing.type_check_only
class UnlinkPersonaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UnlinkPersonaResponse: ...
