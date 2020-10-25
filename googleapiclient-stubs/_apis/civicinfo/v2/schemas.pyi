import typing

import typing_extensions
@typing.type_check_only
class AdministrationRegion(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class AdministrativeBody(typing_extensions.TypedDict, total=False):
    absenteeVotingInfoUrl: str
    ballotInfoUrl: str
    correspondenceAddress: SimpleAddressType
    electionInfoUrl: str
    electionNoticeText: str
    electionNoticeUrl: str
    electionOfficials: typing.List[ElectionOfficial]
    electionRegistrationConfirmationUrl: str
    electionRegistrationUrl: str
    electionRulesUrl: str
    hoursOfOperation: str
    name: str
    physicalAddress: SimpleAddressType
    voter_services: typing.List[str]
    votingLocationFinderUrl: str

@typing.type_check_only
class Candidate(typing_extensions.TypedDict, total=False):
    candidateUrl: str
    channels: typing.List[Channel]
    email: str
    name: str
    orderOnBallot: str
    party: str
    phone: str
    photoUrl: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    id: str
    type: str

@typing.type_check_only
class Contest(typing_extensions.TypedDict, total=False):
    ballotPlacement: str
    ballotTitle: str
    candidates: typing.List[Candidate]
    district: ElectoralDistrict
    electorateSpecifications: str
    level: typing.List[str]
    numberElected: str
    numberVotingFor: str
    office: str
    primaryParties: typing.List[str]
    primaryParty: str
    referendumBallotResponses: typing.List[str]
    referendumBrief: str
    referendumConStatement: str
    referendumEffectOfAbstain: str
    referendumPassageThreshold: str
    referendumProStatement: str
    referendumSubtitle: str
    referendumText: str
    referendumTitle: str
    referendumUrl: str
    roles: typing.List[str]
    sources: typing.List[Source]
    special: str
    type: str

@typing.type_check_only
class DivisionSearchResponse(typing_extensions.TypedDict, total=False):
    kind: str
    results: typing.List[DivisionSearchResult]

@typing.type_check_only
class DivisionSearchResult(typing_extensions.TypedDict, total=False):
    aliases: typing.List[str]
    name: str
    ocdId: str

@typing.type_check_only
class Election(typing_extensions.TypedDict, total=False):
    electionDay: str
    id: str
    name: str
    ocdDivisionId: str

@typing.type_check_only
class ElectionOfficial(typing_extensions.TypedDict, total=False):
    emailAddress: str
    faxNumber: str
    name: str
    officePhoneNumber: str
    title: str

@typing.type_check_only
class ElectionsQueryResponse(typing_extensions.TypedDict, total=False):
    elections: typing.List[Election]
    kind: str

@typing.type_check_only
class ElectoralDistrict(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    scope: typing_extensions.Literal[
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
class GeographicDivision(typing_extensions.TypedDict, total=False):
    alsoKnownAs: typing.List[str]
    name: str
    officeIndices: typing.List[int]

@typing.type_check_only
class Office(typing_extensions.TypedDict, total=False):
    divisionId: str
    levels: typing.List[str]
    name: str
    officialIndices: typing.List[int]
    roles: typing.List[str]
    sources: typing.List[Source]

@typing.type_check_only
class Official(typing_extensions.TypedDict, total=False):
    address: typing.List[SimpleAddressType]
    channels: typing.List[Channel]
    emails: typing.List[str]
    name: str
    party: str
    phones: typing.List[str]
    photoUrl: str
    urls: typing.List[str]

@typing.type_check_only
class PollingLocation(typing_extensions.TypedDict, total=False):
    address: SimpleAddressType
    endDate: str
    latitude: float
    longitude: float
    name: str
    notes: str
    pollingHours: str
    sources: typing.List[Source]
    startDate: str
    voterServices: str

@typing.type_check_only
class RepresentativeInfoData(typing_extensions.TypedDict, total=False):
    divisions: typing.Dict[str, typing.Any]
    offices: typing.List[Office]
    officials: typing.List[Official]

@typing.type_check_only
class RepresentativeInfoResponse(typing_extensions.TypedDict, total=False):
    divisions: typing.Dict[str, typing.Any]
    kind: str
    normalizedInput: SimpleAddressType
    offices: typing.List[Office]
    officials: typing.List[Official]

@typing.type_check_only
class SimpleAddressType(typing_extensions.TypedDict, total=False):
    city: str
    line1: str
    line2: str
    line3: str
    locationName: str
    state: str
    zip: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    name: str
    official: bool

@typing.type_check_only
class VoterInfoResponse(typing_extensions.TypedDict, total=False):
    contests: typing.List[Contest]
    dropOffLocations: typing.List[PollingLocation]
    earlyVoteSites: typing.List[PollingLocation]
    election: Election
    kind: str
    mailOnly: bool
    normalizedInput: SimpleAddressType
    otherElections: typing.List[Election]
    pollingLocations: typing.List[PollingLocation]
    precinctId: str
    state: typing.List[AdministrationRegion]
