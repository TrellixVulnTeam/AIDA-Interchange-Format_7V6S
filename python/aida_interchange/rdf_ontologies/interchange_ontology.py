from rdflib import URIRef

# WARNING. This is a Generated File. Please do not edit.
# Please refer to the README at java/src/main/java/com/ncc/aif/ont2javagen for more information
# Last generated on: 01/21/2022 11:28:49
NAMESPACE = 'https://raw.githubusercontent.com/NextCenturyCorporation/AIDA-Interchange-Format/master/java/src/main/resources/com/ncc/aif/ontologies/InterchangeOntology#'

# Classes
ArgumentStatement = URIRef(NAMESPACE + 'ArgumentStatement')
Attribute = URIRef(NAMESPACE + 'Attribute')
AudioJustification = URIRef(NAMESPACE + 'AudioJustification')
BoundingBox = URIRef(NAMESPACE + 'BoundingBox')
Claim = URIRef(NAMESPACE + 'Claim')
ClaimComponent = URIRef(NAMESPACE + 'ClaimComponent')
ClusterMembership = URIRef(NAMESPACE + 'ClusterMembership')
CompoundJustification = URIRef(NAMESPACE + 'CompoundJustification')
Confidence = URIRef(NAMESPACE + 'Confidence')
Entity = URIRef(NAMESPACE + 'Entity')
EpistemicStatus = URIRef(NAMESPACE + 'EpistemicStatus')
Event = URIRef(NAMESPACE + 'Event')
Hypothesis = URIRef(NAMESPACE + 'Hypothesis')
ImageJustification = URIRef(NAMESPACE + 'ImageJustification')
Justification = URIRef(NAMESPACE + 'Justification')
JustificationTypes = URIRef(NAMESPACE + 'JustificationTypes')
KeyFrameVideoJustification = URIRef(NAMESPACE + 'KeyFrameVideoJustification')
LDCTime = URIRef(NAMESPACE + 'LDCTime')
LDCTimeComponent = URIRef(NAMESPACE + 'LDCTimeComponent')
LinkAssertion = URIRef(NAMESPACE + 'LinkAssertion')
MutualExclusion = URIRef(NAMESPACE + 'MutualExclusion')
MutualExclusionAlternative = URIRef(NAMESPACE + 'MutualExclusionAlternative')
PrivateData = URIRef(NAMESPACE + 'PrivateData')
Relation = URIRef(NAMESPACE + 'Relation')
SameAsCluster = URIRef(NAMESPACE + 'SameAsCluster')
Sentiment = URIRef(NAMESPACE + 'Sentiment')
ShotVideoJustification = URIRef(NAMESPACE + 'ShotVideoJustification')
Subgraph = URIRef(NAMESPACE + 'Subgraph')
System = URIRef(NAMESPACE + 'System')
TextJustification = URIRef(NAMESPACE + 'TextJustification')
TypeStatement = URIRef(NAMESPACE + 'TypeStatement')
VideoJustification = URIRef(NAMESPACE + 'VideoJustification')
VideoJustificationChannel = URIRef(NAMESPACE + 'VideoJustificationChannel')

# Individuals
EpistemicFalseCertain = URIRef(NAMESPACE + 'EpistemicFalseCertain')
EpistemicFalseUncertain = URIRef(NAMESPACE + 'EpistemicFalseUncertain')
EpistemicTrueCertain = URIRef(NAMESPACE + 'EpistemicTrueCertain')
EpistemicTrueUncertain = URIRef(NAMESPACE + 'EpistemicTrueUncertain')
EpistemicUnknown = URIRef(NAMESPACE + 'EpistemicUnknown')
Generic = URIRef(NAMESPACE + 'Generic')
Hedged = URIRef(NAMESPACE + 'Hedged')
Irrealis = URIRef(NAMESPACE + 'Irrealis')
Negated = URIRef(NAMESPACE + 'Negated')
SentimentMixed = URIRef(NAMESPACE + 'SentimentMixed')
SentimentNegative = URIRef(NAMESPACE + 'SentimentNegative')
SentimentNeutralUnknown = URIRef(NAMESPACE + 'SentimentNeutralUnknown')
SentimentPositive = URIRef(NAMESPACE + 'SentimentPositive')
VideoJustificationChannelBoth = URIRef(NAMESPACE + 'VideoJustificationChannelBoth')
VideoJustificationChannelPicture = URIRef(NAMESPACE + 'VideoJustificationChannelPicture')
VideoJustificationChannelSound = URIRef(NAMESPACE + 'VideoJustificationChannelSound')

