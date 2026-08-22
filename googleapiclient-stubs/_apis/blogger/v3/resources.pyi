import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class BloggerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BlogUserInfosResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            userId: str,
            blogId: str,
            maxPosts: int | None = ...,
            **kwargs: typing.Any,
        ) -> BlogUserInfoHttpRequest: ...

    @typing.type_check_only
    class BlogsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            blogId: str,
            maxPosts: int | None = ...,
            view: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> BlogHttpRequest: ...
        def getByUrl(
            self,
            *,
            url: str,
            view: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> BlogHttpRequest: ...
        def listByUser(
            self,
            *,
            userId: str,
            fetchUserInfo: bool | None = ...,
            role: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | _list[
                typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            ]
            | None = ...,
            status: typing.Literal["LIVE", "DELETED"]
            | _list[typing.Literal["LIVE", "DELETED"]]
            | None = ...,
            view: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> BlogListHttpRequest: ...

    @typing.type_check_only
    class CommentsResource(googleapiclient.discovery.Resource):
        def approve(
            self, *, blogId: str, postId: str, commentId: str, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def delete(
            self, *, blogId: str, postId: str, commentId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            blogId: str,
            postId: str,
            commentId: str,
            view: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> CommentHttpRequest: ...
        def list(
            self,
            *,
            blogId: str,
            postId: str,
            endDate: str | None = ...,
            fetchBodies: bool | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            startDate: str | None = ...,
            status: typing.Literal["LIVE", "EMPTIED", "PENDING", "SPAM"] | None = ...,
            view: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> CommentListHttpRequest: ...
        def list_next(
            self,
            previous_request: CommentListHttpRequest,
            previous_response: CommentList,
        ) -> CommentListHttpRequest | None: ...
        def listByBlog(
            self,
            *,
            blogId: str,
            endDate: str | None = ...,
            fetchBodies: bool | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            startDate: str | None = ...,
            status: typing.Literal["LIVE", "EMPTIED", "PENDING", "SPAM"]
            | _list[typing.Literal["LIVE", "EMPTIED", "PENDING", "SPAM"]]
            | None = ...,
            **kwargs: typing.Any,
        ) -> CommentListHttpRequest: ...
        def listByBlog_next(
            self,
            previous_request: CommentListHttpRequest,
            previous_response: CommentList,
        ) -> CommentListHttpRequest | None: ...
        def markAsSpam(
            self, *, blogId: str, postId: str, commentId: str, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def removeContent(
            self, *, blogId: str, postId: str, commentId: str, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...

    @typing.type_check_only
    class PageViewsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            blogId: str,
            range: typing.Literal["all", "30DAYS", "7DAYS"]
            | _list[typing.Literal["all", "30DAYS", "7DAYS"]]
            | None = ...,
            **kwargs: typing.Any,
        ) -> PageviewsHttpRequest: ...

    @typing.type_check_only
    class PagesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            blogId: str,
            pageId: str,
            useTrash: bool | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            blogId: str,
            pageId: str,
            view: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> PageHttpRequest: ...
        def insert(
            self,
            *,
            blogId: str,
            body: Page,
            isDraft: bool | None = ...,
            **kwargs: typing.Any,
        ) -> PageHttpRequest: ...
        def list(
            self,
            *,
            blogId: str,
            fetchBodies: bool | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            status: typing.Literal["LIVE", "DRAFT", "SOFT_TRASHED"]
            | _list[typing.Literal["LIVE", "DRAFT", "SOFT_TRASHED"]]
            | None = ...,
            view: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> PageListHttpRequest: ...
        def list_next(
            self, previous_request: PageListHttpRequest, previous_response: PageList
        ) -> PageListHttpRequest | None: ...
        def patch(
            self,
            *,
            blogId: str,
            pageId: str,
            body: Page,
            publish: bool | None = ...,
            revert: bool | None = ...,
            **kwargs: typing.Any,
        ) -> PageHttpRequest: ...
        def publish(
            self, *, blogId: str, pageId: str, **kwargs: typing.Any
        ) -> PageHttpRequest: ...
        def revert(
            self, *, blogId: str, pageId: str, **kwargs: typing.Any
        ) -> PageHttpRequest: ...
        def update(
            self,
            *,
            blogId: str,
            pageId: str,
            body: Page,
            publish: bool | None = ...,
            revert: bool | None = ...,
            **kwargs: typing.Any,
        ) -> PageHttpRequest: ...

    @typing.type_check_only
    class PostUserInfosResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            userId: str,
            blogId: str,
            postId: str,
            maxComments: int | None = ...,
            **kwargs: typing.Any,
        ) -> PostUserInfoHttpRequest: ...
        def list(
            self,
            *,
            userId: str,
            blogId: str,
            endDate: str | None = ...,
            fetchBodies: bool | None = ...,
            labels: str | None = ...,
            maxResults: int | None = ...,
            orderBy: typing.Literal["ORDER_BY_UNSPECIFIED", "PUBLISHED", "UPDATED"]
            | None = ...,
            pageToken: str | None = ...,
            startDate: str | None = ...,
            status: typing.Literal["LIVE", "DRAFT", "SCHEDULED", "SOFT_TRASHED"]
            | _list[typing.Literal["LIVE", "DRAFT", "SCHEDULED", "SOFT_TRASHED"]]
            | None = ...,
            view: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> PostUserInfosListHttpRequest: ...
        def list_next(
            self,
            previous_request: PostUserInfosListHttpRequest,
            previous_response: PostUserInfosList,
        ) -> PostUserInfosListHttpRequest | None: ...

    @typing.type_check_only
    class PostsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            blogId: str,
            postId: str,
            useTrash: bool | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            blogId: str,
            postId: str,
            fetchBody: bool | None = ...,
            fetchImages: bool | None = ...,
            maxComments: int | None = ...,
            view: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> PostHttpRequest: ...
        def getByPath(
            self,
            *,
            blogId: str,
            path: str,
            maxComments: int | None = ...,
            view: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> PostHttpRequest: ...
        def insert(
            self,
            *,
            blogId: str,
            body: Post,
            fetchBody: bool | None = ...,
            fetchImages: bool | None = ...,
            isDraft: bool | None = ...,
            **kwargs: typing.Any,
        ) -> PostHttpRequest: ...
        def list(
            self,
            *,
            blogId: str,
            endDate: str | None = ...,
            fetchBodies: bool | None = ...,
            fetchImages: bool | None = ...,
            labels: str | None = ...,
            maxResults: int | None = ...,
            orderBy: typing.Literal["ORDER_BY_UNSPECIFIED", "PUBLISHED", "UPDATED"]
            | None = ...,
            pageToken: str | None = ...,
            sortOption: typing.Literal[
                "SORT_OPTION_UNSPECIFIED", "DESCENDING", "ASCENDING"
            ]
            | None = ...,
            startDate: str | None = ...,
            status: typing.Literal["LIVE", "DRAFT", "SCHEDULED", "SOFT_TRASHED"]
            | _list[typing.Literal["LIVE", "DRAFT", "SCHEDULED", "SOFT_TRASHED"]]
            | None = ...,
            view: typing.Literal["VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> PostListHttpRequest: ...
        def list_next(
            self, previous_request: PostListHttpRequest, previous_response: PostList
        ) -> PostListHttpRequest | None: ...
        def patch(
            self,
            *,
            blogId: str,
            postId: str,
            body: Post,
            fetchBody: bool | None = ...,
            fetchImages: bool | None = ...,
            maxComments: int | None = ...,
            publish: bool | None = ...,
            revert: bool | None = ...,
            **kwargs: typing.Any,
        ) -> PostHttpRequest: ...
        def publish(
            self,
            *,
            blogId: str,
            postId: str,
            publishDate: str | None = ...,
            **kwargs: typing.Any,
        ) -> PostHttpRequest: ...
        def revert(
            self, *, blogId: str, postId: str, **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def search(
            self,
            *,
            blogId: str,
            q: str,
            fetchBodies: bool | None = ...,
            orderBy: typing.Literal["ORDER_BY_UNSPECIFIED", "PUBLISHED", "UPDATED"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> PostListHttpRequest: ...
        def update(
            self,
            *,
            blogId: str,
            postId: str,
            body: Post,
            fetchBody: bool | None = ...,
            fetchImages: bool | None = ...,
            maxComments: int | None = ...,
            publish: bool | None = ...,
            revert: bool | None = ...,
            **kwargs: typing.Any,
        ) -> PostHttpRequest: ...

    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        def get(self, *, userId: str, **kwargs: typing.Any) -> UserHttpRequest: ...

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
    def blogUserInfos(self) -> BlogUserInfosResource: ...
    def blogs(self) -> BlogsResource: ...
    def comments(self) -> CommentsResource: ...
    def pageViews(self) -> PageViewsResource: ...
    def pages(self) -> PagesResource: ...
    def postUserInfos(self) -> PostUserInfosResource: ...
    def posts(self) -> PostsResource: ...
    def users(self) -> UsersResource: ...

@typing.type_check_only
class BlogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Blog: ...

@typing.type_check_only
class BlogListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BlogList: ...

@typing.type_check_only
class BlogUserInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BlogUserInfo: ...

@typing.type_check_only
class CommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Comment: ...

@typing.type_check_only
class CommentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CommentList: ...

@typing.type_check_only
class PageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Page: ...

@typing.type_check_only
class PageListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PageList: ...

@typing.type_check_only
class PageviewsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Pageviews: ...

@typing.type_check_only
class PostHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Post: ...

@typing.type_check_only
class PostListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PostList: ...

@typing.type_check_only
class PostUserInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PostUserInfo: ...

@typing.type_check_only
class PostUserInfosListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PostUserInfosList: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> User: ...
