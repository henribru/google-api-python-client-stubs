import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class YouTubeResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AbuseReportsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: AbuseReport = ...,
            **kwargs: typing.Any
        ) -> AbuseReportHttpRequest: ...
    @typing.type_check_only
    class ActivitiesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            channelId: str = ...,
            home: bool = ...,
            maxResults: int = ...,
            mine: bool = ...,
            pageToken: str = ...,
            publishedAfter: str = ...,
            publishedBefore: str = ...,
            regionCode: str = ...,
            **kwargs: typing.Any
        ) -> ActivityListResponseHttpRequest: ...
    @typing.type_check_only
    class CaptionsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str,
            onBehalfOf: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def download(
            self,
            *,
            id: str,
            onBehalfOf: str = ...,
            onBehalfOfContentOwner: str = ...,
            tfmt: str = ...,
            tlang: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Caption = ...,
            onBehalfOf: str = ...,
            onBehalfOfContentOwner: str = ...,
            sync: bool = ...,
            **kwargs: typing.Any
        ) -> CaptionHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            videoId: str,
            id: typing.Union[str, typing.List[str]] = ...,
            onBehalfOf: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> CaptionListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Caption = ...,
            onBehalfOf: str = ...,
            onBehalfOfContentOwner: str = ...,
            sync: bool = ...,
            **kwargs: typing.Any
        ) -> CaptionHttpRequest: ...
    @typing.type_check_only
    class ChannelBannersResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            body: ChannelBannerResource = ...,
            channelId: str = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> ChannelBannerResourceHttpRequest: ...
    @typing.type_check_only
    class ChannelSectionsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, onBehalfOfContentOwner: str = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: ChannelSection = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> ChannelSectionHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            channelId: str = ...,
            hl: str = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            mine: bool = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> ChannelSectionListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: ChannelSection = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> ChannelSectionHttpRequest: ...
    @typing.type_check_only
    class ChannelsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            categoryId: str = ...,
            forUsername: str = ...,
            hl: str = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            managedByMe: bool = ...,
            maxResults: int = ...,
            mine: bool = ...,
            mySubscribers: bool = ...,
            onBehalfOfContentOwner: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ChannelListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Channel = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
    @typing.type_check_only
    class CommentThreadsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: CommentThread = ...,
            **kwargs: typing.Any
        ) -> CommentThreadHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            allThreadsRelatedToChannelId: str = ...,
            channelId: str = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            moderationStatus: typing_extensions.Literal[
                "published", "heldForReview", "likelySpam", "rejected"
            ] = ...,
            order: typing_extensions.Literal[
                "orderUnspecified", "time", "relevance"
            ] = ...,
            pageToken: str = ...,
            searchTerms: str = ...,
            textFormat: typing_extensions.Literal[
                "textFormatUnspecified", "html", "plainText"
            ] = ...,
            videoId: str = ...,
            **kwargs: typing.Any
        ) -> CommentThreadListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: CommentThread = ...,
            **kwargs: typing.Any
        ) -> CommentThreadHttpRequest: ...
    @typing.type_check_only
    class CommentsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Comment = ...,
            **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            id: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            parentId: str = ...,
            textFormat: typing_extensions.Literal[
                "textFormatUnspecified", "html", "plainText"
            ] = ...,
            **kwargs: typing.Any
        ) -> CommentListResponseHttpRequest: ...
        def markAsSpam(
            self, *, id: typing.Union[str, typing.List[str]], **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def setModerationStatus(
            self,
            *,
            id: typing.Union[str, typing.List[str]],
            moderationStatus: typing_extensions.Literal[
                "published", "heldForReview", "likelySpam", "rejected"
            ],
            banAuthor: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Comment = ...,
            **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
    @typing.type_check_only
    class I18nLanguagesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            hl: str = ...,
            **kwargs: typing.Any
        ) -> I18nLanguageListResponseHttpRequest: ...
    @typing.type_check_only
    class I18nRegionsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            hl: str = ...,
            **kwargs: typing.Any
        ) -> I18nRegionListResponseHttpRequest: ...
    @typing.type_check_only
    class LiveBroadcastsResource(googleapiclient.discovery.Resource):
        def bind(
            self,
            *,
            id: str,
            part: typing.Union[str, typing.List[str]],
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            streamId: str = ...,
            **kwargs: typing.Any
        ) -> LiveBroadcastHttpRequest: ...
        def delete(
            self,
            *,
            id: str,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveBroadcast = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> LiveBroadcastHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            broadcastStatus: typing_extensions.Literal[
                "broadcastStatusFilterUnspecified",
                "all",
                "active",
                "upcoming",
                "completed",
            ] = ...,
            broadcastType: typing_extensions.Literal[
                "broadcastTypeFilterUnspecified", "all", "event", "persistent"
            ] = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            mine: bool = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LiveBroadcastListResponseHttpRequest: ...
        def transition(
            self,
            *,
            broadcastStatus: typing_extensions.Literal[
                "statusUnspecified", "testing", "live", "complete"
            ],
            id: str,
            part: typing.Union[str, typing.List[str]],
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> LiveBroadcastHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveBroadcast = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> LiveBroadcastHttpRequest: ...
    @typing.type_check_only
    class LiveChatBansResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveChatBan = ...,
            **kwargs: typing.Any
        ) -> LiveChatBanHttpRequest: ...
    @typing.type_check_only
    class LiveChatMessagesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveChatMessage = ...,
            **kwargs: typing.Any
        ) -> LiveChatMessageHttpRequest: ...
        def list(
            self,
            *,
            liveChatId: str,
            part: typing.Union[str, typing.List[str]],
            hl: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            profileImageSize: int = ...,
            **kwargs: typing.Any
        ) -> LiveChatMessageListResponseHttpRequest: ...
    @typing.type_check_only
    class LiveChatModeratorsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveChatModerator = ...,
            **kwargs: typing.Any
        ) -> LiveChatModeratorHttpRequest: ...
        def list(
            self,
            *,
            liveChatId: str,
            part: typing.Union[str, typing.List[str]],
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LiveChatModeratorListResponseHttpRequest: ...
    @typing.type_check_only
    class LiveStreamsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveStream = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> LiveStreamHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            id: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            mine: bool = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LiveStreamListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveStream = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> LiveStreamHttpRequest: ...
    @typing.type_check_only
    class MembersResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            filterByMemberChannelId: str = ...,
            hasAccessToLevel: str = ...,
            maxResults: int = ...,
            mode: typing_extensions.Literal[
                "listMembersModeUnknown", "updates", "all_current"
            ] = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> MemberListResponseHttpRequest: ...
    @typing.type_check_only
    class MembershipsLevelsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, part: typing.Union[str, typing.List[str]], **kwargs: typing.Any
        ) -> MembershipsLevelListResponseHttpRequest: ...
    @typing.type_check_only
    class PlaylistItemsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, onBehalfOfContentOwner: str = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: PlaylistItem = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> PlaylistItemHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            id: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            onBehalfOfContentOwner: str = ...,
            pageToken: str = ...,
            playlistId: str = ...,
            videoId: str = ...,
            **kwargs: typing.Any
        ) -> PlaylistItemListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: PlaylistItem = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> PlaylistItemHttpRequest: ...
    @typing.type_check_only
    class PlaylistsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, onBehalfOfContentOwner: str = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Playlist = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> PlaylistHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            channelId: str = ...,
            hl: str = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            mine: bool = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> PlaylistListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Playlist = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> PlaylistHttpRequest: ...
    @typing.type_check_only
    class SearchResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            channelId: str = ...,
            channelType: typing_extensions.Literal[
                "channelTypeUnspecified", "any", "show"
            ] = ...,
            eventType: typing_extensions.Literal[
                "none", "upcoming", "live", "completed"
            ] = ...,
            forContentOwner: bool = ...,
            forDeveloper: bool = ...,
            forMine: bool = ...,
            location: str = ...,
            locationRadius: str = ...,
            maxResults: int = ...,
            onBehalfOfContentOwner: str = ...,
            order: typing_extensions.Literal[
                "searchSortUnspecified",
                "date",
                "rating",
                "viewCount",
                "relevance",
                "title",
                "videoCount",
            ] = ...,
            pageToken: str = ...,
            publishedAfter: str = ...,
            publishedBefore: str = ...,
            q: str = ...,
            regionCode: str = ...,
            relatedToVideoId: str = ...,
            relevanceLanguage: str = ...,
            safeSearch: typing_extensions.Literal[
                "safeSearchSettingUnspecified", "none", "moderate", "strict"
            ] = ...,
            topicId: str = ...,
            type: typing.Union[str, typing.List[str]] = ...,
            videoCaption: typing_extensions.Literal[
                "videoCaptionUnspecified", "any", "closedCaption", "none"
            ] = ...,
            videoCategoryId: str = ...,
            videoDefinition: typing_extensions.Literal["any", "standard", "high"] = ...,
            videoDimension: typing_extensions.Literal["any", "2d", "3d"] = ...,
            videoDuration: typing_extensions.Literal[
                "videoDurationUnspecified", "any", "short", "medium", "long"
            ] = ...,
            videoEmbeddable: typing_extensions.Literal[
                "videoEmbeddableUnspecified", "any", "true"
            ] = ...,
            videoLicense: typing_extensions.Literal[
                "any", "youtube", "creativeCommon"
            ] = ...,
            videoSyndicated: typing_extensions.Literal[
                "videoSyndicatedUnspecified", "any", "true"
            ] = ...,
            videoType: typing_extensions.Literal[
                "videoTypeUnspecified", "any", "movie", "episode"
            ] = ...,
            **kwargs: typing.Any
        ) -> SearchListResponseHttpRequest: ...
    @typing.type_check_only
    class SubscriptionsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Subscription = ...,
            **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            channelId: str = ...,
            forChannelId: str = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            mine: bool = ...,
            myRecentSubscribers: bool = ...,
            mySubscribers: bool = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            order: typing_extensions.Literal[
                "subscriptionOrderUnspecified", "relevance", "unread", "alphabetical"
            ] = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> SubscriptionListResponseHttpRequest: ...
    @typing.type_check_only
    class SuperChatEventsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            hl: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> SuperChatEventListResponseHttpRequest: ...
    @typing.type_check_only
    class TestsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: TestItem = ...,
            **kwargs: typing.Any
        ) -> TestItemHttpRequest: ...
    @typing.type_check_only
    class ThirdPartyLinksResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            linkingToken: str,
            type: typing_extensions.Literal["linkUnspecified", "channelToStoreLink"],
            part: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: ThirdPartyLink = ...,
            **kwargs: typing.Any
        ) -> ThirdPartyLinkHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            linkingToken: str = ...,
            type: typing_extensions.Literal[
                "linkUnspecified", "channelToStoreLink"
            ] = ...,
            **kwargs: typing.Any
        ) -> ThirdPartyLinkHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: ThirdPartyLink = ...,
            **kwargs: typing.Any
        ) -> ThirdPartyLinkHttpRequest: ...
    @typing.type_check_only
    class ThumbnailsResource(googleapiclient.discovery.Resource):
        def set(
            self,
            *,
            videoId: str,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> ThumbnailSetResponseHttpRequest: ...
    @typing.type_check_only
    class VideoAbuseReportReasonsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            hl: str = ...,
            **kwargs: typing.Any
        ) -> VideoAbuseReportReasonListResponseHttpRequest: ...
    @typing.type_check_only
    class VideoCategoriesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            hl: str = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            regionCode: str = ...,
            **kwargs: typing.Any
        ) -> VideoCategoryListResponseHttpRequest: ...
    @typing.type_check_only
    class VideosResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, onBehalfOfContentOwner: str = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def getRating(
            self,
            *,
            id: typing.Union[str, typing.List[str]],
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> VideoRatingListResponseHttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Video = ...,
            autoLevels: bool = ...,
            notifySubscribers: bool = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            stabilize: bool = ...,
            **kwargs: typing.Any
        ) -> VideoHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            chart: typing_extensions.Literal["chartUnspecified", "mostPopular"] = ...,
            hl: str = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            locale: str = ...,
            maxHeight: int = ...,
            maxResults: int = ...,
            maxWidth: int = ...,
            myRating: typing_extensions.Literal["none", "like", "dislike"] = ...,
            onBehalfOfContentOwner: str = ...,
            pageToken: str = ...,
            regionCode: str = ...,
            videoCategoryId: str = ...,
            **kwargs: typing.Any
        ) -> VideoListResponseHttpRequest: ...
        def rate(
            self,
            *,
            id: str,
            rating: typing_extensions.Literal["none", "like", "dislike"],
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def reportAbuse(
            self,
            *,
            body: VideoAbuseReport = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Video = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> VideoHttpRequest: ...
    @typing.type_check_only
    class WatermarksResource(googleapiclient.discovery.Resource):
        def set(
            self,
            *,
            channelId: str,
            body: InvideoBranding = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def unset(
            self,
            *,
            channelId: str,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    def abuseReports(self) -> AbuseReportsResource: ...
    def activities(self) -> ActivitiesResource: ...
    def captions(self) -> CaptionsResource: ...
    def channelBanners(self) -> ChannelBannersResource: ...
    def channelSections(self) -> ChannelSectionsResource: ...
    def channels(self) -> ChannelsResource: ...
    def commentThreads(self) -> CommentThreadsResource: ...
    def comments(self) -> CommentsResource: ...
    def i18nLanguages(self) -> I18nLanguagesResource: ...
    def i18nRegions(self) -> I18nRegionsResource: ...
    def liveBroadcasts(self) -> LiveBroadcastsResource: ...
    def liveChatBans(self) -> LiveChatBansResource: ...
    def liveChatMessages(self) -> LiveChatMessagesResource: ...
    def liveChatModerators(self) -> LiveChatModeratorsResource: ...
    def liveStreams(self) -> LiveStreamsResource: ...
    def members(self) -> MembersResource: ...
    def membershipsLevels(self) -> MembershipsLevelsResource: ...
    def playlistItems(self) -> PlaylistItemsResource: ...
    def playlists(self) -> PlaylistsResource: ...
    def search(self) -> SearchResource: ...
    def subscriptions(self) -> SubscriptionsResource: ...
    def superChatEvents(self) -> SuperChatEventsResource: ...
    def tests(self) -> TestsResource: ...
    def thirdPartyLinks(self) -> ThirdPartyLinksResource: ...
    def thumbnails(self) -> ThumbnailsResource: ...
    def videoAbuseReportReasons(self) -> VideoAbuseReportReasonsResource: ...
    def videoCategories(self) -> VideoCategoriesResource: ...
    def videos(self) -> VideosResource: ...
    def watermarks(self) -> WatermarksResource: ...

@typing.type_check_only
class AbuseReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AbuseReport: ...

@typing.type_check_only
class ActivityListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ActivityListResponse: ...

@typing.type_check_only
class CaptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Caption: ...

@typing.type_check_only
class CaptionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CaptionListResponse: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Channel: ...

@typing.type_check_only
class ChannelBannerResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ChannelBannerResource: ...

@typing.type_check_only
class ChannelListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ChannelListResponse: ...

@typing.type_check_only
class ChannelSectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ChannelSection: ...

@typing.type_check_only
class ChannelSectionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ChannelSectionListResponse: ...

@typing.type_check_only
class CommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Comment: ...

@typing.type_check_only
class CommentListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CommentListResponse: ...

@typing.type_check_only
class CommentThreadHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CommentThread: ...

@typing.type_check_only
class CommentThreadListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CommentThreadListResponse: ...

@typing.type_check_only
class I18nLanguageListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> I18nLanguageListResponse: ...

@typing.type_check_only
class I18nRegionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> I18nRegionListResponse: ...

@typing.type_check_only
class LiveBroadcastHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LiveBroadcast: ...

@typing.type_check_only
class LiveBroadcastListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LiveBroadcastListResponse: ...

@typing.type_check_only
class LiveChatBanHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LiveChatBan: ...

@typing.type_check_only
class LiveChatMessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LiveChatMessage: ...

@typing.type_check_only
class LiveChatMessageListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LiveChatMessageListResponse: ...

@typing.type_check_only
class LiveChatModeratorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LiveChatModerator: ...

@typing.type_check_only
class LiveChatModeratorListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LiveChatModeratorListResponse: ...

@typing.type_check_only
class LiveStreamHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LiveStream: ...

@typing.type_check_only
class LiveStreamListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LiveStreamListResponse: ...

@typing.type_check_only
class MemberListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> MemberListResponse: ...

@typing.type_check_only
class MembershipsLevelListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> MembershipsLevelListResponse: ...

@typing.type_check_only
class PlaylistHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Playlist: ...

@typing.type_check_only
class PlaylistItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PlaylistItem: ...

@typing.type_check_only
class PlaylistItemListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PlaylistItemListResponse: ...

@typing.type_check_only
class PlaylistListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PlaylistListResponse: ...

@typing.type_check_only
class SearchListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SearchListResponse: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Subscription: ...

@typing.type_check_only
class SubscriptionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SubscriptionListResponse: ...

@typing.type_check_only
class SuperChatEventListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SuperChatEventListResponse: ...

@typing.type_check_only
class TestItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TestItem: ...

@typing.type_check_only
class ThirdPartyLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ThirdPartyLink: ...

@typing.type_check_only
class ThumbnailSetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ThumbnailSetResponse: ...

@typing.type_check_only
class VideoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Video: ...

@typing.type_check_only
class VideoAbuseReportReasonListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> VideoAbuseReportReasonListResponse: ...

@typing.type_check_only
class VideoCategoryListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> VideoCategoryListResponse: ...

@typing.type_check_only
class VideoListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> VideoListResponse: ...

@typing.type_check_only
class VideoRatingListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> VideoRatingListResponse: ...