# Properties
alternative = URIRef(NAMESPACE + 'alternative')
alternativeGraph = URIRef(NAMESPACE + 'alternativeGraph')
associatedKEs = URIRef(NAMESPACE + 'associatedKEs')
attributes = URIRef(NAMESPACE + 'attributes')
boundingBox = URIRef(NAMESPACE + 'boundingBox')
boundingBoxLowerRightX = URIRef(NAMESPACE + 'boundingBoxLowerRightX')
boundingBoxLowerRightY = URIRef(NAMESPACE + 'boundingBoxLowerRightY')
boundingBoxUpperLeftX = URIRef(NAMESPACE + 'boundingBoxUpperLeftX')
boundingBoxUpperLeftY = URIRef(NAMESPACE + 'boundingBoxUpperLeftY')
channel = URIRef(NAMESPACE + 'channel')
claimDateTime = URIRef(NAMESPACE + 'claimDateTime')
claimId = URIRef(NAMESPACE + 'claimId')
claimLocation = URIRef(NAMESPACE + 'claimLocation')
claimMedium = URIRef(NAMESPACE + 'claimMedium')
claimSemantics = URIRef(NAMESPACE + 'claimSemantics')
claimTemplate = URIRef(NAMESPACE + 'claimTemplate')
claimer = URIRef(NAMESPACE + 'claimer')
claimerAffiliation = URIRef(NAMESPACE + 'claimerAffiliation')
cluster = URIRef(NAMESPACE + 'cluster')
clusterMember = URIRef(NAMESPACE + 'clusterMember')
componentIdentity = URIRef(NAMESPACE + 'componentIdentity')
componentKE = URIRef(NAMESPACE + 'componentKE')
componentName = URIRef(NAMESPACE + 'componentName')
componentProvenance = URIRef(NAMESPACE + 'componentProvenance')
componentType = URIRef(NAMESPACE + 'componentType')
confidence = URIRef(NAMESPACE + 'confidence')
confidenceValue = URIRef(NAMESPACE + 'confidenceValue')
containedJustification = URIRef(NAMESPACE + 'containedJustification')
day = URIRef(NAMESPACE + 'day')
dependsOnHypothesis = URIRef(NAMESPACE + 'dependsOnHypothesis')
end = URIRef(NAMESPACE + 'end')
endOffsetInclusive = URIRef(NAMESPACE + 'endOffsetInclusive')
endTimestamp = URIRef(NAMESPACE + 'endTimestamp')
epistemic = URIRef(NAMESPACE + 'epistemic')
handle = URIRef(NAMESPACE + 'handle')
hasName = URIRef(NAMESPACE + 'hasName')
hypothesisContent = URIRef(NAMESPACE + 'hypothesisContent')
identicalClaims = URIRef(NAMESPACE + 'identicalClaims')
importance = URIRef(NAMESPACE + 'importance')
informativeJustification = URIRef(NAMESPACE + 'informativeJustification')
jsonContent = URIRef(NAMESPACE + 'jsonContent')
justifiedBy = URIRef(NAMESPACE + 'justifiedBy')
keyFrame = URIRef(NAMESPACE + 'keyFrame')
ldcTime = URIRef(NAMESPACE + 'ldcTime')
link = URIRef(NAMESPACE + 'link')
linkTarget = URIRef(NAMESPACE + 'linkTarget')
month = URIRef(NAMESPACE + 'month')
naturalLanguageDescription = URIRef(NAMESPACE + 'naturalLanguageDescription')
noneOfTheAbove = URIRef(NAMESPACE + 'noneOfTheAbove')
numericValue = URIRef(NAMESPACE + 'numericValue')
privateData = URIRef(NAMESPACE + 'privateData')
prototype = URIRef(NAMESPACE + 'prototype')
queryId = URIRef(NAMESPACE + 'queryId')
refutingClaims = URIRef(NAMESPACE + 'refutingClaims')
relatedClaims = URIRef(NAMESPACE + 'relatedClaims')
sentiment = URIRef(NAMESPACE + 'sentiment')
shot = URIRef(NAMESPACE + 'shot')
source = URIRef(NAMESPACE + 'source')
sourceDocument = URIRef(NAMESPACE + 'sourceDocument')
start = URIRef(NAMESPACE + 'start')
startOffset = URIRef(NAMESPACE + 'startOffset')
startTimestamp = URIRef(NAMESPACE + 'startTimestamp')
subgraphContains = URIRef(NAMESPACE + 'subgraphContains')
subtopic = URIRef(NAMESPACE + 'subtopic')
supportingClaims = URIRef(NAMESPACE + 'supportingClaims')
system = URIRef(NAMESPACE + 'system')
textValue = URIRef(NAMESPACE + 'textValue')
timeType = URIRef(NAMESPACE + 'timeType')
topic = URIRef(NAMESPACE + 'topic')
xVariable = URIRef(NAMESPACE + 'xVariable')
year = URIRef(NAMESPACE + 'year')
