import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdministrationRegion(dict[str, typing.Any]): ...

@typing.type_check_only
class AdministrativeBody(typing_extensions.TypedDict, total=False):
    absenteeVotingInfoUrl: str
    ballotInfoUrl: str
    correspondenceAddress: SimpleAddressType
    electionInfoUrl: str
    electionNoticeText: str
    electionNoticeUrl: str
    electionOfficials: _list[ElectionOfficial]
    electionRegistrationConfirmationUrl: str
    electionRegistrationUrl: str
    electionRulesUrl: str
    hoursOfOperation: str
    name: str
    physicalAddress: SimpleAddressType
    voter_services: _list[str]
    votingLocationFinderUrl: str

@typing.type_check_only
class Candidate(typing_extensions.TypedDict, total=False):
    candidateUrl: str
    channels: _list[Channel]
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
    candidates: _list[Candidate]
    district: ElectoralDistrict
    electorateSpecifications: str
    level: _list[str]
    numberElected: str
    numberVotingFor: str
    office: str
    primaryParties: _list[str]
    primaryParty: str
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
    roles: _list[str]
    sources: _list[Source]
    special: str
    type: str

@typing.type_check_only
class DivisionSearchResponse(typing_extensions.TypedDict, total=False):
    kind: str
    results: _list[DivisionSearchResult]

@typing.type_check_only
class DivisionSearchResult(typing_extensions.TypedDict, total=False):
    aliases: _list[str]
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
    elections: _list[Election]
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
    alsoKnownAs: _list[str]
    name: str
    officeIndices: _list[int]

@typing.type_check_only
class Office(typing_extensions.TypedDict, total=False):
    divisionId: str
    levels: _list[str]
    name: str
    officialIndices: _list[int]
    roles: _list[str]
    sources: _list[Source]

@typing.type_check_only
class Official(typing_extensions.TypedDict, total=False):
    address: _list[SimpleAddressType]
    channels: _list[Channel]
    emails: _list[str]
    name: str
    party: str
    phones: _list[str]
    photoUrl: str
    urls: _list[str]

@typing.type_check_only
class PollingLocation(typing_extensions.TypedDict, total=False):
    address: SimpleAddressType
    endDate: str
    latitude: float
    longitude: float
    name: str
    notes: str
    pollingHours: str
    sources: _list[Source]
    startDate: str
    voterServices: str

@typing.type_check_only
class RepresentativeInfoData(typing_extensions.TypedDict, total=False):
    divisions: dict[str, typing.Any]
    offices: _list[Office]
    officials: _list[Official]

@typing.type_check_only
class RepresentativeInfoResponse(typing_extensions.TypedDict, total=False):
    divisions: dict[str, typing.Any]
    kind: str
    normalizedInput: SimpleAddressType
    offices: _list[Office]
    officials: _list[Official]

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
    contests: _list[Contest]
    dropOffLocations: _list[PollingLocation]
    earlyVoteSites: _list[PollingLocation]
    election: Election
    kind: str
    mailOnly: bool
    normalizedInput: SimpleAddressType
    otherElections: _list[Election]
    pollingLocations: _list[PollingLocation]
    precinctId: str
    state: _list[AdministrationRegion]
