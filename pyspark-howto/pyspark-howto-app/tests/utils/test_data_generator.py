import time
import random
import string
from datetime import datetime
from frozendict import frozendict
from models.lead import SfdcLead


SFDC_OBJECTS = (
    ("Account", "001"),
    ("Asset", "02i"),
    ("Campaign", "701"),
    ("Case", "500"),
    ("Contact", "003"),
    ("Contract", "800"),
    ("Event", "00U"),
    ("Group", "00G"),
    ("Lead", "00Q"),
    ("Opportunity", "006"),
    ("OpportunityHistory", "008"),
    ("Profile", "00e"),
    ("Task", "00T"),
    ("User", "005"),
    ("Calendar", "023"),
    ("EventRelation", "0RE"),
    ("Folder", "00l"),
    ("Attachment", "00P"),
    ("OpportunityTeamMember", "00q"),
    ("TaskRelation", "0RT"),
    ("AccountTeamMember", "01M"),
    ("OpportunityContactRole", "00K"),
    ("Note", "002"),
    ("AssistantRecommendation", "05q"),
    ("EmailMessage", "02s"),
    ("UserRole", "00E"),
    ("ForecastingType", "0Db"),
    ("ForecastingQuota", "0J9"),
    ("ForecastingPrediction", "0Lv"),
    ("ForecastingTypeSource", "0hl"),
    ("ForecastingSourceDefinition", "7sy"),
    ("ForecastingFilter", "0r0"),
    ("ForecastingFilterCondition", "1ZK"),
    ("ForecastingPredictionReason", "0Gf"),
    ("ForecastingPredictionElement", "01F"),
    ("ForecastingPredictionTrend", "0OA"),
    ("OpportunityScore", "0Gq"),
    ("OpportunitySplit", "049"),
    ("Individual", "0PK"),
    ("AccountInsight", "17a"),
    ("AccountInsightNewsArticle", "18a"),
    ("OpportunityInsight", "0OM"),
    ("ContactSuggestionInsight", "0Qs"),
    ("Quote", "0Q0"),
    ("OpportunityContactRoleSuggestionInsight", "0Qv"),
    ("PredictionDefinition", "1Pd"),
    ("RecordRecommendation", "0RR"),
    ("CampaignMember", "00v"),
    ("EngagementScore", "0Gq"),
    ("Note", "002"),
    ("LeadInsight", "0O9"),
    ("CampaignInsight", "0V0"),
    ("CampaignInsightRationale", "0Vm"),
    ("ListEmail", "0XB"),
    ("PardotTenant", "0Uv"),
    ("ModelFactor", "0O3"),
    ("MarketingForm", "1Mx"),
    ("LandingPage", "0S7"),
    ("ScoreIntelligence", "0Gq"),
    ("LeadIQConfiguration", "0OC"),
    ("SalesAIScoreCycle", "7D5"),
    ("SalesAIScoreModelFactor", "1tF"),
    ("CampaignInfluenceModel", "03V"),
    ("CampaignInfluence", "0KK"),
    ("Period", "026"),
    ("VoiceCall", "0LQ"),
    ("VoiceCallRecording", "0Ox"),
    ("VideoCall", "6qr"),
    ("VideoCallRecording", "3Qh"),
    ("VideoCallParticipant", "1af"),
    ("CallCoachingMediaProvider", "0hn"),
    ("WorkForecastDemogRun", "0ba"),
    ("Workload", "08S"),
    ("WorkloadUnit", "0Y9"),
    ("WorkDemographic", "0cL"),
    ("WorkForecastRun", "0ZN"),
    ("AIRecordInsight", "9qb"),
    ("AIInsightValue", "9qc"),
    ("AIInsightReason", "0T2"),
    ("MLModel", "873"),
    ("OpportunityStage", "01J"),
)

LAST_UPDATE_TIME_FIELD = "last_update_time"

sfdc_now = datetime.now().microsecond

SFObjects = type(
    "SFObjects", (object,), {name: i + 1 for i, (name, _) in enumerate(SFDC_OBJECTS)}
)

SF_TYPE_TO_ID_PREFIX = frozendict(
    {getattr(SFObjects, name): prefix for name, prefix in SFDC_OBJECTS}
)


