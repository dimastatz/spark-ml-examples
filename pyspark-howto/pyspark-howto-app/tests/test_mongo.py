import uuid
import mongomock

from models.lead import *
from mongoengine import *
from tests.utils.tenant_fixture import *


def test_leads():
    connect('mongoenginetest', 
            host='mongodb://localhost',
            mongo_client_class=mongomock.MongoClient, 
            uuidRepresentation='standard')
    
    lead = SfdcLead()
    lead.FirstName = 'Lead'
    lead.LastName = 'Leader'
    lead.save()

    first = SfdcLead.objects().first()
    print(first.FirstName, first.LastName, dict(first.to_mongo()))
    assert first.FirstName == lead.FirstName

    disconnect()


def test_write(mongo_client):
    lead_in = { 'name': 'lead 1', 'company': 'lead 1 company' }
    lead_id = write(mongo_client, 'leads_db', 'leads', lead=lead_in)
    print('lead_in', lead_id)
    lead_out = read(mongo_client, 'leads_db', 'leads', company='lead 1 company')
    print('lead_out', lead_out[0], type(lead_out[0]))
    assert lead_in['name'] == lead_out[0]['name']
    assert lead_id == lead_out[0]['_id']


def test_mongo_to_df(mongo_client, spark_session):
    db_name = 'leads_db'
    collection = 'leads'

    for i in range(1, 4):
        lead_in = { 'name': f'lead {i}', 'company': f'lead {i} company' }
        write(mongo_client, db_name, collection, lead_in)
    
    leads = read(mongo_client, 'leads_db', 'leads', company='lead *')
    assert len(leads) == 4

    for lead in leads:
        del(lead['_id'])

    print(leads)
    df = spark_session.createDataFrame(leads)
    df.show()

    assert df.count() == 4
    

