import typing

import typing_extensions

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthor(
    typing_extensions.TypedDict, total=False
):
    imageUrl: str
    name: str

class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage(
    typing_extensions.TypedDict, total=False
):
    claimReviewAuthor: GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthor
    versionId: str
    publishDate: str
    pageUrl: str
    name: str
    claimReviewMarkups: typing.List[
        GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkup
    ]

class GoogleFactcheckingFactchecktoolsV1alpha1ClaimRating(
    typing_extensions.TypedDict, total=False
):
    ratingValue: int
    imageUrl: str
    bestRating: int
    ratingExplanation: str
    textualRating: str
    worstRating: int

class GoogleFactcheckingFactchecktoolsV1alpha1Publisher(
    typing_extensions.TypedDict, total=False
):
    site: str
    name: str

class GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthor(
    typing_extensions.TypedDict, total=False
):
    sameAs: str
    imageUrl: str
    name: str
    jobTitle: str

class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReview(
    typing_extensions.TypedDict, total=False
):
    textualRating: str
    title: str
    languageCode: str
    publisher: GoogleFactcheckingFactchecktoolsV1alpha1Publisher
    url: str
    reviewDate: str

class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkup(
    typing_extensions.TypedDict, total=False
):
    rating: GoogleFactcheckingFactchecktoolsV1alpha1ClaimRating
    claimFirstAppearance: str
    url: str
    claimDate: str
    claimAppearances: typing.List[str]
    claimLocation: str
    claimAuthor: GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthor
    claimReviewed: str

class GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    claimReviewMarkupPages: typing.List[
        GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage
    ]

class GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    claims: typing.List[GoogleFactcheckingFactchecktoolsV1alpha1Claim]

class GoogleFactcheckingFactchecktoolsV1alpha1Claim(
    typing_extensions.TypedDict, total=False
):
    text: str
    claimant: str
    claimReview: typing.List[GoogleFactcheckingFactchecktoolsV1alpha1ClaimReview]
    claimDate: str
