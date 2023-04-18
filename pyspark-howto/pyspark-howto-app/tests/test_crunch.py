import cruncher
import tests.utils.test_data_generator as test_data_generator

from models.lead import SfdcLead, SimpleLead
from models.lead_lean import LeadLean
from tests.utils.tenant_fixture import *


def test_create_df(spark_session, mongo_client):
    lead = SimpleLead()
    lead.FirstName = 'First Name Lead'
    lead.LastName = 'Last Name Lead'
    lead.Title = 'Title Name Lead'
    lead.save()    

    assert SimpleLead.count() == 1 


def test_crunch(tenant, spark_session):
    #test_data_generator.generate_sfdc_lead()
    #assert SfdcLead.count() == 1 
    #assert LeadLean.is_empty() 
    
    #test_data_generator.generate_lead_sf_fields()
    #assert SfdcLead.count() == 1
    
    cruncher.crunch(spark=spark_session)
    #assert LeadLean.count() == 1
    assert tenant == 1