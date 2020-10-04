import typing

import typing_extensions
@typing.type_check_only
class Blog(typing_extensions.TypedDict, total=False):
    customMetaData: str
    description: str
    id: str
    kind: str
    locale: typing.Dict[str, typing.Any]
    name: str
    pages: typing.Dict[str, typing.Any]
    posts: typing.Dict[str, typing.Any]
    published: str
    selfLink: str
    status: typing_extensions.Literal["LIVE", "DELETED"]
    updated: str
    url: str

@typing.type_check_only
class BlogList(typing_extensions.TypedDict, total=False):
    blogUserInfos: typing.List[BlogUserInfo]
    items: typing.List[Blog]
    kind: str

@typing.type_check_only
class BlogPerUserInfo(typing_extensions.TypedDict, total=False):
    blogId: str
    hasAdminAccess: bool
    kind: str
    photosAlbumKey: str
    role: typing_extensions.Literal[
        "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
    ]
    userId: str

@typing.type_check_only
class BlogUserInfo(typing_extensions.TypedDict, total=False):
    blog: Blog
    blog_user_info: BlogPerUserInfo
    kind: str

@typing.type_check_only
class Comment(typing_extensions.TypedDict, total=False):
    author: typing.Dict[str, typing.Any]
    blog: typing.Dict[str, typing.Any]
    content: str
    id: str
    inReplyTo: typing.Dict[str, typing.Any]
    kind: str
    post: typing.Dict[str, typing.Any]
    published: str
    selfLink: str
    status: typing_extensions.Literal["LIVE", "EMPTIED", "PENDING", "SPAM"]
    updated: str

@typing.type_check_only
class CommentList(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Comment]
    kind: str
    nextPageToken: str
    prevPageToken: str

@typing.type_check_only
class Page(typing_extensions.TypedDict, total=False):
    author: typing.Dict[str, typing.Any]
    blog: typing.Dict[str, typing.Any]
    content: str
    etag: str
    id: str
    kind: str
    published: str
    selfLink: str
    status: typing_extensions.Literal["LIVE", "DRAFT"]
    title: str
    updated: str
    url: str

@typing.type_check_only
class PageList(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Page]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Post(typing_extensions.TypedDict, total=False):
    author: typing.Dict[str, typing.Any]
    blog: typing.Dict[str, typing.Any]
    content: str
    customMetaData: str
    etag: str
    id: str
    images: typing.List[typing.Dict[str, typing.Any]]
    kind: str
    labels: typing.List[str]
    location: typing.Dict[str, typing.Any]
    published: str
    readerComments: typing_extensions.Literal[
        "ALLOW", "DONT_ALLOW_SHOW_EXISTING", "DONT_ALLOW_HIDE_EXISTING"
    ]
    replies: typing.Dict[str, typing.Any]
    selfLink: str
    status: typing_extensions.Literal["LIVE", "DRAFT", "SCHEDULED"]
    title: str
    titleLink: str
    updated: str
    url: str

@typing.type_check_only
class PostList(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Post]
    kind: str
    nextPageToken: str
    prevPageToken: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    about: str
    blogs: typing.Dict[str, typing.Any]
    created: str
    displayName: str
    id: str
    kind: str
    locale: typing.Dict[str, typing.Any]
    selfLink: str
    url: str
