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
    print(first.FirstName, first.LastName)
    assert first.FirstName == lead.FirstName

    disconnect()


def test_write(mongo_client):
    lead_in = { 'name': 'lead 1', 'company': 'lead 1 company' }
    lead_id = write(mongo_client, 'leads_db', 'leads', lead=lead_in)
    print('lead_in', lead_id)
    lead_out = read(mongo_client, 'leads_db', 'leads', company='lead 1 company')
    print('lead_out', lead_out[0])
    assert lead_in['name'] == lead_out[0]['name']
    assert lead_id == lead_out[0]['_id']



