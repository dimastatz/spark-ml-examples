import mongoengine as meng


class SfdcLead():
    db_colc_name = "Lead"

    FirstName = meng.StringField()
    LastName = meng.StringField()
    Title = meng.StringField()
    AnnualRevenue = meng.StringField()
    NumberOfEmployees = meng.StringField()
    Company = meng.StringField()
    IsConverted = meng.StringField()

    is_deleted = meng.BooleanField()
    skip = meng.BooleanField()
    last_update_time = meng.IntField()


    @classmethod  # index 2
    def get_converted_lead_sfids(cls, sfids):
        return set(
            cls.objects(Id__in=list(sfids), IsConverted="true").values_list("Id")
        )
