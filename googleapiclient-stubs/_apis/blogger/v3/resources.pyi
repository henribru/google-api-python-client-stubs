import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class BloggerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BlogUserInfosResource(googleapiclient.discovery.Resource):
        def get(
            self, *, userId: str, blogId: str, maxPosts: int = ..., **kwargs: typing.Any
        ) -> BlogUserInfoHttpRequest: ...

    @typing.type_check_only
    class BlogsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            blogId: str,
            maxPosts: int = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
        ) -> BlogHttpRequest: ...
        def getByUrl(
            self,
            *,
            url: str,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
        ) -> BlogHttpRequest: ...
        def listByUser(
            self,
            *,
            userId: str,
            fetchUserInfo: bool = ...,
            role: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ]
            | _list[
                typing_extensions.Literal[
                    "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
                ]
            ] = ...,
            status: typing_extensions.Literal["LIVE", "DELETED"]
            | _list[typing_extensions.Literal["LIVE", "DELETED"]] = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
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
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def list(
            self,
            *,
            blogId: str,
            postId: str,
            endDate: str = ...,
            fetchBodies: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            startDate: str = ...,
            status: typing_extensions.Literal[
                "LIVE", "EMPTIED", "PENDING", "SPAM"
            ] = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
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
            endDate: str = ...,
            fetchBodies: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            startDate: str = ...,
            status: typing_extensions.Literal["LIVE", "EMPTIED", "PENDING", "SPAM"]
            | _list[
                typing_extensions.Literal["LIVE", "EMPTIED", "PENDING", "SPAM"]
            ] = ...,
            **kwargs: typing.Any
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
            range: typing_extensions.Literal["all", "30DAYS", "7DAYS"]
            | _list[typing_extensions.Literal["all", "30DAYS", "7DAYS"]] = ...,
            **kwargs: typing.Any
        ) -> PageviewsHttpRequest: ...

    @typing.type_check_only
    class PagesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, blogId: str, pageId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            blogId: str,
            pageId: str,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
        ) -> PageHttpRequest: ...
        def insert(
            self,
            *,
            blogId: str,
            body: Page = ...,
            isDraft: bool = ...,
            **kwargs: typing.Any
        ) -> PageHttpRequest: ...
        def list(
            self,
            *,
            blogId: str,
            fetchBodies: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            status: typing_extensions.Literal["LIVE", "DRAFT", "SOFT_TRASHED"]
            | _list[typing_extensions.Literal["LIVE", "DRAFT", "SOFT_TRASHED"]] = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
        ) -> PageListHttpRequest: ...
        def list_next(
            self, previous_request: PageListHttpRequest, previous_response: PageList
        ) -> PageListHttpRequest | None: ...
        def patch(
            self,
            *,
            blogId: str,
            pageId: str,
            body: Page = ...,
            publish: bool = ...,
            revert: bool = ...,
            **kwargs: typing.Any
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
            body: Page = ...,
            publish: bool = ...,
            revert: bool = ...,
            **kwargs: typing.Any
        ) -> PageHttpRequest: ...

    @typing.type_check_only
    class PostUserInfosResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            userId: str,
            blogId: str,
            postId: str,
            maxComments: int = ...,
            **kwargs: typing.Any
        ) -> PostUserInfoHttpRequest: ...
        def list(
            self,
            *,
            userId: str,
            blogId: str,
            endDate: str = ...,
            fetchBodies: bool = ...,
            labels: str = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal[
                "ORDER_BY_UNSPECIFIED", "PUBLISHED", "UPDATED"
            ] = ...,
            pageToken: str = ...,
            startDate: str = ...,
            status: typing_extensions.Literal[
                "LIVE", "DRAFT", "SCHEDULED", "SOFT_TRASHED"
            ]
            | _list[
                typing_extensions.Literal["LIVE", "DRAFT", "SCHEDULED", "SOFT_TRASHED"]
            ] = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
        ) -> PostUserInfosListHttpRequest: ...
        def list_next(
            self,
            previous_request: PostUserInfosListHttpRequest,
            previous_response: PostUserInfosList,
        ) -> PostUserInfosListHttpRequest | None: ...

    @typing.type_check_only
    class PostsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, blogId: str, postId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            blogId: str,
            postId: str,
            fetchBody: bool = ...,
            fetchImages: bool = ...,
            maxComments: int = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def getByPath(
            self,
            *,
            blogId: str,
            path: str,
            maxComments: int = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def insert(
            self,
            *,
            blogId: str,
            body: Post = ...,
            fetchBody: bool = ...,
            fetchImages: bool = ...,
            isDraft: bool = ...,
            **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def list(
            self,
            *,
            blogId: str,
            endDate: str = ...,
            fetchBodies: bool = ...,
            fetchImages: bool = ...,
            labels: str = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal[
                "ORDER_BY_UNSPECIFIED", "PUBLISHED", "UPDATED"
            ] = ...,
            pageToken: str = ...,
            startDate: str = ...,
            status: typing_extensions.Literal[
                "LIVE", "DRAFT", "SCHEDULED", "SOFT_TRASHED"
            ]
            | _list[
                typing_extensions.Literal["LIVE", "DRAFT", "SCHEDULED", "SOFT_TRASHED"]
            ] = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
        ) -> PostListHttpRequest: ...
        def list_next(
            self, previous_request: PostListHttpRequest, previous_response: PostList
        ) -> PostListHttpRequest | None: ...
        def patch(
            self,
            *,
            blogId: str,
            postId: str,
            body: Post = ...,
            fetchBody: bool = ...,
            fetchImages: bool = ...,
            maxComments: int = ...,
            publish: bool = ...,
            revert: bool = ...,
            **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def publish(
            self,
            *,
            blogId: str,
            postId: str,
            publishDate: str = ...,
            **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def revert(
            self, *, blogId: str, postId: str, **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def search(
            self,
            *,
            blogId: str,
            q: str,
            fetchBodies: bool = ...,
            orderBy: typing_extensions.Literal[
                "ORDER_BY_UNSPECIFIED", "PUBLISHED", "UPDATED"
            ] = ...,
            **kwargs: typing.Any
        ) -> PostListHttpRequest: ...
        def update(
            self,
            *,
            blogId: str,
            postId: str,
            body: Post = ...,
            fetchBody: bool = ...,
            fetchImages: bool = ...,
            maxComments: int = ...,
            publish: bool = ...,
            revert: bool = ...,
            **kwargs: typing.Any
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
        | None = ...,
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
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Blog: ...

@typing.type_check_only
class BlogListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BlogList: ...

@typing.type_check_only
class BlogUserInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BlogUserInfo: ...

@typing.type_check_only
class CommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Comment: ...

@typing.type_check_only
class CommentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CommentList: ...

@typing.type_check_only
class PageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Page: ...

@typing.type_check_only
class PageListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PageList: ...

@typing.type_check_only
class PageviewsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Pageviews: ...

@typing.type_check_only
class PostHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Post: ...

@typing.type_check_only
class PostListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PostList: ...

@typing.type_check_only
class PostUserInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PostUserInfo: ...

@typing.type_check_only
class PostUserInfosListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PostUserInfosList: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> User: ...
