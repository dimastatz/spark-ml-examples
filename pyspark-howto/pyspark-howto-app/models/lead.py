from mongoengine import *
from pymongo import MongoClient


def read(client: MongoClient, db_name: str, collection: str, company: str) -> list:
    db = client.get_database(db_name)
    cur = db.get_collection(collection).find(company=company)
    return list(cur)


def write(client: MongoClient, db_name: str, collection: str, lead: str) -> str:
    db = client.get_database(db_name)
    collection = db.get_collection(collection)
    return collection.insert_one(lead).inserted_id


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
