import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class GamesResource(googleapiclient.discovery.Resource):
    class AchievementDefinitionsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            language: str = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> AchievementDefinitionsListResponseHttpRequest: ...
    class ScoresResource(googleapiclient.discovery.Resource):
        def submitMultiple(
            self,
            *,
            body: PlayerScoreSubmissionList = ...,
            language: str = ...,
            **kwargs: typing.Any
        ) -> PlayerScoreListResponseHttpRequest: ...
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
            returnTopIfAbsent: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            language: str = ...,
            resultsAbove: int = ...,
            **kwargs: typing.Any
        ) -> LeaderboardScoresHttpRequest: ...
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
            pageToken: str = ...,
            maxResults: int = ...,
            language: str = ...,
            **kwargs: typing.Any
        ) -> LeaderboardScoresHttpRequest: ...
        def get(
            self,
            *,
            playerId: str,
            leaderboardId: str,
            timeSpan: typing_extensions.Literal[
                "SCORE_TIME_SPAN_UNSPECIFIED", "ALL", "ALL_TIME", "WEEKLY", "DAILY"
            ],
            pageToken: str = ...,
            language: str = ...,
            maxResults: int = ...,
            includeRankType: typing_extensions.Literal[
                "INCLUDE_RANK_TYPE_UNSPECIFIED", "ALL", "PUBLIC", "SOCIAL", "FRIENDS"
            ] = ...,
            **kwargs: typing.Any
        ) -> PlayerLeaderboardScoreListResponseHttpRequest: ...
        def submit(
            self,
            *,
            leaderboardId: str,
            score: str,
            scoreTag: str = ...,
            language: str = ...,
            **kwargs: typing.Any
        ) -> PlayerScoreResponseHttpRequest: ...
    class RevisionsResource(googleapiclient.discovery.Resource):
        def check(
            self, *, clientRevision: str, **kwargs: typing.Any
        ) -> RevisionCheckResponseHttpRequest: ...
    class LeaderboardsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, leaderboardId: str, language: str = ..., **kwargs: typing.Any
        ) -> LeaderboardHttpRequest: ...
        def list(
            self,
            *,
            language: str = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> LeaderboardListResponseHttpRequest: ...
    class EventsResource(googleapiclient.discovery.Resource):
        def record(
            self,
            *,
            body: EventRecordRequest = ...,
            language: str = ...,
            **kwargs: typing.Any
        ) -> EventUpdateResponseHttpRequest: ...
        def listDefinitions(
            self,
            *,
            pageToken: str = ...,
            language: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> EventDefinitionListResponseHttpRequest: ...
        def listByPlayer(
            self,
            *,
            language: str = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> PlayerEventListResponseHttpRequest: ...
    class MetagameResource(googleapiclient.discovery.Resource):
        def listCategoriesByPlayer(
            self,
            *,
            playerId: str,
            collection: typing_extensions.Literal["COLLECTION_UNSPECIFIED", "ALL"],
            pageToken: str = ...,
            maxResults: int = ...,
            language: str = ...,
            **kwargs: typing.Any
        ) -> CategoryListResponseHttpRequest: ...
        def getMetagameConfig(
            self, **kwargs: typing.Any
        ) -> MetagameConfigHttpRequest: ...
    class StatsResource(googleapiclient.discovery.Resource):
        def get(self, **kwargs: typing.Any) -> StatsResponseHttpRequest: ...
    class ApplicationsResource(googleapiclient.discovery.Resource):
        def played(self, **kwargs: typing.Any) -> googleapiclient.http.HttpRequest: ...
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
        def verify(
            self, *, applicationId: str, **kwargs: typing.Any
        ) -> ApplicationVerifyResponseHttpRequest: ...
    class SnapshotsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            playerId: str,
            pageToken: str = ...,
            maxResults: int = ...,
            language: str = ...,
            **kwargs: typing.Any
        ) -> SnapshotListResponseHttpRequest: ...
        def get(
            self, *, snapshotId: str, language: str = ..., **kwargs: typing.Any
        ) -> SnapshotHttpRequest: ...
    class AchievementsResource(googleapiclient.discovery.Resource):
        def updateMultiple(
            self, *, body: AchievementUpdateMultipleRequest = ..., **kwargs: typing.Any
        ) -> AchievementUpdateMultipleResponseHttpRequest: ...
        def list(
            self,
            *,
            playerId: str,
            maxResults: int = ...,
            language: str = ...,
            pageToken: str = ...,
            state: typing_extensions.Literal[
                "ALL", "HIDDEN", "REVEALED", "UNLOCKED"
            ] = ...,
            **kwargs: typing.Any
        ) -> PlayerAchievementListResponseHttpRequest: ...
        def setStepsAtLeast(
            self, *, achievementId: str, steps: int, **kwargs: typing.Any
        ) -> AchievementSetStepsAtLeastResponseHttpRequest: ...
        def increment(
            self,
            *,
            achievementId: str,
            stepsToIncrement: int,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> AchievementIncrementResponseHttpRequest: ...
        def unlock(
            self, *, achievementId: str, **kwargs: typing.Any
        ) -> AchievementUnlockResponseHttpRequest: ...
        def reveal(
            self, *, achievementId: str, **kwargs: typing.Any
        ) -> AchievementRevealResponseHttpRequest: ...
    class PlayersResource(googleapiclient.discovery.Resource):
        def get(
            self, *, playerId: str, language: str = ..., **kwargs: typing.Any
        ) -> PlayerHttpRequest: ...
        def list(
            self,
            *,
            collection: typing_extensions.Literal[
                "CONNECTED", "VISIBLE", "FRIENDS_ALL"
            ],
            pageToken: str = ...,
            maxResults: int = ...,
            language: str = ...,
            **kwargs: typing.Any
        ) -> PlayerListResponseHttpRequest: ...
    def achievementDefinitions(self) -> AchievementDefinitionsResource: ...
    def scores(self) -> ScoresResource: ...
    def revisions(self) -> RevisionsResource: ...
    def leaderboards(self) -> LeaderboardsResource: ...
    def events(self) -> EventsResource: ...
    def metagame(self) -> MetagameResource: ...
    def stats(self) -> StatsResource: ...
    def applications(self) -> ApplicationsResource: ...
    def snapshots(self) -> SnapshotsResource: ...
    def achievements(self) -> AchievementsResource: ...
    def players(self) -> PlayersResource: ...

class ApplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Application: ...

class MetagameConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MetagameConfig: ...

class PlayerListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlayerListResponse: ...

class PlayerAchievementListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlayerAchievementListResponse: ...

class SnapshotListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SnapshotListResponse: ...

class AchievementIncrementResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AchievementIncrementResponse: ...

class AchievementRevealResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AchievementRevealResponse: ...

class PlayerScoreListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlayerScoreListResponse: ...

class AchievementUnlockResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AchievementUnlockResponse: ...

class AchievementSetStepsAtLeastResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AchievementSetStepsAtLeastResponse: ...

class PlayerLeaderboardScoreListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlayerLeaderboardScoreListResponse: ...

class EventUpdateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EventUpdateResponse: ...

class PlayerScoreResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlayerScoreResponse: ...

class ApplicationVerifyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApplicationVerifyResponse: ...

class EventDefinitionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EventDefinitionListResponse: ...

class LeaderboardScoresHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LeaderboardScores: ...

class CategoryListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CategoryListResponse: ...

class LeaderboardHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Leaderboard: ...

class PlayerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Player: ...

class LeaderboardListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LeaderboardListResponse: ...

class PlayerEventListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlayerEventListResponse: ...

class RevisionCheckResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RevisionCheckResponse: ...

class SnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Snapshot: ...

class AchievementUpdateMultipleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AchievementUpdateMultipleResponse: ...

class AchievementDefinitionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AchievementDefinitionsListResponse: ...

class StatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> StatsResponse: ...
