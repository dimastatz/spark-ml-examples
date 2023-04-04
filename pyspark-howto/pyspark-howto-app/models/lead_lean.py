import mongoengine as meng


DEFAULT_SEGMENT_ID = 0


def build_model_meta(**kwargs):
    assert "auto_create_index" not in kwargs
    meta = {"auto_create_index": False, "queryset_class": ImplisitQuerySet}
    meta.update(kwargs)
    return meta


class ImplisitQuerySet(meng.QuerySetNoCache):
    def first(self):  # pylint: disable=useless-super-delegation
        return super(ImplisitQuerySet, self.limit(1)).first()


class _LeadLeanBase():
    meta = build_model_meta(abstract=True)
    now_override = None
    drop_on_crunch_reset = True

    create_date = meng.DateTimeField(required=True)
    modify_date = meng.DateTimeField()
    is_converted = meng.BooleanField()  # crunched IsConverted field
    converted = meng.BooleanField(
        required=True
    )  # converted as defined by conversion milestone
    converted_upon_creation = meng.BooleanField()
    has_valid_phone = meng.BooleanField(required=True)
    has_valid_mobile = meng.BooleanField(required=True)
    email_prefix = meng.StringField()
    email_domain = meng.StringField()
    email_domain_similarity = meng.BooleanField()
    title_rank = meng.StringField()
    owner_yearly_win_rate = meng.FloatField()
    num_future_tasks = meng.IntField(default=0)
    num_future_events = meng.IntField(default=0)
    total_num_tasks = meng.IntField(default=0)
    total_num_events = meng.IntField(default=0)
    LastActivityDate = meng.StringField()

    Id = meng.StringField()
    segment_id = meng.IntField(required=True, default=DEFAULT_SEGMENT_ID)
    FirstName = meng.StringField()
    LastName = meng.StringField()

    # Local Name fields allow you to define a translated value for a record name.
    # They need to be requested from Salesforce Support before they can be used.
    FirstNameLocal = meng.StringField()
    LastNameLocal = meng.StringField()

    Name = meng.StringField()
    Title = meng.StringField()
    AnnualRevenue = meng.StringField()
    NumberOfEmployees = meng.StringField()
    Company = meng.StringField()
    Website = meng.StringField()
    ConvertedOpportunityId = meng.StringField()
    ConvertedContactId = meng.StringField()
    ConvertedAccountId = meng.StringField()
    ConvertedDate = meng.StringField()
    OwnerId = meng.StringField()
    IsUnreadByOwner = meng.StringField()
    LastModifiedById = meng.StringField()
    Status = meng.StringField()
    Salutation = meng.StringField()
    HasOptedOutOfEmail = meng.StringField()
    HasOptedOutOfFax = meng.StringField()
    LeadSource = meng.StringField()
    Latitude = meng.StringField()
    Longitude = meng.StringField()
    Industry = meng.StringField()
    MobilePhone = meng.StringField()
    Phone = meng.StringField()
    Country = meng.StringField()
    CountryCode = meng.StringField()
    StateCode = meng.StringField()
    Email = meng.StringField()
    EmailBouncedReason = meng.StringField()
    Rating = meng.StringField()


class LeadLean(_LeadLeanBase):
    db_colc_name = "lead_lean"
