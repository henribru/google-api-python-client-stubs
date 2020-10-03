import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class YouTubeResource(googleapiclient.discovery.Resource):
    class SuperChatEventsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            maxResults: int = ...,
            hl: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> SuperChatEventListResponseHttpRequest: ...
    class I18nRegionsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            hl: str = ...,
            **kwargs: typing.Any
        ) -> I18nRegionListResponseHttpRequest: ...
    class PlaylistItemsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, onBehalfOfContentOwner: str = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            playlistId: str = ...,
            videoId: str = ...,
            onBehalfOfContentOwner: str = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> PlaylistItemListResponseHttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: PlaylistItem = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> PlaylistItemHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: PlaylistItem = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> PlaylistItemHttpRequest: ...
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
    class MembershipsLevelsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, part: typing.Union[str, typing.List[str]], **kwargs: typing.Any
        ) -> MembershipsLevelListResponseHttpRequest: ...
    class SearchResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            channelType: typing_extensions.Literal[
                "channelTypeUnspecified", "any", "show"
            ] = ...,
            videoSyndicated: typing_extensions.Literal[
                "videoSyndicatedUnspecified", "any", "true"
            ] = ...,
            order: typing_extensions.Literal[
                "searchSortUnspecified",
                "date",
                "rating",
                "viewCount",
                "relevance",
                "title",
                "videoCount",
            ] = ...,
            type: typing.Union[str, typing.List[str]] = ...,
            videoCaption: typing_extensions.Literal[
                "videoCaptionUnspecified", "any", "closedCaption", "none"
            ] = ...,
            locationRadius: str = ...,
            publishedAfter: str = ...,
            regionCode: str = ...,
            forMine: bool = ...,
            maxResults: int = ...,
            forDeveloper: bool = ...,
            channelId: str = ...,
            videoDuration: typing_extensions.Literal[
                "videoDurationUnspecified", "any", "short", "medium", "long"
            ] = ...,
            videoEmbeddable: typing_extensions.Literal[
                "videoEmbeddableUnspecified", "any", "true"
            ] = ...,
            eventType: typing_extensions.Literal[
                "none", "upcoming", "live", "completed"
            ] = ...,
            location: str = ...,
            videoCategoryId: str = ...,
            videoDefinition: typing_extensions.Literal["any", "standard", "high"] = ...,
            q: str = ...,
            videoType: typing_extensions.Literal[
                "videoTypeUnspecified", "any", "movie", "episode"
            ] = ...,
            pageToken: str = ...,
            safeSearch: typing_extensions.Literal[
                "safeSearchSettingUnspecified", "none", "moderate", "strict"
            ] = ...,
            videoDimension: typing_extensions.Literal["any", "2d", "3d"] = ...,
            forContentOwner: bool = ...,
            topicId: str = ...,
            publishedBefore: str = ...,
            relevanceLanguage: str = ...,
            relatedToVideoId: str = ...,
            onBehalfOfContentOwner: str = ...,
            videoLicense: typing_extensions.Literal[
                "any", "youtube", "creativeCommon"
            ] = ...,
            **kwargs: typing.Any
        ) -> SearchListResponseHttpRequest: ...
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
    class ActivitiesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            maxResults: int = ...,
            channelId: str = ...,
            publishedAfter: str = ...,
            home: bool = ...,
            mine: bool = ...,
            publishedBefore: str = ...,
            regionCode: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ActivityListResponseHttpRequest: ...
    class LiveBroadcastsResource(googleapiclient.discovery.Resource):
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveBroadcast = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> LiveBroadcastHttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveBroadcast = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> LiveBroadcastHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            maxResults: int = ...,
            broadcastType: typing_extensions.Literal[
                "broadcastTypeFilterUnspecified", "all", "event", "persistent"
            ] = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            mine: bool = ...,
            pageToken: str = ...,
            broadcastStatus: typing_extensions.Literal[
                "broadcastStatusFilterUnspecified",
                "all",
                "active",
                "upcoming",
                "completed",
            ] = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> LiveBroadcastListResponseHttpRequest: ...
        def bind(
            self,
            *,
            id: str,
            part: typing.Union[str, typing.List[str]],
            onBehalfOfContentOwner: str = ...,
            streamId: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> LiveBroadcastHttpRequest: ...
        def delete(
            self,
            *,
            id: str,
            onBehalfOfContentOwnerChannel: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def control(
            self,
            *,
            id: str,
            part: typing.Union[str, typing.List[str]],
            walltime: str = ...,
            onBehalfOfContentOwner: str = ...,
            offsetTimeMs: str = ...,
            displaySlate: bool = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> LiveBroadcastHttpRequest: ...
        def transition(
            self,
            *,
            id: str,
            broadcastStatus: typing_extensions.Literal[
                "statusUnspecified", "testing", "live", "complete"
            ],
            part: typing.Union[str, typing.List[str]],
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> LiveBroadcastHttpRequest: ...
    class I18nLanguagesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            hl: str = ...,
            **kwargs: typing.Any
        ) -> I18nLanguageListResponseHttpRequest: ...
    class LiveChatModeratorsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            liveChatId: str,
            part: typing.Union[str, typing.List[str]],
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LiveChatModeratorListResponseHttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveChatModerator = ...,
            **kwargs: typing.Any
        ) -> LiveChatModeratorHttpRequest: ...
    class CaptionsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str,
            onBehalfOf: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            videoId: str,
            part: typing.Union[str, typing.List[str]],
            onBehalfOf: str = ...,
            onBehalfOfContentOwner: str = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> CaptionListResponseHttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Caption = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOf: str = ...,
            sync: bool = ...,
            **kwargs: typing.Any
        ) -> CaptionHttpRequest: ...
        def download(
            self,
            *,
            id: str,
            onBehalfOfContentOwner: str = ...,
            tlang: str = ...,
            tfmt: str = ...,
            onBehalfOf: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Caption = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOf: str = ...,
            sync: bool = ...,
            **kwargs: typing.Any
        ) -> CaptionHttpRequest: ...
    class ChannelSectionsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, onBehalfOfContentOwner: str = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: ChannelSection = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> ChannelSectionHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            hl: str = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            onBehalfOfContentOwner: str = ...,
            mine: bool = ...,
            channelId: str = ...,
            **kwargs: typing.Any
        ) -> ChannelSectionListResponseHttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: ChannelSection = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> ChannelSectionHttpRequest: ...
    class MembersResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            hasAccessToLevel: str = ...,
            maxResults: int = ...,
            mode: typing_extensions.Literal[
                "listMembersModeUnknown", "updates", "all_current"
            ] = ...,
            filterByMemberChannelId: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> MemberListResponseHttpRequest: ...
    class PlaylistsResource(googleapiclient.discovery.Resource):
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Playlist = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> PlaylistHttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Playlist = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> PlaylistHttpRequest: ...
        def delete(
            self, *, id: str, onBehalfOfContentOwner: str = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            onBehalfOfContentOwnerChannel: str = ...,
            hl: str = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            onBehalfOfContentOwner: str = ...,
            channelId: str = ...,
            mine: bool = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> PlaylistListResponseHttpRequest: ...
    class LiveChatMessagesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            liveChatId: str,
            part: typing.Union[str, typing.List[str]],
            profileImageSize: int = ...,
            maxResults: int = ...,
            hl: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LiveChatMessageListResponseHttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveChatMessage = ...,
            **kwargs: typing.Any
        ) -> LiveChatMessageHttpRequest: ...
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class ThumbnailsResource(googleapiclient.discovery.Resource):
        def set(
            self,
            *,
            videoId: str,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> ThumbnailSetResponseHttpRequest: ...
    class VideosResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, onBehalfOfContentOwner: str = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Video = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            notifySubscribers: bool = ...,
            stabilize: bool = ...,
            onBehalfOfContentOwner: str = ...,
            autoLevels: bool = ...,
            **kwargs: typing.Any
        ) -> VideoHttpRequest: ...
        def reportAbuse(
            self,
            *,
            body: VideoAbuseReport = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            myRating: typing_extensions.Literal["none", "like", "dislike"] = ...,
            pageToken: str = ...,
            maxWidth: int = ...,
            hl: str = ...,
            chart: typing_extensions.Literal["chartUnspecified", "mostPopular"] = ...,
            locale: str = ...,
            regionCode: str = ...,
            maxHeight: int = ...,
            onBehalfOfContentOwner: str = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
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
        def getRating(
            self,
            *,
            id: typing.Union[str, typing.List[str]],
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> VideoRatingListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Video = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> VideoHttpRequest: ...
    class LiveStreamsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            maxResults: int = ...,
            mine: bool = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LiveStreamListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveStream = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> LiveStreamHttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: LiveStream = ...,
            onBehalfOfContentOwner: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            **kwargs: typing.Any
        ) -> LiveStreamHttpRequest: ...
        def delete(
            self,
            *,
            id: str,
            onBehalfOfContentOwnerChannel: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
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
            moderationStatus: typing_extensions.Literal[
                "published", "heldForReview", "likelySpam", "rejected"
            ] = ...,
            videoId: str = ...,
            pageToken: str = ...,
            order: typing_extensions.Literal[
                "orderUnspecified", "time", "relevance"
            ] = ...,
            searchTerms: str = ...,
            allThreadsRelatedToChannelId: str = ...,
            channelId: str = ...,
            maxResults: int = ...,
            textFormat: typing_extensions.Literal[
                "textFormatUnspecified", "html", "plainText"
            ] = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> CommentThreadListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: CommentThread = ...,
            **kwargs: typing.Any
        ) -> CommentThreadHttpRequest: ...
    class VideoAbuseReportReasonsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            hl: str = ...,
            **kwargs: typing.Any
        ) -> VideoAbuseReportReasonListResponseHttpRequest: ...
    class SponsorsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            maxResults: int = ...,
            filter: typing_extensions.Literal[
                "sponsorFilterUnknown", "newest", "all"
            ] = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> SponsorListResponseHttpRequest: ...
    class CommentsResource(googleapiclient.discovery.Resource):
        def markAsSpam(
            self, *, id: typing.Union[str, typing.List[str]], **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
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
            textFormat: typing_extensions.Literal[
                "textFormatUnspecified", "html", "plainText"
            ] = ...,
            pageToken: str = ...,
            parentId: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> CommentListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Comment = ...,
            **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
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
    class AbuseReportsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: AbuseReport = ...,
            **kwargs: typing.Any
        ) -> AbuseReportHttpRequest: ...
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
    class SubscriptionsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            mySubscribers: bool = ...,
            onBehalfOfContentOwner: str = ...,
            forChannelId: str = ...,
            order: typing_extensions.Literal[
                "subscriptionOrderUnspecified", "relevance", "unread", "alphabetical"
            ] = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            myRecentSubscribers: bool = ...,
            pageToken: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            maxResults: int = ...,
            mine: bool = ...,
            channelId: str = ...,
            **kwargs: typing.Any
        ) -> SubscriptionListResponseHttpRequest: ...
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Subscription = ...,
            **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class ChannelsResource(googleapiclient.discovery.Resource):
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: Channel = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
        def list(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            pageToken: str = ...,
            mySubscribers: bool = ...,
            maxResults: int = ...,
            hl: str = ...,
            managedByMe: bool = ...,
            id: typing.Union[str, typing.List[str]] = ...,
            categoryId: str = ...,
            onBehalfOfContentOwner: str = ...,
            forUsername: str = ...,
            mine: bool = ...,
            **kwargs: typing.Any
        ) -> ChannelListResponseHttpRequest: ...
    class ThirdPartyLinksResource(googleapiclient.discovery.Resource):
        def update(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: ThirdPartyLink = ...,
            **kwargs: typing.Any
        ) -> ThirdPartyLinkHttpRequest: ...
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
    class TestsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            part: typing.Union[str, typing.List[str]],
            body: TestItem = ...,
            **kwargs: typing.Any
        ) -> TestItemHttpRequest: ...
    class ChannelBannersResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            body: ChannelBannerResource = ...,
            channelId: str = ...,
            onBehalfOfContentOwnerChannel: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> ChannelBannerResourceHttpRequest: ...
    def superChatEvents(self) -> SuperChatEventsResource: ...
    def i18nRegions(self) -> I18nRegionsResource: ...
    def playlistItems(self) -> PlaylistItemsResource: ...
    def watermarks(self) -> WatermarksResource: ...
    def membershipsLevels(self) -> MembershipsLevelsResource: ...
    def search(self) -> SearchResource: ...
    def videoCategories(self) -> VideoCategoriesResource: ...
    def activities(self) -> ActivitiesResource: ...
    def liveBroadcasts(self) -> LiveBroadcastsResource: ...
    def i18nLanguages(self) -> I18nLanguagesResource: ...
    def liveChatModerators(self) -> LiveChatModeratorsResource: ...
    def captions(self) -> CaptionsResource: ...
    def channelSections(self) -> ChannelSectionsResource: ...
    def members(self) -> MembersResource: ...
    def playlists(self) -> PlaylistsResource: ...
    def liveChatMessages(self) -> LiveChatMessagesResource: ...
    def thumbnails(self) -> ThumbnailsResource: ...
    def videos(self) -> VideosResource: ...
    def liveStreams(self) -> LiveStreamsResource: ...
    def commentThreads(self) -> CommentThreadsResource: ...
    def videoAbuseReportReasons(self) -> VideoAbuseReportReasonsResource: ...
    def sponsors(self) -> SponsorsResource: ...
    def comments(self) -> CommentsResource: ...
    def abuseReports(self) -> AbuseReportsResource: ...
    def liveChatBans(self) -> LiveChatBansResource: ...
    def subscriptions(self) -> SubscriptionsResource: ...
    def channels(self) -> ChannelsResource: ...
    def thirdPartyLinks(self) -> ThirdPartyLinksResource: ...
    def tests(self) -> TestsResource: ...
    def channelBanners(self) -> ChannelBannersResource: ...

