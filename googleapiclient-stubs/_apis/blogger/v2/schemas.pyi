import typing

import typing_extensions

_list = list

@typing.type_check_only
class Blog(typing_extensions.TypedDict, total=False):
    customMetaData: str
    description: str
    id: str
    kind: str
    locale: dict[str, typing.Any]
    name: str
    pages: dict[str, typing.Any]
    posts: dict[str, typing.Any]
    published: str
    selfLink: str
    status: typing_extensions.Literal["LIVE", "DELETED"]
    updated: str
    url: str

@typing.type_check_only
class BlogList(typing_extensions.TypedDict, total=False):
    blogUserInfos: _list[BlogUserInfo]
    items: _list[Blog]
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
    author: dict[str, typing.Any]
    blog: dict[str, typing.Any]
    content: str
    id: str
    inReplyTo: dict[str, typing.Any]
    kind: str
    post: dict[str, typing.Any]
    published: str
    selfLink: str
    status: typing_extensions.Literal["LIVE", "EMPTIED", "PENDING", "SPAM"]
    updated: str

@typing.type_check_only
class CommentList(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[Comment]
    kind: str
    nextPageToken: str
    prevPageToken: str

@typing.type_check_only
class Page(typing_extensions.TypedDict, total=False):
    author: dict[str, typing.Any]
    blog: dict[str, typing.Any]
    content: str
    etag: str
    id: str
    kind: str
    published: str
    selfLink: str
    status: typing_extensions.Literal["LIVE", "DRAFT", "SOFT_TRASHED"]
    title: str
    trashed: str
    updated: str
    url: str

@typing.type_check_only
class PageList(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[Page]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Post(typing_extensions.TypedDict, total=False):
    author: dict[str, typing.Any]
    blog: dict[str, typing.Any]
    content: str
    customMetaData: str
    etag: str
    id: str
    images: _list[dict[str, typing.Any]]
    kind: str
    labels: _list[str]
    location: dict[str, typing.Any]
    published: str
    readerComments: typing_extensions.Literal[
        "ALLOW", "DONT_ALLOW_SHOW_EXISTING", "DONT_ALLOW_HIDE_EXISTING"
    ]
    replies: dict[str, typing.Any]
    selfLink: str
    status: typing_extensions.Literal["LIVE", "DRAFT", "SCHEDULED", "SOFT_TRASHED"]
    title: str
    titleLink: str
    trashed: str
    updated: str
    url: str

@typing.type_check_only
class PostList(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[Post]
    kind: str
    nextPageToken: str
    prevPageToken: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    about: str
    blogs: dict[str, typing.Any]
    created: str
    displayName: str
    id: str
    kind: str
    locale: dict[str, typing.Any]
    selfLink: str
    url: str
