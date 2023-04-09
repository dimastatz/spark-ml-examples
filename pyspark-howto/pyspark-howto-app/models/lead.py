from mongoengine import *


class SfdcLead(Document):
    db_colc_name = "Lead"

    FirstName = StringField()
    LastName = StringField()
    Title = StringField()
    AnnualRevenue = StringField()
    NumberOfEmployees = StringField()
    Company = StringField()
    IsConverted = StringField()

    is_deleted = BooleanField()
    skip = BooleanField()
    last_update_time = IntField()


    @classmethod  # index 2
    def get_converted_lead_sfids(cls, sfids):
        return set(
            cls.objects(Id__in=list(sfids), IsConverted="true").values_list("Id")
        )