def generate_sfdc_lead(**kwargs) -> dict:
    lead = {
        "Id": get_random_type(SFObjects.Lead),
        "Email": "lead@a.com",
        "FirstName": "Lead",
        "LastName": "Leader",
        "Name": "Lead Leader",
        "Company": "YKK",
        "IsConverted": "false",
        "Phone": "202-555-0187",
        "MobilePhone": "202-555-0187",
        "Country": "USA",
        "OwnerId": "005d000000PPOOLLKK",
        "CreatedById": "005d000000PPOOLLKK",
        "LastModifiedById": "005d000000PPOOLLKK",
        "SystemModstamp": sfdc_now,
        "CreatedDate": sfdc_now,
        "crunched": False,
        LAST_UPDATE_TIME_FIELD: sfdc_now,
    }
     
    lead.update(**kwargs)

    if "ConvertedOpportunityId" in kwargs or "ConvertedContactId" in kwargs:
        lead.update({"IsConverted": "true"})

    SfdcLead.get_collection().insert_one(lead)
    return lead




def generate_lead_sf_fields(extra_fields=None):
    fields = [
        {"name": "Id", "type": SFTypes.String, "custom": False},
        {"name": "Email", "type": SFTypes.Email, "custom": False},
        {"name": "Name", "type": SFTypes.String, "custom": False},
        {"name": "Website", "type": SFTypes.String, "custom": False},
        {"name": "FirstName", "type": SFTypes.String, "custom": False},
        {"name": "LastName", "type": SFTypes.String, "custom": False},
        {"name": "Title", "type": SFTypes.String, "custom": False},
        {"name": "City", "type": SFTypes.String, "custom": False},
        {"name": "EmailBouncedReason", "type": SFTypes.String, "custom": False},
        {"name": "Industry", "type": SFTypes.String, "custom": False},
        {"name": "LeadSource", "type": SFTypes.String, "custom": False},
        {"name": "AnnualRevenue", "type": SFTypes.Currency, "custom": False},
        {"name": "NumberOfEmployees", "type": SFTypes.Int, "custom": False},
        {"name": "IsConverted", "type": SFTypes.Boolean, "custom": False},
        {"name": "HasOptedOutOfEmail", "type": SFTypes.Boolean, "custom": False},
        {"name": "HasOptedOutOfFax", "type": SFTypes.Boolean, "custom": False},
        {"name": "IsUnreadByOwner", "type": SFTypes.Boolean, "custom": False},
        {"name": "OwnerId", "type": SFTypes.String, "custom": False},
        {"name": "CreatedById", "type": SFTypes.String, "custom": False},
        {"name": "LastModifiedById", "type": SFTypes.String, "custom": False},
        {"name": "Company", "type": SFTypes.String, "custom": False},
        {"name": "ConvertedOpportunityId", "type": SFTypes.String, "custom": False},
        {"name": "ConvertedContactId", "type": SFTypes.String, "custom": False},
        {"name": "Status", "type": SFTypes.PickList, "custom": False},
        {"name": "Rating", "type": SFTypes.PickList, "custom": False},
        {"name": "Phone", "type": SFTypes.Phone, "custom": False},
        {"name": "Country", "type": SFTypes.String, "custom": False},
        {"name": "MobilePhone", "type": SFTypes.Phone, "custom": False},
        {"name": "LastActivityDate", "type": SFTypes.Date, "custom": False},
        {"name": "Numeric__C", "type": SFTypes.Int, "custom": True},
        {"name": "CFieldAddress", "type": SFTypes.String, "custom": True},
        {"name": "CFieldString", "type": SFTypes.String, "custom": True},
    ]

    if extra_fields:
        fields += extra_fields

    SfObjectFields.get_collection().update_one(
        {"table": "Lead"},
        {
            "$set": {
                "fields_metadata": fields,
                "fetched_fields": [field["name"] for field in fields],
            }
        },
        upsert=True,
    )


def get_random_type(sfdc_object_type):
    valid_sfdc_object_prefix = SF_TYPE_TO_ID_PREFIX.get(sfdc_object_type)
    return valid_sfdc_object_prefix + "".join(
        random.choice(string.ascii_lowercase)
        for _ in range(18 - len(valid_sfdc_object_prefix))
    )


def cast_mongo_id(item: dict) -> dict:
    item['_id'] = str(item['_id'])
    return item 
