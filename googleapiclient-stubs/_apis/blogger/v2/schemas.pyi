import typing

import typing_extensions

class BlogPerUserInfo(typing_extensions.TypedDict, total=False):
    userId: str
    kind: str
    hasAdminAccess: bool
    blogId: str
    photosAlbumKey: str
    role: typing_extensions.Literal[
        "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
    ]

class Blog(typing_extensions.TypedDict, total=False):
    description: str
    pages: typing.Dict[str, typing.Any]
    id: str
    selfLink: str
    posts: typing.Dict[str, typing.Any]
    url: str
    kind: str
    updated: str
    locale: typing.Dict[str, typing.Any]
    customMetaData: str
    status: typing_extensions.Literal["LIVE", "DELETED"]
    published: str
    name: str

class Page(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    status: typing_extensions.Literal["LIVE", "DRAFT"]
    url: str
    content: str
    updated: str
    published: str
    selfLink: str
    blog: typing.Dict[str, typing.Any]
    id: str
    author: typing.Dict[str, typing.Any]
    title: str

class PageList(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    items: typing.List[Page]

class Comment(typing_extensions.TypedDict, total=False):
    kind: str
    status: typing_extensions.Literal["LIVE", "EMPTIED", "PENDING", "SPAM"]
    selfLink: str
    content: str
    id: str
    inReplyTo: typing.Dict[str, typing.Any]
    published: str
    post: typing.Dict[str, typing.Any]
    updated: str
    author: typing.Dict[str, typing.Any]
    blog: typing.Dict[str, typing.Any]

class BlogUserInfo(typing_extensions.TypedDict, total=False):
    kind: str
    blog_user_info: BlogPerUserInfo
    blog: Blog

class PostList(typing_extensions.TypedDict, total=False):
    prevPageToken: str
    kind: str
    nextPageToken: str
    etag: str
    items: typing.List[Post]

class BlogList(typing_extensions.TypedDict, total=False):
    blogUserInfos: typing.List[BlogUserInfo]
    kind: str
    items: typing.List[Blog]

class Post(typing_extensions.TypedDict, total=False):
    published: str
    blog: typing.Dict[str, typing.Any]
    labels: typing.List[str]
    titleLink: str
    images: typing.List[typing.Dict[str, typing.Any]]
    customMetaData: str
    selfLink: str
    status: typing_extensions.Literal["LIVE", "DRAFT", "SCHEDULED"]
    replies: typing.Dict[str, typing.Any]
    url: str
    content: str
    author: typing.Dict[str, typing.Any]
    kind: str
    readerComments: typing_extensions.Literal[
        "ALLOW", "DONT_ALLOW_SHOW_EXISTING", "DONT_ALLOW_HIDE_EXISTING"
    ]
    title: str
    updated: str
    etag: str
    location: typing.Dict[str, typing.Any]
    id: str

class User(typing_extensions.TypedDict, total=False):
    locale: typing.Dict[str, typing.Any]
    about: str
    url: str
    kind: str
    selfLink: str
    id: str
    blogs: typing.Dict[str, typing.Any]
    created: str
    displayName: str

class CommentList(typing_extensions.TypedDict, total=False):
    etag: str
    prevPageToken: str
    kind: str
    nextPageToken: str
    items: typing.List[Comment]
