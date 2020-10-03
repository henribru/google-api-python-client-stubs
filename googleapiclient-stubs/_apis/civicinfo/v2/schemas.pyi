import typing

import typing_extensions

class DivisionSearchResult(typing_extensions.TypedDict, total=False):
    ocdId: str
    name: str
    aliases: typing.List[str]

class AdministrativeBody(typing_extensions.TypedDict, total=False):
    physicalAddress: SimpleAddressType
    electionNoticeText: str
    electionInfoUrl: str
    electionRulesUrl: str
    name: str
    hoursOfOperation: str
    electionNoticeUrl: str
    absenteeVotingInfoUrl: str
    electionOfficials: typing.List[ElectionOfficial]
    voter_services: typing.List[str]
    electionRegistrationConfirmationUrl: str
    electionRegistrationUrl: str
    votingLocationFinderUrl: str
    correspondenceAddress: SimpleAddressType
    ballotInfoUrl: str

class Official(typing_extensions.TypedDict, total=False):
    party: str
    photoUrl: str
    channels: typing.List[Channel]
    address: typing.List[SimpleAddressType]
    urls: typing.List[str]
    emails: typing.List[str]
    phones: typing.List[str]
    name: str

class ElectionOfficial(typing_extensions.TypedDict, total=False):
    officePhoneNumber: str
    faxNumber: str
    emailAddress: str
    name: str
    title: str

class RepresentativeInfoResponse(typing_extensions.TypedDict, total=False):
    normalizedInput: SimpleAddressType
    kind: str
    divisions: typing.Dict[str, typing.Any]
    offices: typing.List[Office]
    officials: typing.List[Official]

class Contest(typing_extensions.TypedDict, total=False):
    level: typing.List[str]
    referendumEffectOfAbstain: str
    referendumProStatement: str
    referendumUrl: str
    referendumPassageThreshold: str
    referendumConStatement: str
    district: ElectoralDistrict
    referendumSubtitle: str
    referendumBrief: str
    roles: typing.List[str]
    ballotPlacement: str
    special: str
    office: str
    type: str
    primaryParties: typing.List[str]
    numberElected: str
    referendumText: str
    id: str
    sources: typing.List[Source]
    referendumTitle: str
    numberVotingFor: str
    ballotTitle: str
    primaryParty: str
    electorateSpecifications: str
    referendumBallotResponses: typing.List[str]
    candidates: typing.List[Candidate]

class DivisionSearchResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[DivisionSearchResult]
    kind: str

class VoterInfoResponse(typing_extensions.TypedDict, total=False):
    contests: typing.List[Contest]
    dropOffLocations: typing.List[PollingLocation]
    pollingLocations: typing.List[PollingLocation]
    kind: str
    mailOnly: bool
    precinctId: str
    normalizedInput: SimpleAddressType
    otherElections: typing.List[Election]
    state: typing.List[AdministrationRegion]
    election: Election
    earlyVoteSites: typing.List[PollingLocation]

class Election(typing_extensions.TypedDict, total=False):
    ocdDivisionId: str
    name: str
    id: str
    electionDay: str

class RepresentativeInfoData(typing_extensions.TypedDict, total=False):
    divisions: typing.Dict[str, typing.Any]
    officials: typing.List[Official]
    offices: typing.List[Office]

class ElectionsQueryResponse(typing_extensions.TypedDict, total=False):
    elections: typing.List[Election]
    kind: str

class PollingLocation(typing_extensions.TypedDict, total=False):
    name: str
    notes: str
    sources: typing.List[Source]
    id: str
    pollingHours: str
    startDate: str
    latitude: float
    address: SimpleAddressType
    endDate: str
    longitude: float
    voterServices: str

class Office(typing_extensions.TypedDict, total=False):
    levels: typing.List[str]
    officialIndices: typing.List[int]
    name: str
    sources: typing.List[Source]
    roles: typing.List[str]
    divisionId: str

class Candidate(typing_extensions.TypedDict, total=False):
    email: str
    photoUrl: str
    phone: str
    orderOnBallot: str
    name: str
    candidateUrl: str
    channels: typing.List[Channel]
    party: str

class SimpleAddressType(typing_extensions.TypedDict, total=False):
    line3: str
    line2: str
    zip: str
    locationName: str
    city: str
    line1: str
    state: str

class AdministrationRegion(typing.Dict[str, typing.Any]): ...

class Channel(typing_extensions.TypedDict, total=False):
    id: str
    type: str

class Source(typing_extensions.TypedDict, total=False):
    name: str
    official: bool

class GeographicDivision(typing_extensions.TypedDict, total=False):
    alsoKnownAs: typing.List[str]
    officeIndices: typing.List[int]
    name: str

class ElectoralDistrict(typing_extensions.TypedDict, total=False):
    id: str
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
    name: str
