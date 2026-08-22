import typing

_list = list

@typing.type_check_only
class CivicinfoApiprotosV2DivisionByAddressResponse(typing.TypedDict, total=False):
    divisions: dict[str, typing.Any]
    normalizedInput: CivicinfoSchemaV2SimpleAddressType

@typing.type_check_only
class CivicinfoApiprotosV2DivisionSearchResponse(typing.TypedDict, total=False):
    kind: str
    results: _list[CivicinfoApiprotosV2DivisionSearchResult]

@typing.type_check_only
class CivicinfoApiprotosV2DivisionSearchResult(typing.TypedDict, total=False):
    aliases: _list[str]
    name: str
    ocdId: str

@typing.type_check_only
class CivicinfoApiprotosV2ElectionsQueryResponse(typing.TypedDict, total=False):
    elections: _list[CivicinfoSchemaV2Election]
    kind: str

@typing.type_check_only
class CivicinfoApiprotosV2VoterInfoResponse(typing.TypedDict, total=False):
    contests: _list[CivicinfoSchemaV2Contest]
    dropOffLocations: _list[CivicinfoSchemaV2PollingLocation]
    earlyVoteSites: _list[CivicinfoSchemaV2PollingLocation]
    election: CivicinfoSchemaV2Election
    kind: str
    mailOnly: bool
    normalizedInput: CivicinfoSchemaV2SimpleAddressType
    otherElections: _list[CivicinfoSchemaV2Election]
    pollingLocations: _list[CivicinfoSchemaV2PollingLocation]
    precinctId: str
    precincts: _list[CivicinfoSchemaV2Precinct]
    state: _list[CivicinfoSchemaV2AdministrationRegion]

@typing.type_check_only
class CivicinfoSchemaV2AdministrationRegion(typing.TypedDict, total=False):
    electionAdministrationBody: CivicinfoSchemaV2AdministrativeBody
    local_jurisdiction: CivicinfoSchemaV2AdministrationRegion
    name: str
    sources: _list[CivicinfoSchemaV2Source]

@typing.type_check_only
class CivicinfoSchemaV2AdministrativeBody(typing.TypedDict, total=False):
    absenteeVotingInfoUrl: str
    ballotInfoUrl: str
    correspondenceAddress: CivicinfoSchemaV2SimpleAddressType
    electionInfoUrl: str
    electionNoticeText: str
    electionNoticeUrl: str
    electionOfficials: _list[CivicinfoSchemaV2ElectionOfficial]
    electionRegistrationConfirmationUrl: str
    electionRegistrationUrl: str
    electionRulesUrl: str
    hoursOfOperation: str
    name: str
    physicalAddress: CivicinfoSchemaV2SimpleAddressType
    voter_services: _list[str]
    votingLocationFinderUrl: str

@typing.type_check_only
class CivicinfoSchemaV2Candidate(typing.TypedDict, total=False):
    candidateUrl: str
    channels: _list[CivicinfoSchemaV2Channel]
    email: str
    name: str
    orderOnBallot: str
    party: str
    phone: str
    photoUrl: str

@typing.type_check_only
class CivicinfoSchemaV2Channel(typing.TypedDict, total=False):
    id: str
    type: str

@typing.type_check_only
class CivicinfoSchemaV2Contest(typing.TypedDict, total=False):
    ballotPlacement: str
    ballotTitle: str
    candidates: _list[CivicinfoSchemaV2Candidate]
    district: CivicinfoSchemaV2ElectoralDistrict
    electorateSpecifications: str
    level: _list[
        typing.Literal[
            "international",
            "country",
            "administrativeArea1",
            "regional",
            "administrativeArea2",
            "locality",
            "subLocality1",
            "subLocality2",
            "special",
        ]
    ]
    numberElected: str
    numberVotingFor: str
    office: str
    primaryParties: _list[str]
    referendumBallotResponses: _list[str]
    referendumBrief: str
    referendumConStatement: str
    referendumEffectOfAbstain: str
    referendumPassageThreshold: str
    referendumProStatement: str
    referendumSubtitle: str
    referendumText: str
    referendumTitle: str
    referendumUrl: str
    roles: _list[
        typing.Literal[
            "headOfState",
            "headOfGovernment",
            "deputyHeadOfGovernment",
            "governmentOfficer",
            "executiveCouncil",
            "legislatorUpperBody",
            "legislatorLowerBody",
            "highestCourtJudge",
            "judge",
            "schoolBoard",
            "specialPurposeOfficer",
            "otherRole",
        ]
    ]
    sources: _list[CivicinfoSchemaV2Source]
    special: str
    type: str

@typing.type_check_only
class CivicinfoSchemaV2Election(typing.TypedDict, total=False):
    electionDay: str
    id: str
    name: str
    ocdDivisionId: str
    shapeLookupBehavior: typing.Literal[
        "shapeLookupDefault", "shapeLookupDisabled", "shapeLookupEnabled"
    ]

@typing.type_check_only
class CivicinfoSchemaV2ElectionOfficial(typing.TypedDict, total=False):
    emailAddress: str
    faxNumber: str
    name: str
    officePhoneNumber: str
    title: str

@typing.type_check_only
class CivicinfoSchemaV2ElectoralDistrict(typing.TypedDict, total=False):
    id: str
    name: str
    scope: typing.Literal[
        "statewide",
        "congressional",
        "stateUpper",
        "stateLower",
        "countywide",
        "judicial",
        "schoolBoard",
        "citywide",
        "special",
        "countyCouncil",
        "township",
        "ward",
        "cityCouncil",
        "national",
    ]

@typing.type_check_only
class CivicinfoSchemaV2GeographicDivision(typing.TypedDict, total=False):
    alsoKnownAs: _list[str]
    name: str
    officeIndices: _list[int]

@typing.type_check_only
class CivicinfoSchemaV2PollingLocation(typing.TypedDict, total=False):
    address: CivicinfoSchemaV2SimpleAddressType
    endDate: str
    latitude: float
    longitude: float
    name: str
    notes: str
    pollingHours: str
    sources: _list[CivicinfoSchemaV2Source]
    startDate: str
    voterServices: str

@typing.type_check_only
class CivicinfoSchemaV2Precinct(typing.TypedDict, total=False):
    administrationRegionId: str
    contestId: _list[str]
    datasetId: str
    earlyVoteSiteId: _list[str]
    electoralDistrictId: _list[str]
    id: str
    mailOnly: bool
    name: str
    number: str
    ocdId: _list[str]
    pollingLocationId: _list[str]
    spatialBoundaryId: _list[str]
    splitName: str
    ward: str

@typing.type_check_only
class CivicinfoSchemaV2SimpleAddressType(typing.TypedDict, total=False):
    addressLine: _list[str]
    city: str
    line1: str
    line2: str
    line3: str
    locationName: str
    state: str
    zip: str

@typing.type_check_only
class CivicinfoSchemaV2Source(typing.TypedDict, total=False):
    name: str
    official: bool
