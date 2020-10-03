import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class BloggerResource(googleapiclient.discovery.Resource):
    class PageViewsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            blogId: str,
            range: typing.Union[
                typing_extensions.Literal["all", "30DAYS", "7DAYS"],
                typing.List[typing_extensions.Literal["all", "30DAYS", "7DAYS"]],
            ] = ...,
            **kwargs: typing.Any
        ) -> PageviewsHttpRequest: ...
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
        def update(
            self,
            *,
            blogId: str,
            pageId: str,
            body: Page = ...,
            revert: bool = ...,
            publish: bool = ...,
            **kwargs: typing.Any
        ) -> PageHttpRequest: ...
        def list(
            self,
            *,
            blogId: str,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            fetchBodies: bool = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            status: typing.Union[
                typing_extensions.Literal["LIVE", "DRAFT"],
                typing.List[typing_extensions.Literal["LIVE", "DRAFT"]],
            ] = ...,
            **kwargs: typing.Any
        ) -> PageListHttpRequest: ...
        def publish(
            self, *, blogId: str, pageId: str, **kwargs: typing.Any
        ) -> PageHttpRequest: ...
        def revert(
            self, *, blogId: str, pageId: str, **kwargs: typing.Any
        ) -> PageHttpRequest: ...
        def insert(
            self,
            *,
            blogId: str,
            body: Page = ...,
            isDraft: bool = ...,
            **kwargs: typing.Any
        ) -> PageHttpRequest: ...
    class PostUserInfosResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            userId: str,
            blogId: str,
            status: typing.Union[
                typing_extensions.Literal["LIVE", "DRAFT", "SCHEDULED"],
                typing.List[typing_extensions.Literal["LIVE", "DRAFT", "SCHEDULED"]],
            ] = ...,
            fetchBodies: bool = ...,
            startDate: str = ...,
            endDate: str = ...,
            orderBy: typing_extensions.Literal[
                "ORDER_BY_UNSPECIFIED", "PUBLISHED", "UPDATED"
            ] = ...,
            pageToken: str = ...,
            labels: str = ...,
            maxResults: int = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
        ) -> PostUserInfosListHttpRequest: ...
        def get(
            self,
            *,
            userId: str,
            blogId: str,
            postId: str,
            maxComments: int = ...,
            **kwargs: typing.Any
        ) -> PostUserInfoHttpRequest: ...
    class CommentsResource(googleapiclient.discovery.Resource):
        def approve(
            self, *, blogId: str, postId: str, commentId: str, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def removeContent(
            self, *, blogId: str, postId: str, commentId: str, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def list(
            self,
            *,
            blogId: str,
            postId: str,
            maxResults: int = ...,
            endDate: str = ...,
            status: typing_extensions.Literal[
                "LIVE", "EMPTIED", "PENDING", "SPAM"
            ] = ...,
            startDate: str = ...,
            pageToken: str = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            fetchBodies: bool = ...,
            **kwargs: typing.Any
        ) -> CommentListHttpRequest: ...
        def delete(
            self, *, blogId: str, postId: str, commentId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def listByBlog(
            self,
            *,
            blogId: str,
            status: typing.Union[
                typing_extensions.Literal["LIVE", "EMPTIED", "PENDING", "SPAM"],
                typing.List[
                    typing_extensions.Literal["LIVE", "EMPTIED", "PENDING", "SPAM"]
                ],
            ] = ...,
            endDate: str = ...,
            startDate: str = ...,
            pageToken: str = ...,
            fetchBodies: bool = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> CommentListHttpRequest: ...
        def markAsSpam(
            self, *, blogId: str, postId: str, commentId: str, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
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
    class PostsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            blogId: str,
            fetchImages: bool = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            maxResults: int = ...,
            startDate: str = ...,
            endDate: str = ...,
            pageToken: str = ...,
            fetchBodies: bool = ...,
            orderBy: typing_extensions.Literal[
                "ORDER_BY_UNSPECIFIED", "PUBLISHED", "UPDATED"
            ] = ...,
            labels: str = ...,
            status: typing.Union[
                typing_extensions.Literal["LIVE", "DRAFT", "SCHEDULED"],
                typing.List[typing_extensions.Literal["LIVE", "DRAFT", "SCHEDULED"]],
            ] = ...,
            **kwargs: typing.Any
        ) -> PostListHttpRequest: ...
        def publish(
            self,
            *,
            blogId: str,
            postId: str,
            publishDate: str = ...,
            **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def delete(
            self, *, blogId: str, postId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def revert(
            self, *, blogId: str, postId: str, **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def update(
            self,
            *,
            blogId: str,
            postId: str,
            body: Post = ...,
            revert: bool = ...,
            fetchImages: bool = ...,
            maxComments: int = ...,
            fetchBody: bool = ...,
            publish: bool = ...,
            **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def insert(
            self,
            *,
            blogId: str,
            body: Post = ...,
            fetchImages: bool = ...,
            isDraft: bool = ...,
            fetchBody: bool = ...,
            **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def getByPath(
            self,
            *,
            blogId: str,
            path: str,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            maxComments: int = ...,
            **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def get(
            self,
            *,
            blogId: str,
            postId: str,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            fetchImages: bool = ...,
            maxComments: int = ...,
            fetchBody: bool = ...,
            **kwargs: typing.Any
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
        def patch(
            self,
            *,
            blogId: str,
            postId: str,
            body: Post = ...,
            publish: bool = ...,
            maxComments: int = ...,
            fetchBody: bool = ...,
            fetchImages: bool = ...,
            revert: bool = ...,
            **kwargs: typing.Any
        ) -> PostHttpRequest: ...
    class BlogUserInfosResource(googleapiclient.discovery.Resource):
        def get(
            self, *, userId: str, blogId: str, maxPosts: int = ..., **kwargs: typing.Any
        ) -> BlogUserInfoHttpRequest: ...
    class UsersResource(googleapiclient.discovery.Resource):
        def get(self, *, userId: str, **kwargs: typing.Any) -> UserHttpRequest: ...
    class BlogsResource(googleapiclient.discovery.Resource):
        def getByUrl(
            self,
            *,
            url: str,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            **kwargs: typing.Any
        ) -> BlogHttpRequest: ...
        def get(
            self,
            *,
            blogId: str,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            maxPosts: int = ...,
            **kwargs: typing.Any
        ) -> BlogHttpRequest: ...
        def listByUser(
            self,
            *,
            userId: str,
            role: typing.Union[
                typing_extensions.Literal[
                    "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
                ],
                typing.List[
                    typing_extensions.Literal[
                        "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
                    ]
                ],
            ] = ...,
            fetchUserInfo: bool = ...,
            view: typing_extensions.Literal[
                "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
            ] = ...,
            status: typing.Union[
                typing_extensions.Literal["LIVE", "DELETED"],
                typing.List[typing_extensions.Literal["LIVE", "DELETED"]],
            ] = ...,
            **kwargs: typing.Any
        ) -> BlogListHttpRequest: ...
    def pageViews(self) -> PageViewsResource: ...
    def pages(self) -> PagesResource: ...
    def postUserInfos(self) -> PostUserInfosResource: ...
    def comments(self) -> CommentsResource: ...
    def posts(self) -> PostsResource: ...
    def blogUserInfos(self) -> BlogUserInfosResource: ...
    def users(self) -> UsersResource: ...
    def blogs(self) -> BlogsResource: ...

class BlogListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BlogList: ...

class PageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Page: ...

class PostUserInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PostUserInfo: ...

class PostHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Post: ...

class PostListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PostList: ...

class PageviewsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Pageviews: ...

class PageListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PageList: ...

class CommentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CommentList: ...

class PostUserInfosListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PostUserInfosList: ...

class BlogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Blog: ...

class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> User: ...

class BlogUserInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BlogUserInfo: ...

class CommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Comment: ...
