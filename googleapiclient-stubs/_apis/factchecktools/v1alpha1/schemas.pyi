import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1Claim(
    typing_extensions.TypedDict, total=False
):
    claimDate: str
    claimReview: _list[GoogleFactcheckingFactchecktoolsV1alpha1ClaimReview]
    claimant: str
    text: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthor(
    typing_extensions.TypedDict, total=False
):
    imageUrl: str
    jobTitle: str
    name: str
    sameAs: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimRating(
    typing_extensions.TypedDict, total=False
):
    bestRating: int
    imageUrl: str
    ratingExplanation: str
    ratingValue: int
    textualRating: str
    worstRating: int

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReview(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    publisher: GoogleFactcheckingFactchecktoolsV1alpha1Publisher
    reviewDate: str
    textualRating: str
    title: str
    url: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthor(
    typing_extensions.TypedDict, total=False
):
    imageUrl: str
    name: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkup(
    typing_extensions.TypedDict, total=False
):
    claimAppearances: _list[str]
    claimAuthor: GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthor
    claimDate: str
    claimFirstAppearance: str
    claimLocation: str
    claimReviewed: str
    rating: GoogleFactcheckingFactchecktoolsV1alpha1ClaimRating
    url: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage(
    typing_extensions.TypedDict, total=False
):
    claimReviewAuthor: GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthor
    claimReviewMarkups: _list[GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkup]
    name: str
    pageUrl: str
    publishDate: str
    versionId: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse(
    typing_extensions.TypedDict, total=False
):
    claims: _list[GoogleFactcheckingFactchecktoolsV1alpha1Claim]
    nextPageToken: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponse(
    typing_extensions.TypedDict, total=False
):
    claimReviewMarkupPages: _list[
        GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1Publisher(
    typing_extensions.TypedDict, total=False
):
    name: str
    site: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
