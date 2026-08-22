import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class YouTubeResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AbuseReportsResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, part: str | _list[str], body: AbuseReport, **kwargs: typing.Any
        ) -> AbuseReportHttpRequest: ...

    @typing.type_check_only
    class ActivitiesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: str | _list[str],
            channelId: str | None = ...,
            home: bool | None = ...,
            maxResults: int | None = ...,
            mine: bool | None = ...,
            pageToken: str | None = ...,
            publishedAfter: str | None = ...,
            publishedBefore: str | None = ...,
            regionCode: str | None = ...,
            **kwargs: typing.Any,
        ) -> ActivityListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ActivityListResponseHttpRequest,
            previous_response: ActivityListResponse,
        ) -> ActivityListResponseHttpRequest | None: ...

    @typing.type_check_only
    class CaptionsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str,
            onBehalfOf: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def download(
            self,
            *,
            id: str,
            onBehalfOf: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            tfmt: str | None = ...,
            tlang: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def download_media(
            self,
            *,
            id: str,
            onBehalfOf: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            tfmt: str | None = ...,
            tlang: str | None = ...,
            **kwargs: typing.Any,
        ) -> BytesHttpRequest: ...
        def insert(
            self,
            *,
            part: str | _list[str],
            body: Caption,
            onBehalfOf: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            sync: bool | None = ...,
            **kwargs: typing.Any,
        ) -> CaptionHttpRequest: ...
        def list(
            self,
            *,
            part: str | _list[str],
            videoId: str,
            id: str | _list[str] | None = ...,
            onBehalfOf: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> CaptionListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: str | _list[str],
            body: Caption,
            onBehalfOf: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            sync: bool | None = ...,
            **kwargs: typing.Any,
        ) -> CaptionHttpRequest: ...

    @typing.type_check_only
    class ChannelBannersResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            body: ChannelBannerResource,
            channelId: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            **kwargs: typing.Any,
        ) -> ChannelBannerResourceHttpRequest: ...

    @typing.type_check_only
    class ChannelSectionsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: str | _list[str],
            body: ChannelSection,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            **kwargs: typing.Any,
        ) -> ChannelSectionHttpRequest: ...
        def list(
            self,
            *,
            part: str | _list[str],
            channelId: str | None = ...,
            hl: str | None = ...,
            id: str | _list[str] | None = ...,
            mine: bool | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> ChannelSectionListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: str | _list[str],
            body: ChannelSection,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> ChannelSectionHttpRequest: ...

    @typing.type_check_only
    class ChannelsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: str | _list[str],
            categoryId: str | None = ...,
            forHandle: str | None = ...,
            forUsername: str | None = ...,
            hl: str | None = ...,
            id: str | _list[str] | None = ...,
            managedByMe: bool | None = ...,
            maxResults: int | None = ...,
            mine: bool | None = ...,
            mySubscribers: bool | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ChannelListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ChannelListResponseHttpRequest,
            previous_response: ChannelListResponse,
        ) -> ChannelListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            part: str | _list[str],
            body: Channel,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class CommentThreadsResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, part: str | _list[str], body: CommentThread, **kwargs: typing.Any
        ) -> CommentThreadHttpRequest: ...
        def list(
            self,
            *,
            part: str | _list[str],
            allThreadsRelatedToChannelId: str | None = ...,
            channelId: str | None = ...,
            id: str | _list[str] | None = ...,
            maxResults: int | None = ...,
            moderationStatus: typing.Literal[
                "published", "heldForReview", "likelySpam", "rejected"
            ]
            | None = ...,
            order: typing.Literal["orderUnspecified", "time", "relevance"] | None = ...,
            pageToken: str | None = ...,
            postId: str | None = ...,
            searchTerms: str | None = ...,
            textFormat: typing.Literal["textFormatUnspecified", "html", "plainText"]
            | None = ...,
            videoId: str | None = ...,
            **kwargs: typing.Any,
        ) -> CommentThreadListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: CommentThreadListResponseHttpRequest,
            previous_response: CommentThreadListResponse,
        ) -> CommentThreadListResponseHttpRequest | None: ...

    @typing.type_check_only
    class CommentsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self, *, part: str | _list[str], body: Comment, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def list(
            self,
            *,
            part: str | _list[str],
            id: str | _list[str] | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            parentId: str | None = ...,
            textFormat: typing.Literal["textFormatUnspecified", "html", "plainText"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> CommentListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: CommentListResponseHttpRequest,
            previous_response: CommentListResponse,
        ) -> CommentListResponseHttpRequest | None: ...
        def markAsSpam(
            self, *, id: str | _list[str], **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def setModerationStatus(
            self,
            *,
            id: str | _list[str],
            moderationStatus: typing.Literal[
                "published", "heldForReview", "likelySpam", "rejected"
            ],
            banAuthor: bool | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def update(
            self, *, part: str | _list[str], body: Comment, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...

    @typing.type_check_only
    class I18nLanguagesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, part: str | _list[str], hl: str | None = ..., **kwargs: typing.Any
        ) -> I18nLanguageListResponseHttpRequest: ...

    @typing.type_check_only
    class I18nRegionsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, part: str | _list[str], hl: str | None = ..., **kwargs: typing.Any
        ) -> I18nRegionListResponseHttpRequest: ...

    @typing.type_check_only
    class LiveBroadcastsResource(googleapiclient.discovery.Resource):
        def bind(
            self,
            *,
            id: str,
            part: str | _list[str],
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            streamId: str | None = ...,
            **kwargs: typing.Any,
        ) -> LiveBroadcastHttpRequest: ...
        def delete(
            self,
            *,
            id: str,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: str | _list[str],
            body: LiveBroadcast,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            **kwargs: typing.Any,
        ) -> LiveBroadcastHttpRequest: ...
        def insertCuepoint(
            self,
            *,
            body: Cuepoint,
            id: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            part: str | _list[str] | None = ...,
            **kwargs: typing.Any,
        ) -> CuepointHttpRequest: ...
        def list(
            self,
            *,
            part: str | _list[str],
            broadcastStatus: typing.Literal[
                "broadcastStatusFilterUnspecified",
                "all",
                "active",
                "upcoming",
                "completed",
            ]
            | None = ...,
            broadcastType: typing.Literal[
                "broadcastTypeFilterUnspecified", "all", "event", "persistent"
            ]
            | None = ...,
            id: str | _list[str] | None = ...,
            maxResults: int | None = ...,
            mine: bool | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> LiveBroadcastListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: LiveBroadcastListResponseHttpRequest,
            previous_response: LiveBroadcastListResponse,
        ) -> LiveBroadcastListResponseHttpRequest | None: ...
        def transition(
            self,
            *,
            broadcastStatus: typing.Literal[
                "statusUnspecified", "testing", "live", "complete"
            ],
            id: str,
            part: str | _list[str],
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            **kwargs: typing.Any,
        ) -> LiveBroadcastHttpRequest: ...
        def update(
            self,
            *,
            part: str | _list[str],
            body: LiveBroadcast,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            **kwargs: typing.Any,
        ) -> LiveBroadcastHttpRequest: ...

    @typing.type_check_only
    class LiveChatBansResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self, *, part: str | _list[str], body: LiveChatBan, **kwargs: typing.Any
        ) -> LiveChatBanHttpRequest: ...

    @typing.type_check_only
    class LiveChatMessagesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self, *, part: str | _list[str], body: LiveChatMessage, **kwargs: typing.Any
        ) -> LiveChatMessageHttpRequest: ...
        def list(
            self,
            *,
            liveChatId: str,
            part: str | _list[str],
            hl: str | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            profileImageSize: int | None = ...,
            **kwargs: typing.Any,
        ) -> LiveChatMessageListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: LiveChatMessageListResponseHttpRequest,
            previous_response: LiveChatMessageListResponse,
        ) -> LiveChatMessageListResponseHttpRequest | None: ...
        def transition(
            self,
            *,
            id: str | None = ...,
            status: typing.Literal["statusUnspecified", "closed"] | None = ...,
            **kwargs: typing.Any,
        ) -> LiveChatMessageHttpRequest: ...

    @typing.type_check_only
    class LiveChatModeratorsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: str | _list[str],
            body: LiveChatModerator,
            **kwargs: typing.Any,
        ) -> LiveChatModeratorHttpRequest: ...
        def list(
            self,
            *,
            liveChatId: str,
            part: str | _list[str],
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> LiveChatModeratorListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: LiveChatModeratorListResponseHttpRequest,
            previous_response: LiveChatModeratorListResponse,
        ) -> LiveChatModeratorListResponseHttpRequest | None: ...

    @typing.type_check_only
    class LiveStreamsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: str | _list[str],
            body: LiveStream,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            **kwargs: typing.Any,
        ) -> LiveStreamHttpRequest: ...
        def list(
            self,
            *,
            part: str | _list[str],
            id: str | _list[str] | None = ...,
            maxResults: int | None = ...,
            mine: bool | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> LiveStreamListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: LiveStreamListResponseHttpRequest,
            previous_response: LiveStreamListResponse,
        ) -> LiveStreamListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            part: str | _list[str],
            body: LiveStream,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            **kwargs: typing.Any,
        ) -> LiveStreamHttpRequest: ...

    @typing.type_check_only
    class MembersResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: str | _list[str],
            filterByMemberChannelId: str | None = ...,
            hasAccessToLevel: str | None = ...,
            maxResults: int | None = ...,
            mode: typing.Literal["listMembersModeUnknown", "updates", "all_current"]
            | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> MemberListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: MemberListResponseHttpRequest,
            previous_response: MemberListResponse,
        ) -> MemberListResponseHttpRequest | None: ...

    @typing.type_check_only
    class MembershipsLevelsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, part: str | _list[str], **kwargs: typing.Any
        ) -> MembershipsLevelListResponseHttpRequest: ...

    @typing.type_check_only
    class PlaylistImagesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            body: PlaylistImage,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            part: str | _list[str] | None = ...,
            **kwargs: typing.Any,
        ) -> PlaylistImageHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            pageToken: str | None = ...,
            parent: str | None = ...,
            part: str | _list[str] | None = ...,
            **kwargs: typing.Any,
        ) -> PlaylistImageListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: PlaylistImageListResponseHttpRequest,
            previous_response: PlaylistImageListResponse,
        ) -> PlaylistImageListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            body: PlaylistImage,
            onBehalfOfContentOwner: str | None = ...,
            part: str | _list[str] | None = ...,
            **kwargs: typing.Any,
        ) -> PlaylistImageHttpRequest: ...

    @typing.type_check_only
    class PlaylistItemsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: str | _list[str],
            body: PlaylistItem,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> PlaylistItemHttpRequest: ...
        def list(
            self,
            *,
            part: str | _list[str],
            id: str | _list[str] | None = ...,
            maxResults: int | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            pageToken: str | None = ...,
            playlistId: str | None = ...,
            videoId: str | None = ...,
            **kwargs: typing.Any,
        ) -> PlaylistItemListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: PlaylistItemListResponseHttpRequest,
            previous_response: PlaylistItemListResponse,
        ) -> PlaylistItemListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            part: str | _list[str],
            body: PlaylistItem,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> PlaylistItemHttpRequest: ...

    @typing.type_check_only
    class PlaylistsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: str | _list[str],
            body: Playlist,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            **kwargs: typing.Any,
        ) -> PlaylistHttpRequest: ...
        def list(
            self,
            *,
            part: str | _list[str],
            channelId: str | None = ...,
            hl: str | None = ...,
            id: str | _list[str] | None = ...,
            maxResults: int | None = ...,
            mine: bool | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> PlaylistListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: PlaylistListResponseHttpRequest,
            previous_response: PlaylistListResponse,
        ) -> PlaylistListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            part: str | _list[str],
            body: Playlist,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> PlaylistHttpRequest: ...

    @typing.type_check_only
    class SearchResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: str | _list[str],
            channelId: str | None = ...,
            channelType: typing.Literal["channelTypeUnspecified", "any", "show"]
            | None = ...,
            eventType: typing.Literal["none", "upcoming", "live", "completed"]
            | None = ...,
            forContentOwner: bool | None = ...,
            forDeveloper: bool | None = ...,
            forMine: bool | None = ...,
            location: str | None = ...,
            locationRadius: str | None = ...,
            maxResults: int | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            order: typing.Literal[
                "searchSortUnspecified",
                "date",
                "rating",
                "viewCount",
                "relevance",
                "title",
                "videoCount",
            ]
            | None = ...,
            pageToken: str | None = ...,
            publishedAfter: str | None = ...,
            publishedBefore: str | None = ...,
            q: str | None = ...,
            regionCode: str | None = ...,
            relevanceLanguage: str | None = ...,
            safeSearch: typing.Literal[
                "safeSearchSettingUnspecified", "none", "moderate", "strict"
            ]
            | None = ...,
            topicId: str | None = ...,
            type: str | _list[str] | None = ...,
            videoCaption: typing.Literal[
                "videoCaptionUnspecified", "any", "closedCaption", "none"
            ]
            | None = ...,
            videoCategoryId: str | None = ...,
            videoDefinition: typing.Literal["any", "standard", "high"] | None = ...,
            videoDimension: typing.Literal["any", "2d", "3d"] | None = ...,
            videoDuration: typing.Literal[
                "videoDurationUnspecified", "any", "short", "medium", "long"
            ]
            | None = ...,
            videoEmbeddable: typing.Literal["videoEmbeddableUnspecified", "any", "true"]
            | None = ...,
            videoLicense: typing.Literal["any", "youtube", "creativeCommon"]
            | None = ...,
            videoPaidProductPlacement: typing.Literal[
                "videoPaidProductPlacementUnspecified", "any", "true"
            ]
            | None = ...,
            videoSyndicated: typing.Literal["videoSyndicatedUnspecified", "any", "true"]
            | None = ...,
            videoType: typing.Literal["videoTypeUnspecified", "any", "movie", "episode"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> SearchListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: SearchListResponseHttpRequest,
            previous_response: SearchListResponse,
        ) -> SearchListResponseHttpRequest | None: ...

    @typing.type_check_only
    class SubscriptionsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self, *, part: str | _list[str], body: Subscription, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def list(
            self,
            *,
            part: str | _list[str],
            channelId: str | None = ...,
            forChannelId: str | None = ...,
            id: str | _list[str] | None = ...,
            maxResults: int | None = ...,
            mine: bool | None = ...,
            myRecentSubscribers: bool | None = ...,
            mySubscribers: bool | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            order: typing.Literal[
                "subscriptionOrderUnspecified", "relevance", "unread", "alphabetical"
            ]
            | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> SubscriptionListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: SubscriptionListResponseHttpRequest,
            previous_response: SubscriptionListResponse,
        ) -> SubscriptionListResponseHttpRequest | None: ...

    @typing.type_check_only
    class SuperChatEventsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: str | _list[str],
            hl: str | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> SuperChatEventListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: SuperChatEventListResponseHttpRequest,
            previous_response: SuperChatEventListResponse,
        ) -> SuperChatEventListResponseHttpRequest | None: ...

    @typing.type_check_only
    class TestsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            part: str | _list[str],
            body: TestItem,
            externalChannelId: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            **kwargs: typing.Any,
        ) -> TestItemHttpRequest: ...

    @typing.type_check_only
    class ThirdPartyLinksResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            linkingToken: str,
            type: typing.Literal[
                "linkUnspecified", "channelToStoreLink", "channelToAffiliateProgramLink"
            ],
            externalChannelId: str | None = ...,
            part: str | _list[str] | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            part: str | _list[str],
            body: ThirdPartyLink,
            externalChannelId: str | None = ...,
            **kwargs: typing.Any,
        ) -> ThirdPartyLinkHttpRequest: ...
        def list(
            self,
            *,
            part: str | _list[str],
            externalChannelId: str | None = ...,
            linkingToken: str | None = ...,
            type: typing.Literal[
                "linkUnspecified", "channelToStoreLink", "channelToAffiliateProgramLink"
            ]
            | None = ...,
            **kwargs: typing.Any,
        ) -> ThirdPartyLinkListResponseHttpRequest: ...
        def update(
            self,
            *,
            part: str | _list[str],
            body: ThirdPartyLink,
            externalChannelId: str | None = ...,
            **kwargs: typing.Any,
        ) -> ThirdPartyLinkHttpRequest: ...

    @typing.type_check_only
    class ThumbnailsResource(googleapiclient.discovery.Resource):
        def set(
            self,
            *,
            videoId: str,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> ThumbnailSetResponseHttpRequest: ...

    @typing.type_check_only
    class VideoAbuseReportReasonsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, part: str | _list[str], hl: str | None = ..., **kwargs: typing.Any
        ) -> VideoAbuseReportReasonListResponseHttpRequest: ...

    @typing.type_check_only
    class VideoCategoriesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            part: str | _list[str],
            hl: str | None = ...,
            id: str | _list[str] | None = ...,
            regionCode: str | None = ...,
            **kwargs: typing.Any,
        ) -> VideoCategoryListResponseHttpRequest: ...

    @typing.type_check_only
    class VideoTrainabilityResource(googleapiclient.discovery.Resource):
        def get(
            self, *, id: str | None = ..., **kwargs: typing.Any
        ) -> VideoTrainabilityHttpRequest: ...

    @typing.type_check_only
    class VideosResource(googleapiclient.discovery.Resource):
        def batchGetStats(
            self,
            *,
            id: str | _list[str] | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            part: str | _list[str] | None = ...,
            **kwargs: typing.Any,
        ) -> BatchGetStatsResponseHttpRequest: ...
        def delete(
            self,
            *,
            id: str,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def getRating(
            self,
            *,
            id: str | _list[str],
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> VideoGetRatingResponseHttpRequest: ...
        def insert(
            self,
            *,
            part: str | _list[str],
            body: Video,
            autoLevels: bool | None = ...,
            notifySubscribers: bool | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            onBehalfOfContentOwnerChannel: str | None = ...,
            stabilize: bool | None = ...,
            **kwargs: typing.Any,
        ) -> VideoHttpRequest: ...
        def list(
            self,
            *,
            part: str | _list[str],
            chart: typing.Literal["chartUnspecified", "mostPopular"] | None = ...,
            hl: str | None = ...,
            id: str | _list[str] | None = ...,
            locale: str | None = ...,
            maxHeight: int | None = ...,
            maxResults: int | None = ...,
            maxWidth: int | None = ...,
            myRating: typing.Literal["none", "like", "dislike"] | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            pageToken: str | None = ...,
            regionCode: str | None = ...,
            videoCategoryId: str | None = ...,
            **kwargs: typing.Any,
        ) -> VideoListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: VideoListResponseHttpRequest,
            previous_response: VideoListResponse,
        ) -> VideoListResponseHttpRequest | None: ...
        def rate(
            self,
            *,
            id: str,
            rating: typing.Literal["none", "like", "dislike"],
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def reportAbuse(
            self,
            *,
            body: VideoAbuseReport,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def update(
            self,
            *,
            part: str | _list[str],
            body: Video,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> VideoHttpRequest: ...

    @typing.type_check_only
    class WatermarksResource(googleapiclient.discovery.Resource):
        def set(
            self,
            *,
            channelId: str,
            body: InvideoBranding,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def unset(
            self,
            *,
            channelId: str,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class YoutubeResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class V3Resource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LiveChatResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class MessagesResource(googleapiclient.discovery.Resource):
                    def stream(
                        self,
                        *,
                        hl: str | None = ...,
                        liveChatId: str | None = ...,
                        maxResults: int | None = ...,
                        pageToken: str | None = ...,
                        part: str | _list[str] | None = ...,
                        profileImageSize: int | None = ...,
                        **kwargs: typing.Any,
                    ) -> LiveChatMessageListResponseHttpRequest: ...
                    def stream_next(
                        self,
                        previous_request: LiveChatMessageListResponseHttpRequest,
                        previous_response: LiveChatMessageListResponse,
                    ) -> LiveChatMessageListResponseHttpRequest | None: ...

                def messages(self) -> MessagesResource: ...

            def liveChat(self) -> LiveChatResource: ...

        def v3(self) -> V3Resource: ...

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
    def playlistImages(self) -> PlaylistImagesResource: ...
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
    def videoTrainability(self) -> VideoTrainabilityResource: ...
    def videos(self) -> VideosResource: ...
    def watermarks(self) -> WatermarksResource: ...
    def youtube(self) -> YoutubeResource: ...

@typing.type_check_only
class AbuseReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AbuseReport: ...

@typing.type_check_only
class ActivityListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ActivityListResponse: ...

@typing.type_check_only
class BatchGetStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchGetStatsResponse: ...

@typing.type_check_only
class CaptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Caption: ...

@typing.type_check_only
class CaptionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CaptionListResponse: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Channel: ...

@typing.type_check_only
class ChannelBannerResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ChannelBannerResource: ...

@typing.type_check_only
class ChannelListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ChannelListResponse: ...

@typing.type_check_only
class ChannelSectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ChannelSection: ...

@typing.type_check_only
class ChannelSectionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ChannelSectionListResponse: ...

@typing.type_check_only
class CommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Comment: ...

@typing.type_check_only
class CommentListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CommentListResponse: ...

@typing.type_check_only
class CommentThreadHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CommentThread: ...

@typing.type_check_only
class CommentThreadListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CommentThreadListResponse: ...

@typing.type_check_only
class CuepointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Cuepoint: ...

@typing.type_check_only
class I18nLanguageListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> I18nLanguageListResponse: ...

@typing.type_check_only
class I18nRegionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> I18nRegionListResponse: ...

@typing.type_check_only
class LiveBroadcastHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiveBroadcast: ...

@typing.type_check_only
class LiveBroadcastListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiveBroadcastListResponse: ...

@typing.type_check_only
class LiveChatBanHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiveChatBan: ...

@typing.type_check_only
class LiveChatMessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiveChatMessage: ...

@typing.type_check_only
class LiveChatMessageListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiveChatMessageListResponse: ...

@typing.type_check_only
class LiveChatModeratorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiveChatModerator: ...

@typing.type_check_only
class LiveChatModeratorListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiveChatModeratorListResponse: ...

@typing.type_check_only
class LiveStreamHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiveStream: ...

@typing.type_check_only
class LiveStreamListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiveStreamListResponse: ...

@typing.type_check_only
class MemberListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MemberListResponse: ...

@typing.type_check_only
class MembershipsLevelListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MembershipsLevelListResponse: ...

@typing.type_check_only
class PlaylistHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Playlist: ...

@typing.type_check_only
class PlaylistImageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlaylistImage: ...

@typing.type_check_only
class PlaylistImageListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlaylistImageListResponse: ...

@typing.type_check_only
class PlaylistItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlaylistItem: ...

@typing.type_check_only
class PlaylistItemListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlaylistItemListResponse: ...

@typing.type_check_only
class PlaylistListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlaylistListResponse: ...

@typing.type_check_only
class SearchListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchListResponse: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Subscription: ...

@typing.type_check_only
class SubscriptionListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SubscriptionListResponse: ...

@typing.type_check_only
class SuperChatEventListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SuperChatEventListResponse: ...

@typing.type_check_only
class TestItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestItem: ...

@typing.type_check_only
class ThirdPartyLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ThirdPartyLink: ...

@typing.type_check_only
class ThirdPartyLinkListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ThirdPartyLinkListResponse: ...

@typing.type_check_only
class ThumbnailSetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ThumbnailSetResponse: ...

@typing.type_check_only
class VideoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Video: ...

@typing.type_check_only
class VideoAbuseReportReasonListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VideoAbuseReportReasonListResponse: ...

@typing.type_check_only
class VideoCategoryListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VideoCategoryListResponse: ...

@typing.type_check_only
class VideoGetRatingResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VideoGetRatingResponse: ...

@typing.type_check_only
class VideoListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VideoListResponse: ...

@typing.type_check_only
class VideoTrainabilityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VideoTrainability: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> bytes: ...
