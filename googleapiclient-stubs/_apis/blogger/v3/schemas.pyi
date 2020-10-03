import typing

import typing_extensions

class User(typing_extensions.TypedDict, total=False):
    id: str
    url: str
    about: str
    selfLink: str
    locale: typing.Dict[str, typing.Any]
    created: str
    blogs: typing.Dict[str, typing.Any]
    kind: str
    displayName: str

class Comment(typing_extensions.TypedDict, total=False):
    content: str
    blog: typing.Dict[str, typing.Any]
    selfLink: str
    inReplyTo: typing.Dict[str, typing.Any]
    updated: str
    kind: str
    published: str
    id: str
    author: typing.Dict[str, typing.Any]
    status: typing_extensions.Literal["LIVE", "EMPTIED", "PENDING", "SPAM"]
    post: typing.Dict[str, typing.Any]

class PostUserInfosList(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    items: typing.List[PostUserInfo]

class Page(typing_extensions.TypedDict, total=False):
    selfLink: str
    status: typing_extensions.Literal["LIVE", "DRAFT"]
    url: str
    published: str
    title: str
    updated: str
    author: typing.Dict[str, typing.Any]
    etag: str
    kind: str
    blog: typing.Dict[str, typing.Any]
    content: str
    id: str

class Pageviews(typing_extensions.TypedDict, total=False):
    blogId: str
    kind: str
    counts: typing.List[typing.Dict[str, typing.Any]]

class PostUserInfo(typing_extensions.TypedDict, total=False):
    post_user_info: PostPerUserInfo
    post: Post
    kind: str

class Blog(typing_extensions.TypedDict, total=False):
    customMetaData: str
    kind: str
    pages: typing.Dict[str, typing.Any]
    updated: str
    published: str
    description: str
    url: str
    posts: typing.Dict[str, typing.Any]
    name: str
    status: typing_extensions.Literal["LIVE", "DELETED"]
    id: str
    selfLink: str
    locale: typing.Dict[str, typing.Any]

class BlogList(typing_extensions.TypedDict, total=False):
    items: typing.List[Blog]
    blogUserInfos: typing.List[BlogUserInfo]
    kind: str

class Post(typing_extensions.TypedDict, total=False):
    replies: typing.Dict[str, typing.Any]
    status: typing_extensions.Literal["LIVE", "DRAFT", "SCHEDULED"]
    selfLink: str
    images: typing.List[typing.Dict[str, typing.Any]]
    updated: str
    title: str
    published: str
    labels: typing.List[str]
    content: str
    readerComments: typing_extensions.Literal[
        "ALLOW", "DONT_ALLOW_SHOW_EXISTING", "DONT_ALLOW_HIDE_EXISTING"
    ]
    url: str
    etag: str
    blog: typing.Dict[str, typing.Any]
    author: typing.Dict[str, typing.Any]
    customMetaData: str
    kind: str
    location: typing.Dict[str, typing.Any]
    id: str
    titleLink: str

class BlogPerUserInfo(typing_extensions.TypedDict, total=False):
    kind: str
    blogId: str
    hasAdminAccess: bool
    role: typing_extensions.Literal[
        "VIEW_TYPE_UNSPECIFIED", "READER", "AUTHOR", "ADMIN"
    ]
    userId: str
    photosAlbumKey: str

class PostList(typing_extensions.TypedDict, total=False):
    items: typing.List[Post]
    nextPageToken: str
    kind: str
    etag: str
    prevPageToken: str

class BlogUserInfo(typing_extensions.TypedDict, total=False):
    blog: Blog
    blog_user_info: BlogPerUserInfo
    kind: str

class PostPerUserInfo(typing_extensions.TypedDict, total=False):
    hasEditAccess: bool
    kind: str
    postId: str
    blogId: str
    userId: str

class PageList(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    etag: str
    kind: str
    items: typing.List[Page]

class CommentList(typing_extensions.TypedDict, total=False):
    prevPageToken: str
    kind: str
    nextPageToken: str
    items: typing.List[Comment]
    etag: str
