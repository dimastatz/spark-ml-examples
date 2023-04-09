import uuid
import mongomock

from models.lead import SfdcLead
from mongoengine import connect, disconnect


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