class I18nRegionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> I18nRegionListResponse: ...

class ThirdPartyLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ThirdPartyLink: ...

class SearchListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchListResponse: ...

class VideoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Video: ...

class VideoCategoryListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VideoCategoryListResponse: ...

class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Channel: ...

class LiveChatModeratorListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiveChatModeratorListResponse: ...

class MembershipsLevelListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MembershipsLevelListResponse: ...

class CommentListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CommentListResponse: ...

class ChannelListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ChannelListResponse: ...

class LiveBroadcastHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiveBroadcast: ...

class LiveStreamListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiveStreamListResponse: ...

class CaptionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CaptionListResponse: ...

class LiveStreamHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiveStream: ...

class MemberListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MemberListResponse: ...

class SubscriptionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SubscriptionListResponse: ...

class I18nLanguageListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> I18nLanguageListResponse: ...

class CommentThreadHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CommentThread: ...

class ActivityListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ActivityListResponse: ...

class LiveBroadcastListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiveBroadcastListResponse: ...

class LiveChatModeratorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiveChatModerator: ...

class ChannelSectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ChannelSection: ...

class SponsorListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SponsorListResponse: ...

class PlaylistListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlaylistListResponse: ...

class ChannelBannerResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ChannelBannerResource: ...

class LiveChatMessageListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiveChatMessageListResponse: ...

class ChannelSectionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ChannelSectionListResponse: ...

class AbuseReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AbuseReport: ...

class VideoRatingListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VideoRatingListResponse: ...

class CaptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Caption: ...

class CommentThreadListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CommentThreadListResponse: ...

class VideoAbuseReportReasonListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VideoAbuseReportReasonListResponse: ...

class LiveChatBanHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiveChatBan: ...

class CommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Comment: ...

class TestItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestItem: ...

class VideoListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VideoListResponse: ...

class PlaylistItemListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlaylistItemListResponse: ...

class PlaylistHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Playlist: ...

class LiveChatMessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiveChatMessage: ...

class PlaylistItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlaylistItem: ...

class ThumbnailSetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ThumbnailSetResponse: ...

class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Subscription: ...

class SuperChatEventListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SuperChatEventListResponse: ...
