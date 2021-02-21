import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class BloggerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BlogsResource(googleapiclient.discovery.Resource):
        def get(self, *, blogId: str, **kwargs: typing.Any) -> BlogHttpRequest: ...
        def list(self, *, userId: str, **kwargs: typing.Any) -> BlogListHttpRequest: ...
    @typing.type_check_only
    class CommentsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, blogId: str, postId: str, commentId: str, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def list(
            self,
            *,
            blogId: str,
            postId: str,
            fetchBodies: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            startDate: str = ...,
            **kwargs: typing.Any
        ) -> CommentListHttpRequest: ...
    @typing.type_check_only
    class PagesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, blogId: str, pageId: str, **kwargs: typing.Any
        ) -> PageHttpRequest: ...
        def list(
            self, *, blogId: str, fetchBodies: bool = ..., **kwargs: typing.Any
        ) -> PageListHttpRequest: ...
    @typing.type_check_only
    class PostsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, blogId: str, postId: str, **kwargs: typing.Any
        ) -> PostHttpRequest: ...
        def list(
            self,
            *,
            blogId: str,
            fetchBodies: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            startDate: str = ...,
            **kwargs: typing.Any
        ) -> PostListHttpRequest: ...
    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        def get(self, *, userId: str, **kwargs: typing.Any) -> UserHttpRequest: ...
    def blogs(self) -> BlogsResource: ...
    def comments(self) -> CommentsResource: ...
    def pages(self) -> PagesResource: ...
    def posts(self) -> PostsResource: ...
    def users(self) -> UsersResource: ...

@typing.type_check_only
class BlogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Blog: ...

@typing.type_check_only
class BlogListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BlogList: ...

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
class CommentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CommentList: ...

@typing.type_check_only
class PageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Page: ...

@typing.type_check_only
class PageListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PageList: ...

@typing.type_check_only
class PostHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Post: ...

@typing.type_check_only
class PostListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PostList: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> User: ...
