import typing

_list = list

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1Claim(typing.TypedDict, total=False):
    claimDate: str
    claimReview: _list[GoogleFactcheckingFactchecktoolsV1alpha1ClaimReview]
    claimant: str
    text: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthor(
    typing.TypedDict, total=False
):
    imageUrl: str
    jobTitle: str
    name: str
    sameAs: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimRating(
    typing.TypedDict, total=False
):
    bestRating: int
    imageUrl: str
    ratingExplanation: str
    ratingValue: int
    textualRating: str
    worstRating: int

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReview(
    typing.TypedDict, total=False
):
    languageCode: str
    publisher: GoogleFactcheckingFactchecktoolsV1alpha1Publisher
    reviewDate: str
    textualRating: str
    title: str
    url: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthor(
    typing.TypedDict, total=False
):
    imageUrl: str
    name: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkup(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    claimReviewAuthor: GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthor
    claimReviewMarkups: _list[GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkup]
    name: str
    pageUrl: str
    publishDate: str
    versionId: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimImageSearchResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    results: _list[
        GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimImageSearchResponseResult
    ]

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimImageSearchResponseResult(
    typing.TypedDict, total=False
):
    claim: GoogleFactcheckingFactchecktoolsV1alpha1Claim

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse(
    typing.TypedDict, total=False
):
    claims: _list[GoogleFactcheckingFactchecktoolsV1alpha1Claim]
    nextPageToken: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponse(
    typing.TypedDict, total=False
):
    claimReviewMarkupPages: _list[
        GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1Publisher(typing.TypedDict, total=False):
    name: str
    site: str

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...
